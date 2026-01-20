# Todo Full-Stack Web Application

This is a full-stack todo application with a Next.js frontend and FastAPI backend featuring beautiful UI, complete CRUD functionality, and robust authentication.

## Project Structure

- `frontend/` - Next.js 16 application
- `backend/` - FastAPI server
- `specs/` - Feature specifications and plans

## Authentication & API Security

This application implements authentication and API security using Better Auth with JWT tokens.

### Setup Instructions

1. Copy the `.env.example` file to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Generate a strong secret for `BETTER_AUTH_SECRET` in the `.env` file:
   ```bash
   # Use a strong random secret (at least 32 characters)
   BETTER_AUTH_SECRET=your-super-secret-jwt-key-here-make-it-long-and-random
   ```

3. Set the API base URL in the `.env` file:
   ```bash
   NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
   ```

### Authentication Flow

1. **Homepage**: Visit the public landing page at `http://localhost:3000` with project details and sign in/up buttons
2. **Signup**: Navigate to `/signup` to create a new account
3. **Signin**: Navigate to `/signin` to log in with existing credentials
4. **Protected Routes**: Access to `/dashboard` and other protected routes requires authentication
5. **API Calls**: All API calls to protected endpoints require a valid JWT token in the Authorization header
6. **Logout**: Click the logout button to securely end your session

### Security Features

- JWT tokens are issued upon successful authentication
- Protected routes are restricted to authenticated users only
- API endpoints verify JWT tokens and enforce user isolation
- Users can only access their own data
- Secure password hashing using bcrypt

## Backend Setup

1. Navigate to the project root:
   ```bash
   cd todo-full-stack
   ```

2. Create and activate a virtual environment:
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
   # Edit .env and add your DATABASE_URL and BETTER_AUTH_SECRET
   ```

5. Run the backend server:
   ```bash
   uvicorn backend.main:app --reload
   ```

The server will be available at `http://localhost:8000`.

## Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the development server:
   ```bash
   npm run dev
   ```

The frontend will be available at `http://localhost:3000`.

## API Endpoints

- Health Check: `GET http://localhost:8000/health`
- Auth Signup: `POST http://localhost:8000/api/v1/auth/register`
- Auth Signin: `POST http://localhost:8000/api/v1/auth/login`
- Auth Logout: Handled on frontend by clearing JWT token
- Tasks: `GET/POST/PUT/DELETE http://localhost:8000/api/v1/tasks` (requires authentication)

## Database

The application uses Neon Serverless PostgreSQL. The database tables will be created automatically on startup.

## Running the Application

1. Start the backend server from the root directory:
   ```bash
   uvicorn backend.main:app --reload
   ```

2. In a separate terminal, start the frontend from the frontend directory:
   ```bash
   cd frontend
   npm run dev
   ```

The backend will start on `http://127.0.0.1:8000` and the frontend will be available at `http://localhost:3000`.

## Application Flow

1. Visit the homepage at `http://localhost:3000` - public landing page with project details and sign in/up buttons
2. Click on the "Sign Up" button to create a new account at `/signup`
3. Fill in your email and password, then submit
4. After successful signup, you'll be redirected to the sign in page at `/signin`
5. Sign in with your credentials to access the protected dashboard at `/dashboard`
6. On the dashboard, you can:
   - View your existing tasks in a responsive card-based layout
   - Add new tasks using the form in the sidebar
   - Edit existing tasks by clicking the edit icon
   - Mark tasks as complete/incomplete using the checkbox
   - Delete tasks using the delete icon
   - View statistics about your tasks
7. Use the logout button in the header to securely end your session

## Dashboard Features

- **Beautiful UI**: Modern design with gradients, cards, hover effects, and smooth animations
- **Responsive Layout**: Works seamlessly across mobile, tablet, and desktop devices
- **Real-time Updates**: Changes to tasks are reflected immediately in the UI
- **Loading States**: Visual feedback during API operations
- **Error Handling**: User-friendly error messages for failed operations
- **Statistics Panel**: Shows total tasks, completed tasks, and pending tasks

## User Isolation

The application enforces strict user isolation - each user can only see and modify their own tasks. When a second user logs in, they will only see their own tasks, not tasks created by other users. This is enforced both at the frontend and backend levels.

## Testing

To run the full flow test:
```bash
python test_full_flow.py
```

This test script verifies the complete flow: signup → signin → dashboard → CRUD operations → logout → new user login (with empty list).