# Data Model: Testing Auth Security

## User Model
- **id**: Integer, Primary Key, Auto-increment
- **email**: String(255), Unique, Required, Validated
- **password_hash**: String, Required, Encrypted
- **created_at**: DateTime, Optional, Default: now()
- **updated_at**: DateTime, Optional, Default: now()
- **is_active**: Boolean, Default: True

## JWT Token
- **header**: Object containing algorithm and token type
- **payload**: Object containing user_id, expiration, and other claims
- **signature**: Encrypted signature using BETTER_AUTH_SECRET

## Task Model
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

## Expected Test Results
- User authentication creates valid JWT with user_id
- Unauthorized API requests return 401 status
- Cross-user data access attempts return 403 status
- Session management properly clears on logout
- Protected routes redirect unauthenticated users to login

## Indexes
- User.email: Unique index for fast lookups
- Task.user_id: Index for foreign key lookups and ownership filtering
- Task.complete: Index for filtering completed tasks