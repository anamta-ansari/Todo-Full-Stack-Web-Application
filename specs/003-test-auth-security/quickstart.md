# Quickstart Guide: Testing Auth Security

## Prerequisites
- Python 3.11+
- Node.js 18+ and npm/yarn/pnpm
- Access to Neon Serverless PostgreSQL instance
- Better Auth account or self-hosted instance
- Valid BETTER_AUTH_SECRET

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
   # Edit .env and add your DATABASE_URL and BETTER_AUTH_SECRET
   ```

## Testing Instructions

### 1. Backend Health & DB Connection Test
1. Start the backend server:
   ```bash
   uvicorn backend.main:app --reload
   ```
2. Verify the server starts without errors
3. Navigate to `http://localhost:8000/health` to confirm 200 OK response
4. Verify Neon DB connection works during startup

### 2. Authentication Flow Test
1. Navigate to `/signup` to create a new account
2. Use a valid email and password (at least 8 characters)
3. Verify successful signup and JWT token issuance
4. Navigate to `/signin` to log in with the created credentials
5. Verify successful signin and JWT token issuance

### 3. Security & Isolation Test
1. Make an API call to a protected endpoint without a JWT token
2. Verify the response is 401 Unauthorized
3. Create two different user accounts
4. Log in as the first user and create some tasks
5. Log out and log in as the second user
6. Attempt to access the first user's tasks via API
7. Verify the response is 403 Forbidden

### 4. Frontend Route Protection Test
1. Navigate directly to `/dashboard` without being logged in
2. Verify that you're redirected to the login page
3. Log in and verify you can access `/dashboard`
4. Log out and verify you're redirected to the login page

### 5. Logout Test
1. Click the logout button on the dashboard
2. Verify that the JWT token is removed from localStorage
3. Try to access `/dashboard` and verify you're redirected to `/signin`

## API Endpoints for Testing

- Health Check: `GET http://localhost:8000/health`
- Auth Signup: `POST http://localhost:8000/api/v1/auth/signup`
- Auth Signin: `POST http://localhost:8000/api/v1/auth/signin`
- Auth Logout: `POST http://localhost:8000/api/v1/auth/logout`
- Tasks: `GET/POST/PUT/DELETE http://localhost:8000/api/v1/tasks/*` (requires authentication)

## Expected Test Results

- All 10 critical tests pass without failures
- No 500 errors occur during testing
- User isolation is verified through 403 test
- System is confirmed ready for Part 3 (dashboard + CRUD)

## Troubleshooting

- If authentication fails, verify your BETTER_AUTH_SECRET is consistent between frontend and backend
- If protected routes don't work, ensure JWT tokens are being properly attached to requests
- Check that the database connection is working and user records exist
- Verify that the middleware is properly protecting routes