# Quickstart Guide: Backend Foundation

## Prerequisites
- Python 3.11+
- pip package manager
- Access to Neon Serverless PostgreSQL instance

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env and add your DATABASE_URL
   ```

5. Run the backend server:
   ```bash
   uvicorn backend.main:app --reload
   ```

## API Endpoints

- Health Check: `GET http://localhost:8000/health`
  - Response: `{"status": "ok"}`

## Database Setup

The application will automatically create the required tables (users, tasks) on startup if they don't exist.

## Troubleshooting

- If you get a database connection error, verify your `DATABASE_URL` is correct
- If the server won't start, ensure all dependencies are installed
- Check that port 8000 is available