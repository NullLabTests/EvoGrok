#!/bin/bash

# Define variables
LOG_FILE="evo.log"
CODE_FILE="main.py"
GROK_API_URL="https://api.x.ai/v1/chat/completions"
GROK_API_KEY="your-api-key-here"
CYCLE_INTERVAL=240  # 4 minutes

# Function to send logs and code to Grok-2 for analysis
send_to_grok() {
    local code_content
    local log_content
    log_content=$(tail -n 50 "$LOG_FILE")
    code_content=$(cat "$CODE_FILE")

    # Prepare payload for Grok-2
    payload=$(cat <<EOF
{
    "model": "grok-2",
    "messages": [
        {"role": "system", "content": "You are a code improvement assistant."},
        {"role": "user", "content": "Improve the following code based on these logs. Provide a fully improved version of main.py that fixes errors and enhances autonomous self-updating capabilities. Code:\n\n$code_content\n\nLogs:\n$log_content"}
    ],
    "max_tokens": 1500
}
EOF
)

    # Send request to Grok API and capture the response
    response=$(curl -s -X POST "$GROK_API_URL" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $GROK_API_KEY" \
        -d "$payload")

    # Log the raw response for debugging
    echo "Raw Grok API Response:" >> "$LOG_FILE"
    echo "$response" >> "$LOG_FILE"

    # Check if the response is valid JSON
    echo "$response" | jq . > /dev/null 2>&1
    if [[ $? -ne 0 ]]; then
        echo "Error: Invalid JSON response from Grok API" >> "$LOG_FILE"
        return
    fi

    # Extract and apply the suggestion from Grok
    new_code=$(echo "$response" | jq -r '.choices[0].message.content')
    if [[ -z "$new_code" ]]; then
        echo "Error: No code suggestions returned by Grok" >> "$LOG_FILE"
        return
    fi

    echo "$new_code" > "$CODE_FILE"
}

# Infinite loop to auto-improve
while true; do
    echo "=== Auto-Improve Cycle Started at $(date) ===" >> "$LOG_FILE"

    # Send logs and current code to Grok for analysis and improvement
    send_to_grok

    # Log success and wait for the next cycle
    echo "=== Auto-Improve Cycle Completed at $(date) ===" >> "$LOG_FILE"
    sleep "$CYCLE_INTERVAL"
done

