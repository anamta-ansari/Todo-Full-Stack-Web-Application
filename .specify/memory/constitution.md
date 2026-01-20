<!-- SYNC IMPACT REPORT
Version change: 2.0.0 -> 3.0.0
Modified principles: Principles I-VII updated to reflect Part 3 requirements
Added sections: Principle VIII (Dashboard & CRUD Standards), Frontend Architecture Standards update
Removed sections: None
Templates requiring updates:
- ✅ .specify/templates/plan-template.md - Updated to reflect new principles
- ✅ .specify/templates/spec-template.md - Updated to reflect new principles
- ✅ .specify/templates/tasks-template.md - Updated to reflect new principles
- ✅ .specify/templates/commands/*.md - Verified no outdated references
Follow-up TODOs: None
-->

# Todo Full-Stack Web Application Constitution

## Core Principles

### I. Scope of Part 3
Dashboard & CRUD-focused development: Implement protected dashboard UI with full CRUD operations; Frontend adds task management interface with add/view/update/delete/complete functionality; Backend enforces user isolation in API endpoints; UI must be responsive, beautiful, and modern with proper user experience.

### II. Technology Stack for Part 3
Frontend: Next.js 16+ (App Router) with Tailwind CSS for styling; Backend: Python FastAPI + SQLModel (from Part 1) with JWT verification (from Part 2); Authentication: Better Auth + JWT (from Part 2) for secure API calls; Shared secret: BETTER_AUTH_SECRET (environment variable).

### III. Project Structure (Post Part 3)
Monorepo organization with dedicated backend/ and frontend/ directories; Frontend uses App Router with protected routes including dashboard; Clear separation of concerns between frontend and backend codebases; Standardized specs/ directory for documentation and planning artifacts; Dashboard UI accessible at /dashboard route after authentication.

### IV. Deliverables for Part 3 (NON-NEGOTIABLE)
Working dashboard UI with task management functionality; All 5 CRUD operations (Add, View, Update, Delete, Mark Complete); User isolation enforced in both frontend and backend; Responsive and aesthetically pleasing UI with modern design elements; Proper authentication state management throughout the application.

### V. Test-First Approach
TDD mandatory: Tests written → Requirements validated → Tests fail → Then implement; Red-Green-Refactor cycle strictly enforced for all dashboard and CRUD functionality.

### VI. Documentation and Clarity
All code must include appropriate docstrings; README updated with dashboard and CRUD setup and run instructions; Architecture decisions documented in specs/ directory.

### VII. Security & User Isolation Standards
- Dashboard protected: redirect to /login if not authenticated
- Backend enforces ownership: all operations filtered by authenticated user_id
- Frontend never displays tasks from other users
- All API calls must include Authorization: Bearer <token>
- Prevent cross-user data access: unauthorized requests return 401, ownership mismatches return 403
- Frontend properly handles authentication state and redirects to login when unauthenticated

### VIII. Dashboard & CRUD Standards
- After login, redirect to /dashboard
- Dashboard shows only current user's tasks (GET /api/v1/tasks)
- Add task → POST /api/v1/tasks
- Edit task → PUT /api/v1/tasks/{id}
- Delete task → DELETE /api/v1/tasks/{id}
- Toggle complete → PUT /api/v1/tasks/{id} (with complete field)
- UI must be responsive, beautiful, modern (cards, hover effects, intuitive UX)
- Error handling with user-friendly messages
- Loading states for better user experience

## Frontend Architecture Standards
- Use Next.js App Router with proper route protection
- Implement consistent authentication state management
- Follow accessibility best practices for all UI components
- Ensure responsive design for all pages and components
- Handle authentication errors gracefully with user-friendly messages
- Implement proper loading states and error boundaries
- Use Tailwind CSS for consistent styling and modern UI components
- Organize components logically (TaskList, AddTaskForm, EditModal, etc.)

## Backend Architecture Standards
- Follow FastAPI best practices for API design
- Use SQLModel for consistent database modeling
- Implement proper error handling and validation
- Follow security best practices for API endpoints including JWT verification
- Ensure database connection pooling and optimization
- Enforce user isolation in all data access operations
- Maintain consistent API endpoint patterns for CRUD operations

## Development Workflow
- All changes must follow the spec-plan-tasks implementation cycle
- Code reviews required for all pull requests
- Automated testing required before merge
- Clear commit messages following conventional format
- Branch naming convention: feature/[issue-number]-[short-description]

## Governance
This constitution governs Part 3 of Phase II development: implementing the protected Todo dashboard UI and full CRUD integration with user isolation. All development activities must comply with these principles. Amendments require explicit documentation and team approval.

**Version**: 3.0.0 | **Ratified**: 2026-01-13 | **Last Amended**: 2026-01-14