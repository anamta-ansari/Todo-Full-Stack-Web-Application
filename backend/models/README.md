# Models Documentation

This directory contains the SQLModel definitions for the application.

## User Model
- **id**: Integer, Primary Key, Auto-increment
- **email**: String(255), Unique, Required, Validated
- **created_at**: DateTime, Optional, Default: now()
- **updated_at**: DateTime, Optional, Default: now()
- **tasks**: Relationship to Task objects

## Task Model
- **id**: Integer, Primary Key, Auto-increment
- **title**: String(255), Required, Validated (max 255 chars)
- **description**: Text, Optional
- **complete**: Boolean, Default: False
- **user_id**: Integer, Foreign Key to User.id, Required
- **created_at**: DateTime, Optional, Default: now()
- **updated_at**: DateTime, Optional, Default: now()
- **user**: Relationship to User object

## Relationships
- User has many Tasks (one-to-many)
- Task belongs to one User

## Validation
- User.email must be a valid email format
- Task.title must not exceed 255 characters