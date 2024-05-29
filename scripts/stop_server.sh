#!/bin/bash
# Stop the application server

# Define the command to identify the server process
COMMAND="uvicorn main:app --host 0.0.0.0 --port 8000"

# Function to stop the server
stop_server() {
    echo "Stopping server..."
    pkill -f "$COMMAND"
    echo "Server stopped successfully."
}

# Check if the server is running
if pgrep -f "$COMMAND" > /dev/null
then
    stop_server
else
    echo "Server is not running."
fi