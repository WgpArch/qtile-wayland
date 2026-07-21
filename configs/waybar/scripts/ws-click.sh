#!/bin/bash
# Handle workspace click - $1 is the workspace number
qtile cmd-obj -o group $1 -f toscreen
