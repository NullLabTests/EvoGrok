import os
import sqlite3
import random
import numpy as np
import logging
from openai import OpenAI

# Configure logging early to avoid missing logs
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("evo.log"),
        logging.StreamHandler()
    ]
)

# Optionally use GPU if available (for potential future use)
try:
    import torch
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    logging.info(f"Using device: {device}")
except ImportError:
    device = None
    logging.info("Torch not installed. Running on CPU.")

# Load xAI API Key
XAI_API_KEY = os.getenv("XAI_API_KEY")
if not XAI_API_KEY:
    raise ValueError("XAI_API_KEY is not set in environment.")

# Initialize Grok/xAI API client
client = OpenAI(api_key=XAI_API_KEY, base_url="https://api.x.ai/v1")

# Database
DB_PATH = "evo_w_grok.db"

# Evolution config
POPULATION_SIZE = 100
MUTATION_RATE = 0.1

class Agent:
    def __init__(self):
        self.alpha = random.uniform(0, 1)
        self.gamma = random.uniform(0, 1)
        self.epsilon = random.uniform(0, 1)
        self.epsilon_decay = random.uniform(0, 1)

    def fitness(self):
        return self.alpha * 0.4 + self.gamma * 0.3 + self.epsilon * 0.2 + self.epsilon_decay * 0.1

    def mutate(self):
        if random.random() < MUTATION_RATE:
            self.alpha = np.clip(self.alpha + random.uniform(-0.1, 0.1), 0, 1)
            self.gamma = np.clip(self.gamma + random.uniform(-0.1, 0.1), 0, 1)
            self.epsilon = np.clip(self.epsilon + random.uniform(-0.1, 0.1), 0, 1)
            self.epsilon_decay = np.clip(self.epsilon_decay + random.uniform(-0.1, 0.1), 0, 1)

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
            generation, agent.alpha, agent.gamma, agent.epsilon,
            agent.epsilon_decay, fitness, prompt, response, tokens
        ))
        conn.commit()
        conn.close()
        logging.info(f"Generation {generation} logged.")
    except sqlite3.Error as e:
        logging.error(f"Failed to log generation {generation}: {e}")

def construct_grok_prompt(agent):
    return (
        f"Analyze these AI agent parameters: alpha={agent.alpha:.2f}, gamma={agent.gamma:.2f}, "
        f"epsilon={agent.epsilon:.2f}, epsilon_decay={agent.epsilon_decay:.2f}. "
        "Suggest improvements."
    )

def query_grok(prompt):
    try:
        logging.info("Sending query to Grok-2...")
        response = client.chat.completions.create(
            model="grok-2",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2048,
            temperature=0.7,
        )
        content = response.choices[0].message.content
        tokens_used = getattr(response.usage, "total_tokens", 2048)
        return content, tokens_used
    except Exception as e:
        logging.warning(f"Grok query failed: {e}")
        return f"[Mock Response] Insight based on: {prompt}", 0

def evolve(population):
    survivors = sorted(population, key=lambda a: a.fitness(), reverse=True)[:POPULATION_SIZE // 2]
    offspring = []
    for _ in range(POPULATION_SIZE // 2):
        p1, p2 = random.sample(survivors, 2)
        child = Agent()
        child.alpha = (p1.alpha + p2.alpha) / 2
        child.gamma = (p1.gamma + p2.gamma) / 2
        child.epsilon = (p1.epsilon + p2.epsilon) / 2
        child.epsilon_decay = (p1.epsilon_decay + p2.epsilon_decay) / 2
        child.mutate()
        offspring.append(child)
    return survivors + offspring

def main():
    initialize_db()
    population = [Agent() for _ in range(POPULATION_SIZE)]
    generation = 0

    while True:
        logging.info(f"=== Generation {generation} ===")
        best_agent = max(population, key=lambda a: a.fitness())
        fitness = best_agent.fitness()
        prompt = construct_grok_prompt(best_agent)

        grok_response, tokens = query_grok(prompt)

        log_generation(generation, best_agent, fitness, prompt, grok_response, tokens)
        logging.info(f"Fitness: {fitness:.4f}")
        logging.info(f"Grok insight: {grok_response[:200]}...")

        population = evolve(population)
        generation += 1

if __name__ == "__main__":
    main()

