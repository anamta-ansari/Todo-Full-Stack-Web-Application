import uvicorn
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath('.'))

if __name__ == "__main__":
    uvicorn.run(
        "backend.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="debug"
    )