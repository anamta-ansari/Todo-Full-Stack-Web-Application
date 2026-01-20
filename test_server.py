import sys
import os
import threading
import time
import requests

# Add the project root to the path
sys.path.insert(0, os.path.abspath('.'))

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

print("Starting server...")

# Import and run the app
from backend.main import app
import uvicorn

def run_server():
    uvicorn.run(app, host='127.0.0.1', port=8001, log_level="debug")

# Start server in a thread
server_thread = threading.Thread(target=run_server)
server_thread.daemon = True
server_thread.start()

print("Server started in background thread")
print("Waiting for server to be ready...")

# Wait a bit for the server to start
time.sleep(3)

# Test the server
try:
    response = requests.get("http://127.0.0.1:8001/")
    print(f"Server responded: {response.status_code} - {response.json()}")
except Exception as e:
    print(f"Error connecting to server: {e}")

# Keep the main thread alive
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Shutting down...")