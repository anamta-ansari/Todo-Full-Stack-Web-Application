# Quickstart Guide: Authentication & API Security

## Prerequisites
- Python 3.11+
- Node.js 18+ and npm/yarn/pnpm
- Access to Neon Serverless PostgreSQL instance
- Better Auth account or self-hosted instance

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Set up the backend:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Set up the frontend:
   ```bash
   cd frontend
   npm install  # or yarn install or pnpm install
   ```

4. Configure environment variables:
   ```bash
   # In root directory
   cp .env.example .env
   # Edit .env and add your BETTER_AUTH_SECRET and DATABASE_URL
   ```

5. Run the backend server:
   ```bash
   # From project root
   uvicorn backend.main:app --reload
   ```

6. Run the frontend development server:
   ```bash
   # From frontend directory
   npm run dev  # or yarn dev or pnpm dev
   ```

## Authentication Flow

1. Navigate to `/signup` to create a new account
2. Use your email and password to register
3. After successful signup, you'll be redirected to the dashboard
4. Alternatively, navigate to `/signin` to log in with existing credentials
5. Use the logout button to securely end your session

## API Endpoints

- Signup: `POST /auth/signup`
- Signin: `POST /auth/signin`
- Health Check: `GET /health`
- Protected Dashboard: `GET /dashboard` (requires authentication)

## Troubleshooting

- If authentication fails, verify your BETTER_AUTH_SECRET is consistent between frontend and backend
- If protected routes don't work, ensure JWT tokens are being properly attached to requests
- Check that the database connection is working and user records exist