import os
import sqlite3
import random
import numpy as np
import logging
import time
from openai import OpenAI

# Configure logging to file and console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("evo.log"), logging.StreamHandler()]
)

# Optionally use GPU if available (for future extensions)
try:
    import torch
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    logging.info(f"Using device: {device}")
except ImportError:
    device = None
    logging.info("Torch not installed. Running on CPU.")

# Load xAI API Key from environment
XAI_API_KEY = os.getenv("XAI_API_KEY")
if not XAI_API_KEY:
    raise ValueError("XAI_API_KEY is not set. Please configure your environment.")

# Initialize the xAI API client (Grok-2)
client = OpenAI(api_key=XAI_API_KEY, base_url="https://api.x.ai/v1")

# Database path for logging evolution
DB_PATH = "evo_w_grok.db"

# Evolutionary parameters
POPULATION_SIZE = 100
MUTATION_RATE = 0.15
MAX_GENERATIONS = 1000

# --------------------- Tool System ---------------------
class Tool:
    def __init__(self, name: str, func: callable, description: str = ""):
        self.name = name
        self.func = func
        self.description = description
        self.uses = 0

    def use(self, *args):
        self.uses += 1
        try:
            return f"Success: {self.func(*args)}"
        except Exception as e:
            return f"Failed: {e}"

class ToolBox:
    def __init__(self):
        self.tools = {
            "lower": Tool("lower", lambda x: x.lower(), "Converts text to lowercase"),
            "add": Tool("add", lambda x: str(eval(x)), "Evaluates arithmetic expressions")
        }
    
    def get(self, name: str):
        return self.tools.get(name)
    
    def list_tools(self):
        return list(self.tools.keys())
    
    def add_tool(self, name: str, func: callable, description: str):
        self.tools[name] = Tool(name, func, description)

# --------------------- Agent with Emergent Behavior ---------------------
class Agent:
    def __init__(self, toolbox: ToolBox):
        self.alpha = random.uniform(0, 1)
        self.gamma = random.uniform(0, 1)
        self.epsilon = random.uniform(0, 1)
        self.epsilon_decay = random.uniform(0, 1)
        self.toolbox = toolbox
        self.memory = []  # Records (task, tool used, result)
        self.tool_preferences = {}  # Map task to preferred tool
        self.fitness_history = []  # Track fitness over generations for self-reflection

    def fitness(self):
        base = self.alpha * 0.4 + self.gamma * 0.3 + self.epsilon * 0.2 + self.epsilon_decay * 0.1
        success_bonus = sum(1 for _, _, r in self.memory if "Success" in r) * 0.15
        coherence = self.calculate_coherence()
        emergence_bonus = len(self.toolbox.tools) * 0.05  # Reward diversity in tools
        return min(base + success_bonus + coherence + emergence_bonus, 3.0)

    def calculate_coherence(self):
        if not self.memory:
            return 0
        task_success = {}
        for task, tool, result in self.memory:
            task_success[task] = task_success.get(task, 0) + (1 if "Success" in result else 0)
        return (sum(task_success.values()) / max(1, len(self.memory))) * 0.3

    def mutate(self):
        if random.random() < MUTATION_RATE:
            delta = random.uniform(-0.15, 0.15)
            if self.fitness_history:
                delta *= (1.0 - self.fitness_history[-1] / 3.0)
            self.alpha = np.clip(self.alpha + delta, 0, 1)
            self.gamma = np.clip(self.gamma + delta * self.gamma, 0, 1)
            self.epsilon = np.clip(self.epsilon + delta * self.epsilon, 0, 1)
            self.epsilon_decay = np.clip(self.epsilon_decay + delta, 0, 1)

    def solve_task(self, task: str, input_data: str):
        if task in self.tool_preferences and random.random() > self.epsilon:
            tool_name = self.tool_preferences[task]
        else:
            tool_name = random.choice(self.toolbox.list_tools())
        tool = self.toolbox.get(tool_name)
        result = tool.use(input_data) if tool else "No tool available"
        self.memory.append((task, tool_name, result))
        if "Success" in result:
            self.tool_preferences[task] = tool_name
            self.epsilon = max(0.05, self.epsilon * 0.9)
        self.reflect(result)
        return result

    def reflect(self, result):
        fitness_val = self.fitness()
        self.fitness_history.append(fitness_val)
        if len(self.fitness_history) > 5:
            self.fitness_history.pop(0)
        if len(self.fitness_history) > 1:
            trend = self.fitness_history[-1] - self.fitness_history[-2]
            if trend < 0 and "Failed" in result:
                self.epsilon = min(1.0, self.epsilon + 0.1)
            elif trend > 0:
                self.alpha = min(1.0, self.alpha + 0.05)

    def request_tool(self, task: str):
        prompt = f"Generate a lambda function for the task: {task}. For example, use 'lambda x: x[::-1]' for reversing or 'lambda x: x.lower()' for lowercase conversion."
        try:
            response = client.chat.completions.create(
                model="grok-2",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500,
                temperature=0.9
            )
            code = response.choices[0].message.content.strip()
            if "lambda" in code:
                safe_locals = {}
                exec(f"func = {code}", {"__builtins__": {}}, safe_locals)
                tool_name = f"tool_{len(self.toolbox.tools)}"
                self.toolbox.add_tool(tool_name, safe_locals["func"], f"Auto-generated for {task}")
                logging.info(f"Added new tool: {tool_name} for task '{task}'")
                return tool_name
            else:
                logging.warning(f"Tool request did not yield a lambda: {code}")
        except Exception as e:
            logging.error(f"Tool request failed: {e}")
        return None

    def self_improve(self):
        improvement_prompt = (
            f"Analyze agent fitness history: {self.fitness_history}. Suggest parameter adjustments (alpha, gamma, epsilon, epsilon_decay) to enhance task-solving. Ensure all values remain between 0 and 1."
        )
        try:
            response = client.chat.completions.create(
                model="grok-2",
                messages=[{"role": "user", "content": improvement_prompt}],
                max_tokens=200,
                temperature=0.8
            )
            suggestion = response.choices[0].message.content.strip()
            logging.info(f"Self-improvement suggestion: {suggestion}")
            # Simulate minor adjustment:
            adjustment = random.uniform(-0.05, 0.05)
            self.alpha = np.clip(self.alpha + adjustment, 0, 1)
            return suggestion
        except Exception as e:
            logging.error(f"Self-improvement request failed: {e}")
            return "No suggestion"

# --------------------- Database Functions ---------------------
def initialize_db():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS evolution_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                generation INTEGER,
                best_alpha REAL,
                best_gamma REAL,
                best_epsilon REAL,
                best_epsilon_decay REAL,
                best_fitness REAL,
                grok_query TEXT,
                grok_response TEXT,
                tokens_used INTEGER,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        conn.close()
        logging.info("Database initialized.")
    except sqlite3.Error as e:
        logging.error(f"Database initialization failed: {e}")

def log_generation(generation, agent, fitness, prompt, response, tokens):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO evolution_log (
                generation, best_alpha, best_gamma, best_epsilon, best_epsilon_decay,
                best_fitness, grok_query, grok_response, tokens_used
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            generation, agent.alpha, agent.gamma, agent.epsilon, agent.epsilon_decay,
            fitness, prompt, response, tokens
        ))
        conn.commit()
        conn.close()
        logging.info(f"Generation {generation} logged.")
    except sqlite3.Error as e:
        logging.error(f"Failed to log generation {generation}: {e}")

def construct_grok_prompt(agent):
    memory_summary = (f"Memory: {len(agent.memory)} entries, "
                      f"{sum(1 for _,_,r in agent.memory if 'Success' in r)} successes.")
    return (f"Analyze this agent: alpha={agent.alpha:.2f}, gamma={agent.gamma:.2f}, "
            f"epsilon={agent.epsilon:.2f}, epsilon_decay={agent.epsilon_decay:.2f}. {memory_summary} "
            "Suggest improvements for adaptability and tool utilization.")

def query_grok(prompt):
    try:
        logging.info("Sending query to Grok-2...")
        response = client.chat.completions.create(
            model="grok-2",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2048,
            temperature=0.8
        )
        content = response.choices[0].message.content
        tokens_used = getattr(response.usage, "total_tokens", 2048)
        return content, tokens_used
    except Exception as e:
        logging.warning(f"Grok query failed: {e}")
        return f"[Mock Response] Insight for: {prompt}", 0

def evolve(population):
    survivors = sorted(population, key=lambda a: a.fitness(), reverse=True)[:POPULATION_SIZE // 2]
    offspring = []
    for _ in range(POPULATION_SIZE - len(survivors)):
        p1, p2 = random.sample(survivors, 2)
        child = Agent(p1.toolbox)
        child.alpha = np.clip((p1.alpha + p2.alpha) / 2 + random.uniform(-0.05, 0.05), 0, 1)
        child.gamma = np.clip((p1.gamma + p2.gamma) / 2 + random.uniform(-0.05, 0.05), 0, 1)
        child.epsilon = np.clip((p1.epsilon + p2.epsilon) / 2 + random.uniform(-0.05, 0.05), 0, 1)
        child.epsilon_decay = np.clip((p1.epsilon_decay + p2.epsilon_decay) / 2 + random.uniform(-0.05, 0.05), 0, 1)
        child.mutate()
        if random.random() < 0.3:
            child.tool_preferences = p1.tool_preferences.copy()
        offspring.append(child)
    return survivors + offspring

# --------------------- Main Loop ---------------------
def main():
    initialize_db()
    toolbox = ToolBox()
    population = [Agent(toolbox) for _ in range(POPULATION_SIZE)]
    tasks = [
        ("Lowercase Conversion", "HELLO WORLD"),
        ("Arithmetic Addition", "2 + 3"),
        ("Reverse String", "WORLD")
    ]
    generation = 0
    stagnant_count = 0
    last_avg_fitness = 0

    while generation < MAX_GENERATIONS:
        logging.info(f"=== Generation {generation} ===")
        best_agent = max(population, key=lambda a: a.fitness())
        fitness = best_agent.fitness()
        prompt = construct_grok_prompt(best_agent)
        
        for task, input_data in tasks:
            result = best_agent.solve_task(task, input_data)
            logging.info(f"Task '{task}' with input '{input_data}' yielded: {result}")
            if "Failed" in result and random.random() < 0.4:
                best_agent.request_tool(task)
        
        avg_fitness = sum(agent.fitness() for agent in population) / len(population)
        if abs(avg_fitness - last_avg_fitness) < 0.01:
            stagnant_count += 1
        else:
            stagnant_count = 0
        last_avg_fitness = avg_fitness
        if stagnant_count >= 5:
            logging.info("Fitness plateau detected, initiating self-improvement.")
            best_agent.self_improve()
            stagnant_count = 0
        
        grok_response, tokens = query_grok(prompt)
        log_generation(generation, best_agent, fitness, prompt, grok_response, tokens)
        logging.info(f"Generation {generation}: Fitness: {fitness:.4f}, Tools: {len(toolbox.tools)}")
        logging.info(f"Grok insight (first 200 chars): {grok_response[:200]}...")
        
        population = evolve(population)
        generation += 1
        time.sleep(1)  # Throttle loop to prevent overload

if __name__ == "__main__":
    main()
