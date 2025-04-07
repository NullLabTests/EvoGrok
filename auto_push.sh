#!/bin/bash
# auto_push.sh - Automatically commit and push changes every 4 minutes without using cron

# Ensure you run this script from the root of your git repository.

while true; do
    # Stage all changes (added, modified, deleted)
    git add -A

    # Check if there are any changes to commit
    if ! git diff-index --quiet HEAD --; then
        commit_msg="Auto update $(date +'%Y-%m-%d %H:%M:%S')"
        git commit -m "$commit_msg"
        # Push the current branch to the upstream remote. Adjust branch name if needed.
        git push -u origin $(git rev-parse --abbrev-ref HEAD)
        echo "Committed and pushed changes at $(date)."
    else
        echo "No changes detected at $(date)."
    fi

    # Sleep for 4 minutes (240 seconds)
    sleep 240
done

