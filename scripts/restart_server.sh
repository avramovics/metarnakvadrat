#!/bin/bash
# Restart the application server

# Define the command to run the server
COMMAND="uvicorn main:app --host 0.0.0.0 --port 8000"

# Function to start the server
start_server() {
    cd ~
    cd myapp
    uvicorn main:app --host 0.0.0.0 --port 8000
    echo "Server started successfully."
}

# Check if the server is running
if pgrep -f "$COMMAND" > /dev/null
then
    echo "Server is running. Restarting server..."
    pkill -f "$COMMAND"
    sleep 2
    start_server
else
    echo "Server is not running. Starting server..."
fi