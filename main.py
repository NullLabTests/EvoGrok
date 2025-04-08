import os
import sqlite3
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import random
from collections import deque
import requests
import psutil
from openai import OpenAI
import logging
import time
import ast
from datetime import datetime
import importlib.util

# --- Setup ---

# Load XAI_API_KEY from environment
XAI_API_KEY = os.getenv("XAI_API_KEY")
if not XAI_API_KEY:
    raise ValueError("XAI_API_KEY must be set in the environment")

# Initialize OpenAI client for xAI API
client = OpenAI(api_key=XAI_API_KEY, base_url="https://api.x.ai/v1")

# Set up logging
logging.basicConfig(filename="evo_combined.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Initialize database
DB_PATH = "evo_combined.db"
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create tables if they don’t exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS tentacles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT,
    performance REAL,
    creation_time TIMESTAMP,
    parent_id INTEGER,
    domains TEXT
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS challenges (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT,
    input TEXT,
    expected_output TEXT,
    domain TEXT
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS knowledge (
    key TEXT PRIMARY KEY,
    value TEXT,
    fetch_count INTEGER,
    last_fetched TIMESTAMP
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS logs (
    timestamp TIMESTAMP,
    action TEXT,
    reward REAL,
    state TEXT
)
''')
conn.commit()

# Define a diverse set of challenges
challenges = [
    {"description": "convert the text to lowercase", "input": "Hello WORLD!", "expected": "helloworld!", "domain": "text processing"},
    {"description": "evaluate the mathematical expression", "input": "2 + 2", "expected": "4", "domain": "mathematics"},
    {"description": "determine if the statement is true or false", "input": "If A implies B and B implies C, then A implies C.", "expected": "True", "domain": "logic"},
    {"description": "sort the list of numbers", "input": "3,1,4,2", "expected": "1,2,3,4", "domain": "data analysis"},
    {"description": "extract URLs from the text", "input": "Visit https://x.ai for more info.", "expected": "https://x.ai", "domain": "text processing"},
    {"description": "count the number of words", "input": "This is a test.", "expected": "4", "domain": "text processing"},
    {"description": "check if the number is prime", "input": "7", "expected": "True", "domain": "mathematics"},
    {"description": "find the maximum in the list", "input": "[3,1,4,2]", "expected": "4", "domain": "data analysis"},
    {"description": "evaluate the logical expression", "input": "True and False", "expected": "False", "domain": "logic"},
    {"description": "solve the equation for x", "input": "2*x + 3 = 7", "expected": "2", "domain": "mathematics"},
    {"description": "parse and extract entities from text", "input": "John went to Paris.", "expected": "Person: John, Location: Paris", "domain": "natural language processing"},
]

# Insert challenges into the database if not already present
for challenge in challenges:
    cursor.execute('INSERT OR IGNORE INTO challenges (description, input, expected_output, domain) VALUES (?, ?, ?, ?)',
                   (challenge["description"], challenge["input"], challenge["expected"], challenge["domain"]))
conn.commit()

# --- Deep Q-Network (DQN) ---

class DQN(nn.Module):
    def __init__(self, state_size, action_size):
        super(DQN, self).__init__()
        self.fc1 = nn.Linear(state_size, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, action_size)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return self.fc3(x)

class DQNAgent:
    def __init__(self, state_size, action_size):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        if self.device.type == "cuda":
            logging.info(f"Using GPU: {torch.cuda.get_device_name(self.device)}")
        else:
            logging.warning("GPU not available, using CPU")
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(maxlen=10000)
        self.gamma = 0.99  # Discount factor
        self.epsilon = 1.0  # Exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.model = DQN(state_size, action_size).to(self.device)
        self.target_model = DQN(state_size, action_size).to(self.device)
        self.optimizer = optim.Adam(self.model.parameters(), lr=0.001)
        self.update_target_model()

    def update_target_model(self):
        self.target_model.load_state_dict(self.model.state_dict())

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        state = torch.FloatTensor(state).unsqueeze(0).to(self.device)
        with torch.no_grad():
            q_values = self.model(state)
        return torch.argmax(q_values).item()

    def replay(self, batch_size):
        if len(self.memory) < batch_size:
            return
        minibatch = random.sample(self.memory, batch_size)
        for state, action, reward, next_state, done in minibatch:
            state = torch.FloatTensor(state).unsqueeze(0).to(self.device)
            next_state = torch.FloatTensor(next_state).unsqueeze(0).to(self.device)
            target = reward
            if not done:
                target = reward + self.gamma * torch.max(self.target_model(next_state)).item()
            target_f = self.model(state).detach().clone()
            target_f[0][action] = target
            loss = nn.MSELoss()(self.model(state), target_f)
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

# --- Tentacle Class ---

class Tentacle:
    def __init__(self, id, code, domains):
        self.id = id
        self.code = code
        self.domains = domains.split(',')
        self.performance = 0.0
        self.file_path = f"tentacle_{id}.py"
        with open(self.file_path, "w") as f:
            f.write(code)
        spec = importlib.util.spec_from_file_location(f"tentacle_{id}", self.file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.func = module.tentacle

    def solve(self, input_data):
        try:
            return self.func(input_data)
        except Exception as e:
            logging.error(f"Tentacle {self.id} failed: {e}")
            return None

# Load existing tentacles from the database
tentacles = {}
cursor.execute('SELECT id, code, domains FROM tentacles')
for row in cursor.fetchall():
    tentacle_id, code, domains = row
    tentacles[tentacle_id] = Tentacle(tentacle_id, code, domains)

# --- Action Functions ---

def evolve_tentacle():
    """Evolve a new tentacle using Grok-2 based on high-performing parents and domain knowledge."""
    try:
        cursor.execute('SELECT id, code, domains FROM tentacles ORDER BY performance DESC LIMIT 2')
        parents = cursor.fetchall()
        if len(parents) < 2:
            logging.warning("Not enough tentacles to evolve")
            return -1.0
        parent1_id, parent1_code, parent1_domains = parents[0]
        parent2_id, parent2_code, parent2_domains = parents[1]
        all_domains = list(set(parent1_domains.split(',') + parent2_domains.split(',')))
        # Fetch relevant knowledge
        placeholders = ','.join('?' * len(all_domains))
        cursor.execute(f'SELECT key, value FROM knowledge WHERE key IN ({placeholders})', all_domains)
        knowledge = "\n".join([f"{key}: {value[:200]}" for key, value in cursor.fetchall()])
        # Generate new tentacle code
        prompt = f"Generate a new Python tentacle function based on these parents and knowledge:\nParent1:\n{parent1_code}\nParent2:\n{parent2_code}\nKnowledge:\n{knowledge}"
        response = client.chat.completions.create(
            model="grok-2-latest",
            messages=[{"role": "user", "content": prompt}]
        )
        new_code = response.choices[0].message.content.strip()
        if "```python" in new_code:
            new_code = new_code.split("```python")[1].split("```")[0].strip()
        # Validate syntax
        try:
            ast.parse(new_code)
        except SyntaxError:
            logging.error("Invalid syntax in generated tentacle code")
            return -1.0
        # Insert into database
        cursor.execute('INSERT INTO tentacles (code, performance, creation_time, parent_id, domains) VALUES (?, ?, ?, ?, ?)',
                       (new_code, 0.0, datetime.now(), parent1_id, ",".join(all_domains)))
        conn.commit()
        tentacle_id = cursor.lastrowid
        tentacles[tentacle_id] = Tentacle(tentacle_id, new_code, ",".join(all_domains))
        logging.info(f"Evolved new tentacle: tentacle_{tentacle_id}")
        return 1.0
    except Exception as e:
        logging.error(f"Evolve tentacle failed: {e}")
        return -1.0

def test_tentacles():
    """Test a tentacle on a random challenge and update its performance."""
    try:
        available_domains = set()
        for tentacle in tentacles.values():
            available_domains.update(tentacle.domains)
        logging.info(f"Available domains: {available_domains}")
        
        if not available_domains:
            logging.warning("No tentacles available for any domain")
            return -1.0
        
        placeholders = ','.join('?' * len(available_domains))
        cursor.execute(f'SELECT * FROM challenges WHERE domain IN ({placeholders}) ORDER BY RANDOM() LIMIT 1', list(available_domains))
        challenge = cursor.fetchone()
        if not challenge:
            logging.warning("No challenges found for available domains")
            return -1.0
        challenge_id, description, input_data, expected_output, domain = challenge
        logging.info(f"Selected challenge {challenge_id} for domain: {domain}")
        
        domain_tentacles = [t for t in tentacles.values() if domain in t.domains]
        if not domain_tentacles:
            logging.warning(f"No tentacles for domain: {domain}")
            return -1.0
        
        best_tentacle = max(domain_tentacles, key=lambda t: t.performance)
        output = best_tentacle.solve(input_data)
        reward = 5.0 if str(output) == expected_output else 0.0
        best_tentacle.performance += reward / 5.0
        cursor.execute('UPDATE tentacles SET performance = ? WHERE id = ?', (best_tentacle.performance, best_tentacle.id))
        conn.commit()
        logging.info(f"Tested tentacle {best_tentacle.id} on challenge {challenge_id}: Reward {reward}")
        return reward
    except Exception as e:
        logging.error(f"Test tentacles failed: {e}")
        return -1.0

def fetch_knowledge():
    """Fetch and summarize a Wikipedia page for a random domain using Grok-2."""
    try:
        domains = list(set([challenge["domain"] for challenge in challenges]))
        domain = random.choice(domains)
        url = f"https://en.wikipedia.org/wiki/{domain.replace(' ', '_')}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        content = response.text[:1000]  # Limit content size
        summary = client.chat.completions.create(
            model="grok-2-latest",
            messages=[{"role": "user", "content": f"Summarize this: {content}"}]
        ).choices[0].message.content
        cursor.execute('INSERT OR REPLACE INTO knowledge (key, value, fetch_count, last_fetched) VALUES (?, ?, 1, ?)',
                       (domain, summary, datetime.now()))
        conn.commit()
        logging.info(f"Fetched knowledge for domain: {domain}")
        return 1.0
    except Exception as e:
        logging.error(f"Fetch knowledge failed: {e}")
        return -1.0

def optimize_resources():
    """Delete low-performing tentacles if CPU or memory usage exceeds 60%, preserving domain coverage."""
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    if cpu > 60 or mem > 60:
        domain_tentacles = {}
        for tentacle in tentacles.values():
            for domain in tentacle.domains:
                domain_tentacles.setdefault(domain, []).append(tentacle)
        
        deletable_tentacles = []
        for tentacle in tentacles.values():
            can_delete = True
            for domain in tentacle.domains:
                if len(domain_tentacles[domain]) <= 1:
                    can_delete = False
                    break
            if can_delete:
                deletable_tentacles.append(tentacle)
        
        if deletable_tentacles:
            to_delete = min(deletable_tentacles, key=lambda t: t.performance)
            cursor.execute('DELETE FROM tentacles WHERE id = ?', (to_delete.id,))
            conn.commit()
            del tentacles[to_delete.id]
            if os.path.exists(to_delete.file_path):
                os.remove(to_delete.file_path)
            logging.info(f"Deleted tentacle {to_delete.id} (domains: {to_delete.domains}) due to high resource usage")
            return 1.0
        else:
            logging.info("No tentacles deleted; preserving domain coverage")
    return 0.0

# --- State Function ---

def get_state():
    """Get the current system state for the DQN agent."""
    tentacle_count = len(tentacles)
    avg_performance = np.mean([t.performance for t in tentacles.values()]) if tentacles else 0
    knowledge_size = cursor.execute('SELECT COUNT(*) FROM knowledge').fetchone()[0]
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    return np.array([tentacle_count, avg_performance, knowledge_size, cpu, mem], dtype=np.float32)

# --- Main Loop ---

# Initialize DQN agent (state size: 5, action size: 4)
agent = DQNAgent(state_size=5, action_size=4)  # Actions: evolve, test, fetch, optimize

# Seed initial tentacles if fewer than 3 exist
cursor.execute('SELECT COUNT(*) FROM tentacles')
tentacle_count = cursor.fetchone()[0]
if tentacle_count < 3:
    default_code1 = "def tentacle(input_data):\n    return str(input_data).lower()"
    default_code2 = "def tentacle(input_data):\n    try:\n        return str(eval(input_data))\n    except:\n        return 'Error'"
    default_code3 = "def tentacle(input_data):\n    return ','.join(sorted(input_data.split(',')))"
    cursor.execute('INSERT OR IGNORE INTO tentacles (code, performance, creation_time, domains) VALUES (?, ?, ?, ?)',
                   (default_code1, 0.0, datetime.now(), "text processing"))
    cursor.execute('INSERT OR IGNORE INTO tentacles (code, performance, creation_time, domains) VALUES (?, ?, ?, ?)',
                   (default_code2, 0.0, datetime.now(), "mathematics"))
    cursor.execute('INSERT OR IGNORE INTO tentacles (code, performance, creation_time, domains) VALUES (?, ?, ?, ?)',
                   (default_code3, 0.0, datetime.now(), "data analysis"))
    conn.commit()
    # Reload tentacles
    cursor.execute('SELECT id, code, domains FROM tentacles')
    for row in cursor.fetchall():
        tentacle_id, code, domains = row
        if tentacle_id not in tentacles:
            tentacles[tentacle_id] = Tentacle(tentacle_id, code, domains)
    logging.info(f"Initialized {len(tentacles)} tentacles")

iteration = 0
try:
    while True:
        state = get_state()
        action = agent.act(state)
        if action == 0:
            reward = evolve_tentacle()
            action_name = "evolve_tentacle"
        elif action == 1:
            reward = test_tentacles()
            action_name = "test_tentacles"
        elif action == 2:
            reward = fetch_knowledge()
            action_name = "fetch_knowledge"
        elif action == 3:
            reward = optimize_resources()
            action_name = "optimize_resources"
        next_state = get_state()
        agent.remember(state, action, reward, next_state, False)
        agent.replay(batch_size=32)
        if iteration % 100 == 0:
            agent.update_target_model()
        logging.info(f"Iteration {iteration}: Action={action_name}, Reward={reward}, State={state.tolist()}")
        iteration += 1
        time.sleep(1)  # Prevent overloading
except KeyboardInterrupt:
    logging.info("Script stopped by user")
finally:
    conn.close()
