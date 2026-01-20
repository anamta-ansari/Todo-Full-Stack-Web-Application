# Data Model: Dashboard & Full CRUD Integration

## User Entity
- **id**: Integer, Primary Key, Auto-increment
- **email**: String(255), Unique, Required, Validated
- **password_hash**: String, Required, Encrypted
- **created_at**: DateTime, Optional, Default: now()
- **updated_at**: DateTime, Optional, Default: now()
- **is_active**: Boolean, Default: True

## Task Entity
- **id**: Integer, Primary Key, Auto-increment
- **title**: String(255), Required, Validated (max 255 chars)
- **description**: Text, Optional
- **complete**: Boolean, Default: False
- **user_id**: Integer, Foreign Key to User.id, Required
- **created_at**: DateTime, Optional, Default: now()
- **updated_at**: DateTime, Optional, Default: now()

## Relationships
- User has many Tasks (one-to-many)
- Task belongs to one User
- JWT Token contains user_id reference to User

## Validation Rules
- User.email must be a valid email format
- User.password must meet security requirements (min 8 chars)
- Task.title must not exceed 255 characters
- Task.user_id must reference an existing User
- All Task operations must be filtered by authenticated user_id

## Expected Behavior in Dashboard
- Only tasks belonging to the authenticated user are displayed
- Users can create new tasks with title (required) and description (optional)
- Users can update task details (title, description, completion status)
- Users can delete their own tasks
- Users cannot access or modify other users' tasks
- Task completion status can be toggled independently

## Indexes
- User.email: Unique index for fast lookups
- Task.user_id: Index for foreign key lookups and ownership filtering
- Task.complete: Index for filtering completed tasks