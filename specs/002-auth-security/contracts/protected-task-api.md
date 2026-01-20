# API Contract: Protected Task Endpoints

## Get User Tasks Endpoint

### GET /tasks

#### Description
Retrieves all tasks for the authenticated user.

#### Request
- Method: GET
- Path: `/tasks`
- Headers: Authorization: Bearer <token>
- Query Parameters: None
- Request Body: None

#### Response
- Status Code: 200 OK
- Content-Type: application/json

##### Success Response
```json
{
  "tasks": [
    {
      "id": 1,
      "title": "string",
      "description": "string or null",
      "complete": boolean,
      "user_id": integer,
      "created_at": "ISO date string",
      "updated_at": "ISO date string"
    }
  ]
}
```

##### Error Responses
- 401 Unauthorized: Invalid or missing JWT token
```json
{
  "detail": "Not authenticated"
}
```

#### Implementation Notes
- Verify JWT token
- Extract user_id from token
- Filter tasks by user_id
- Return only tasks belonging to authenticated user

## Create Task Endpoint

### POST /tasks

#### Description
Creates a new task for the authenticated user.

#### Request
- Method: POST
- Path: `/tasks`
- Headers: Authorization: Bearer <token>
- Content-Type: application/json
- Request Body:
```json
{
  "title": "string (required)",
  "description": "string or null (optional)",
  "complete": "boolean (optional, default false)"
}
```

#### Response
- Status Code: 201 Created
- Content-Type: application/json

##### Success Response
```json
{
  "id": integer,
  "title": "string",
  "description": "string or null",
  "complete": boolean,
  "user_id": integer,
  "created_at": "ISO date string",
  "updated_at": "ISO date string"
}
```

##### Error Responses
- 401 Unauthorized: Invalid or missing JWT token
```json
{
  "detail": "Not authenticated"
}
```

#### Implementation Notes
- Verify JWT token
- Extract user_id from token
- Set user_id from token (not from request body)
- Create task with authenticated user's ID

## Update Task Endpoint

### PUT /tasks/{task_id}

#### Description
Updates an existing task for the authenticated user.

#### Request
- Method: PUT
- Path: `/tasks/{task_id}`
- Headers: Authorization: Bearer <token>
- Content-Type: application/json
- Request Body:
```json
{
  "title": "string (optional)",
  "description": "string or null (optional)",
  "complete": "boolean (optional)"
}
```

#### Response
- Status Code: 200 OK
- Content-Type: application/json

##### Success Response
```json
{
  "id": integer,
  "title": "string",
  "description": "string or null",
  "complete": boolean,
  "user_id": integer,
  "created_at": "ISO date string",
  "updated_at": "ISO date string"
}
```

##### Error Responses
- 401 Unauthorized: Invalid or missing JWT token
```json
{
  "detail": "Not authenticated"
}
```

- 403 Forbidden: Task does not belong to authenticated user
```json
{
  "detail": "Access denied: Task does not belong to authenticated user"
}
```

- 404 Not Found: Task does not exist
```json
{
  "detail": "Task not found"
}
```

#### Implementation Notes
- Verify JWT token
- Extract user_id from token
- Verify that task belongs to authenticated user
- Update task if ownership is confirmed

## Delete Task Endpoint

### DELETE /tasks/{task_id}

#### Description
Deletes an existing task for the authenticated user.

#### Request
- Method: DELETE
- Path: `/tasks/{task_id}`
- Headers: Authorization: Bearer <token>
- Request Body: None

#### Response
- Status Code: 204 No Content

##### Error Responses
- 401 Unauthorized: Invalid or missing JWT token
```json
{
  "detail": "Not authenticated"
}
```

- 403 Forbidden: Task does not belong to authenticated user
```json
{
  "detail": "Access denied: Task does not belong to authenticated user"
}
```

- 404 Not Found: Task does not exist
```json
{
  "detail": "Task not found"
}
```

#### Implementation Notes
- Verify JWT token
- Extract user_id from token
- Verify that task belongs to authenticated user
- Delete task if ownership is confirmed