# EvoGrok

**EvoGrok** is an evolutionary AI framework that leverages insights from Grok-2 for continuous self-improvement and growth. The system uses an evolutionary algorithm to optimize agent parameters (alpha, gamma, epsilon, epsilon_decay) while querying the Grok-2 model for expert insights. It logs every generation's progress in an SQLite database.

## Features

- **Evolutionary Algorithm:** Agents evolve via selection, crossover, and mutation.
- **Grok-2 Integration:** Query the Grok-2 model for suggestions to improve agent parameters.
- **Database Logging:** Stores generation details and insights in a local SQLite database.
- **Robust & Extensible:** Designed with logging, error handling, and continuous operation for production use.

## Getting Started

### Prerequisites

- Python 3.8+
- Environment variable \`XAI_API_KEY\` set to your xAI API key.
- Packages: \`openai\`, \`numpy\` (and optionally \`torch\` for GPU usage)


### Running the Project

To start the evolutionary algorithm (which runs indefinitely), simply run:

```bash
python main.py
```

## Project File Tree

```
EvoGrok/
├── LICENSE
├── README.md
├── main.py
└── requirements.txt
```

## Continuous Learning

EvoGrok is designed to run continuously on high-end GPUs (if available) or CPUs, evolving and learning over generations. You can adjust the parameters in \`main.py\` to tailor its behavior.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Project File Tree

EvoGrok/
├── LICENSE
├── README.md
├── main.py
└── requirements.txt

