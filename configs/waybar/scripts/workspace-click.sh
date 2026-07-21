#!/bin/bash
# Workspace click handler for Qtile + Waybar

# Get the current workspace list from the file
workspaces=$(cat /tmp/qtile-groups.txt 2>/dev/null)

# Parse which workspace was clicked based on position
# This is a simplified version - clicks anywhere switches to workspace 1
# For proper position-based clicking, we'd need more complex logic

# For now, cycle through workspaces 1-12
current=$(qtile cmd-obj -o screen -f info | grep -o '"name": "[^"]*"' | head -1 | cut -d'"' -f4)

# Calculate next workspace
next=$(( (current % 11) + 1 ))

# Switch to next workspace
qtile cmd-obj -o group $next -f toscreen 2>/dev/null || \
qtile cmd-obj -o cmd -f to_group $next 2>/dev/null
