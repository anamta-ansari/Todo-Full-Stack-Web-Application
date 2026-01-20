# Quickstart Guide: Dashboard & Full CRUD Integration

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

## Implementation Instructions

### 1. Dashboard Page Implementation
1. Create the dashboard page at `frontend/app/dashboard/page.tsx`
2. Protect the route using Next.js middleware or authentication guards
3. Fetch user's tasks using the authenticated API call to GET /api/v1/tasks
4. Implement loading states while fetching data
5. Display tasks in a responsive, card-based layout

### 2. Task List Component
1. Create a reusable TaskList component in `frontend/components/dashboard/task-list.tsx`
2. Display each task with title, description, and completion status
3. Implement visual indicators for completed tasks
4. Add loading and empty state handling

### 3. Add Task Form
1. Create an AddTaskForm component in `frontend/components/dashboard/add-task-form.tsx`
2. Include fields for title (required) and description (optional)
3. Implement form validation
4. Handle submission with POST /api/v1/tasks API call
5. Add success/error feedback

### 4. Edit Task Functionality
1. Create an EditTaskModal component in `frontend/components/dashboard/edit-task-modal.tsx`
2. Pre-populate form with existing task data
3. Handle submission with PUT /api/v1/tasks/{id} API call
4. Add success/error feedback

### 5. Delete Task Functionality
1. Add delete buttons to each task item
2. Implement confirmation dialog for deletion
3. Handle deletion with DELETE /api/v1/tasks/{id} API call
4. Add success/error feedback

### 6. Toggle Complete Functionality
1. Add toggle switches/buttons to each task item
2. Handle completion updates with PUT /api/v1/tasks/{id} API call
3. Update UI immediately upon successful toggle
4. Add success/error feedback

### 7. Logout Integration
1. Add logout button to the dashboard
2. Integrate with existing signOut() function
3. Redirect to login page after logout

## API Endpoints for Implementation

- Get Tasks: `GET http://localhost:8000/api/v1/tasks` (requires authentication)
- Add Task: `POST http://localhost:8000/api/v1/tasks` (requires authentication)
- Update Task: `PUT http://localhost:8000/api/v1/tasks/{id}` (requires authentication)
- Delete Task: `DELETE http://localhost:8000/api/v1/tasks/{id}` (requires authentication)

## Expected Implementation Results

- Dashboard page is protected and redirects unauthenticated users to login
- Task list displays only the current user's tasks
- All 5 CRUD operations work correctly (Add, View, Update, Delete, Mark Complete)
- User isolation is maintained (users cannot access other users' tasks)
- UI is responsive and visually appealing with Tailwind CSS
- Loading states and error/success feedback are implemented
- Logout functionality works correctly

## Testing Instructions

1. Start the backend server:
   ```bash
   uvicorn backend.main:app --reload
   ```

2. Start the frontend development server:
   ```bash
   npm run dev
   ```

3. Test the full CRUD flow:
   - Login to the application
   - Navigate to the dashboard
   - Add a new task
   - Edit an existing task
   - Toggle task completion status
   - Delete a task
   - Logout and verify redirect to login

4. Test user isolation:
   - Create two different user accounts
   - Log in as the first user and create some tasks
   - Log out and log in as the second user
   - Verify that the second user cannot see the first user's tasks

## Troubleshooting

- If dashboard is not protected, verify your authentication middleware is properly configured
- If tasks are not displaying, check that the API call to GET /api/v1/tasks is properly authenticated
- If user isolation is not working, verify that the backend is filtering tasks by user_id
- If API calls are failing, verify that JWT tokens are being properly attached to requests