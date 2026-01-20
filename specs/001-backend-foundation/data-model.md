# Data Model: Backend Foundation

## User Model
- **id**: Integer, Primary Key, Auto-increment
- **email**: String(255), Unique, Required
- **created_at**: DateTime, Optional, Default: now()
- **updated_at**: DateTime, Optional, Default: now()

## Task Model
- **id**: Integer, Primary Key, Auto-increment
- **title**: String(255), Required
- **description**: Text, Optional
- **complete**: Boolean, Default: False
- **user_id**: Integer, Foreign Key to User.id, Required
- **created_at**: DateTime, Optional, Default: now()
- **updated_at**: DateTime, Optional, Default: now()

## Relationships
- User has many Tasks (one-to-many)
- Task belongs to one User

## Validation Rules
- User.email must be a valid email format
- Task.title must not exceed 255 characters
- Task.user_id must reference an existing User

## Indexes
- User.email: Unique index for fast lookups
- Task.user_id: Index for foreign key lookups
- Task.complete: Index for filtering completed tasks