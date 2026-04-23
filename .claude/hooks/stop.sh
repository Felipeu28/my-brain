#!/usr/bin/env bash
# Fires when a Claude Code session finishes a task in knowledge-base.
osascript -e 'display notification "Task complete in knowledge-base" with title "Claude Code" sound name "Glass"'
echo "$(date): knowledge-base task completed" >> ~/.claude/task-log.txt
