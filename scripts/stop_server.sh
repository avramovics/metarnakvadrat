#!/bin/bash
# Stop the application server

COMMAND="uvicorn main:app --host 0.0.0.0 --port 8000"

if pgrep -f "$COMMAND" > /dev/null; then
    echo "Stopping server..."
    cd ~
    cd myapp
    pkill -f "$COMMAND"
    echo "Server stopped successfully."
else
    echo "Server is not running."
fi