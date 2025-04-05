import os
import sqlite3
import random
import numpy as np
import logging
from openai import OpenAI

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load API Key from environment
XAI_API_KEY = os.getenv("XAI_API_KEY")
if not XAI_API_KEY:
    raise ValueError("XAI_API_KEY is not set. Please configure your environment.")

# Initialize xAI API client
client = OpenAI(api_key=XAI_API_KEY, base_url="https://api.x.ai/v1")

# SQLite database path
DB_PATH = "evo_w_grok.db"

# Evolution parameters
POPULATION_SIZE = 100
GENERATIONS = 100
MUTATION_RATE = 0.1
CONVERGENCE_THRESHOLD = 0.001

# Grok-2 query parameters
GROK_QUERY_PROMPT = "Provide insights on the evolution of AI"

class Agent:
    """
    Represents an agent in the evolutionary algorithm with parameters:
    alpha, gamma, epsilon, and epsilon_decay.
    """
    def __init__(self):
        self.alpha = random.uniform(0, 1)
        self.gamma = random.uniform(0, 1)
        self.epsilon = random.uniform(0, 1)
        self.epsilon_decay = random.uniform(0, 1)

    def fitness(self):
        """
        Calculate the fitness of the agent using a weighted sum.
        Adjust weights as needed for your domain.
        """
        return self.alpha * 0.4 + self.gamma * 0.3 + self.epsilon * 0.2 + self.epsilon_decay * 0.1

    def mutate(self):
        """
        Mutate the agent's parameters with a given mutation rate.
        Values are clipped to remain within the [0, 1] interval.
        """
        if random.random() < MUTATION_RATE:
            self.alpha = np.clip(self.alpha + random.uniform(-0.1, 0.1), 0, 1)
            self.gamma = np.clip(self.gamma + random.uniform(-0.1, 0.1), 0, 1)
            self.epsilon = np.clip(self.epsilon + random.uniform(-0.1, 0.1), 0, 1)
            self.epsilon_decay = np.clip(self.epsilon_decay + random.uniform(-0.1, 0.1), 0, 1)

def initialize_db():
    """
    Initialize the SQLite database and create the evolution_log table if it does not exist.
    """
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
        logging.info("Database initialized successfully.")
    except sqlite3.Error as e:
        logging.error(f"Database initialization failed: {e}")

def log_generation(generation, best_agent, best_fitness, grok_query, grok_response, tokens_used):
    """
    Log the details of the current generation to the SQLite database.
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO evolution_log
            (generation, best_alpha, best_gamma, best_epsilon, best_epsilon_decay, best_fitness, grok_query, grok_response, tokens_used)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (generation, best_agent.alpha, best_agent.gamma, best_agent.epsilon, best_agent.epsilon_decay,
              best_fitness, grok_query, grok_response, tokens_used))
        conn.commit()
        conn.close()
        logging.info(f"Generation {generation} logged successfully.")
    except sqlite3.Error as e:
        logging.error(f"Logging generation {generation} failed: {e}")

def construct_grok_prompt(best_agent):
    """
    Construct a prompt for the Grok-2 query based on the best agent's parameters.
    """
    return (f"Analyze these AI agent parameters: alpha={best_agent.alpha:.2f}, gamma={best_agent.gamma:.2f}, "
            f"epsilon={best_agent.epsilon:.2f}, epsilon_decay={best_agent.epsilon_decay:.2f}. "
            "Suggest improvements.")

def query_grok(prompt):
    """
    Query the Grok-2 model with the given prompt and return the response and tokens used.
    """
    try:
        response = client.chat.completions.create(
            model="grok-2",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2048,
            temperature=0.7,
        )
        tokens_used = response.usage.total_tokens if hasattr(response.usage, "total_tokens") else 2048
        return response.choices[0].message.content, tokens_used
    except Exception as e:
        logging.error(f"Grok-2 query failed: {e}")
        return None, 0

def evolve(population):
    """
    Evolve the population by selecting the best agents, creating offspring through crossover,
    and applying mutation to the offspring.
    """
    selected_agents = sorted(population, key=lambda x: x.fitness(), reverse=True)[:int(POPULATION_SIZE / 2)]
    offspring = []
    for _ in range(int(POPULATION_SIZE / 2)):
        parent1, parent2 = random.sample(selected_agents, 2)
        child = Agent()
        child.alpha = (parent1.alpha + parent2.alpha) / 2
        child.gamma = (parent1.gamma + parent2.gamma) / 2
        child.epsilon = (parent1.epsilon + parent2.epsilon) / 2
        child.epsilon_decay = (parent1.epsilon_decay + parent2.epsilon_decay) / 2
        child.mutate()
        offspring.append(child)
    return selected_agents + offspring

def main():
    """
    Main function to run the evolutionary algorithm.
    """
    initialize_db()
    population = [Agent() for _ in range(POPULATION_SIZE)]
    last_best_fitness = 0
    for generation in range(GENERATIONS):
        best_agent = max(population, key=lambda x: x.fitness())
        best_fitness = best_agent.fitness()
        prompt = construct_grok_prompt(best_agent)
        grok_response, tokens_used = query_grok(prompt)
        if grok_response:
            log_generation(generation, best_agent, best_fitness, prompt, grok_response, tokens_used)
            logging.info(f"Generation {generation}: Fitness = {best_fitness:.4f}")
        else:
            logging.warning(f"Generation {generation}: Grok-2 response missing.")
        population = evolve(population)
        if abs(best_fitness - last_best_fitness) < CONVERGENCE_THRESHOLD:
            logging.info(f"Convergence reached at generation {generation}.")
            break
        last_best_fitness = best_fitness

if __name__ == "__main__":
    main()
