# API Contract: Authentication Endpoints

## Health Check Endpoint

### GET /health

#### Description
Returns the health status of the backend server.

#### Request
- Method: GET
- Path: `/health`
- Headers: None required

#### Response
- Status Code: 200 OK
- Content-Type: application/json

##### Success Response
```json
{
  "status": "healthy",
  "timestamp": "ISO date string"
}
```

##### Error Responses
- 500 Internal Server Error: Server is not healthy
```json
{
  "status": "unhealthy",
  "error": "string"
}
```

#### Implementation Notes
- Verify database connection
- Check system resources if applicable

## Signup Endpoint

### POST /api/v1/auth/signup

#### Description
Creates a new user account and issues a JWT token.

#### Request
- Method: POST
- Path: `/api/v1/auth/signup`
- Content-Type: application/json
- Headers: None required
- Request Body:
```json
{
  "email": "string (valid email format)",
  "password": "string (minimum 8 characters)"
}
```

#### Response
- Status Code: 200 OK
- Content-Type: application/json

##### Success Response
```json
{
  "access_token": "JWT token string",
  "token_type": "bearer",
  "user_id": integer,
  "email": "string"
}
```

##### Error Responses
- 400 Bad Request: Invalid input data
```json
{
  "detail": "string"
}
```

- 409 Conflict: Email already exists
```json
{
  "detail": "Email already registered"
}
```

#### Implementation Notes
- Hash the password before storing
- Issue JWT token containing user_id
- Store user in Neon DB

## Signin Endpoint

### POST /api/v1/auth/signin

#### Description
Authenticates a user and issues a JWT token.

#### Request
- Method: POST
- Path: `/api/v1/auth/signin`
- Content-Type: application/json
- Headers: None required
- Request Body:
```json
{
  "email": "string (valid email format)",
  "password": "string"
}
```

#### Response
- Status Code: 200 OK
- Content-Type: application/json

##### Success Response
```json
{
  "access_token": "JWT token string",
  "token_type": "bearer",
  "user_id": integer,
  "email": "string"
}
```

##### Error Responses
- 400 Bad Request: Missing email or password
```json
{
  "detail": "string"
}
```

- 401 Unauthorized: Invalid credentials
```json
{
  "detail": "Invalid email or password"
}
```

#### Implementation Notes
- Verify password hash
- Issue JWT token containing user_id

## Logout Endpoint

### POST /api/v1/auth/logout

#### Description
Logs out the user and invalidates the JWT token.

#### Request
- Method: POST
- Path: `/api/v1/auth/logout`
- Headers: Authorization: Bearer <token>
- Request Body: None

#### Response
- Status Code: 200 OK
- Content-Type: application/json

##### Success Response
```json
{
  "message": "Logged out successfully"
}
```

#### Implementation Notes
- Clear the JWT token from the client
- Optionally maintain a blacklist of invalidated tokens