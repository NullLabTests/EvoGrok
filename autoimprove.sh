#!/bin/bash
# auto_improve.sh: Automatically send current main.py and evo.log to Grok to get improvement suggestions,
# then update main.py accordingly, enabling live self-updating of code.
# Requirements: XAI_API_KEY must be set in your environment.
# Usage: Run this script in your project root where main.py and evo.log are located.

set -e

while true; do
    echo "=== Auto-Improve Cycle Started at $(date) ==="

    # Read current code from main.py
    CODE=$(cat main.py)
    
    # Read logs if available; otherwise, use placeholder text
    if [ -f evo.log ]; then
        LOGS=$(cat evo.log)
    else
        LOGS="No logs available."
    fi

    # Prepare the prompt to send to Grok-2. We need to JSON encode the prompt properly.
    PROMPT=$(python3 -c "import json; 
print(json.dumps(
    'Improve the following code based on these logs. Provide a fully improved version of main.py that fixes errors and enhances autonomous self-updating capabilities. Code: '''\n$CODE\n''' Logs: '''\n$LOGS\n''''
))")
    
    echo "Sending prompt to Grok-2 for code improvement..."
    
    # Call the OpenAI API using a Python one-liner
    IMPROVED=$(python3 - <<PY
import os, openai, json
openai.api_key = os.getenv('XAI_API_KEY')
response = openai.ChatCompletion.create(
    model='grok-2',
    messages=[{"role": "user", "content": json.loads('$PROMPT')}],
    max_tokens=1000,
    temperature=0.8
)
print(response.choices[0].message.content.strip())
PY
)
    
    if [ -n "$IMPROVED" ]; then
        echo "$IMPROVED" > main.py
        echo "main.py updated successfully at $(date)."
    else
        echo "No improvement received at $(date)."
    fi

    echo "=== Auto-Improve Cycle Completed. Sleeping for 4 minutes... ==="
    sleep 240
done

