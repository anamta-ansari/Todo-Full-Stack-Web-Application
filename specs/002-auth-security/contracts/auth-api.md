# API Contract: Authentication Endpoints

## Signup Endpoint

### POST /auth/signup

#### Description
Creates a new user account and issues a JWT token.

#### Request
- Method: POST
- Path: `/auth/signup`
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
- Status Code: 201 Created
- Content-Type: application/json

##### Success Response
```json
{
  "status": "success",
  "message": "User created successfully",
  "token": "JWT token string"
}
```

##### Error Responses
- 400 Bad Request: Invalid input data
```json
{
  "status": "error",
  "message": "Invalid email format or password too short"
}
```

- 409 Conflict: Email already exists
```json
{
  "status": "error",
  "message": "Email already registered"
}
```

#### Implementation Notes
- Hash the password before storing
- Issue JWT token containing user_id
- Store user in Neon DB

## Signin Endpoint

### POST /auth/signin

#### Description
Authenticates a user and issues a JWT token.

#### Request
- Method: POST
- Path: `/auth/signin`
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
  "status": "success",
  "message": "Signin successful",
  "token": "JWT token string"
}
```

##### Error Responses
- 400 Bad Request: Missing email or password
```json
{
  "status": "error",
  "message": "Email and password are required"
}
```

- 401 Unauthorized: Invalid credentials
```json
{
  "status": "error",
  "message": "Invalid email or password"
}
```

#### Implementation Notes
- Verify password hash
- Issue JWT token containing user_id

## Logout Endpoint

### POST /auth/logout

#### Description
Logs out the user and invalidates the JWT token.

#### Request
- Method: POST
- Path: `/auth/logout`
- Headers: Authorization: Bearer <token>
- Request Body: None

#### Response
- Status Code: 200 OK
- Content-Type: application/json

##### Success Response
```json
{
  "status": "success",
  "message": "Logout successful"
}
```

#### Implementation Notes
- Clear the JWT token from the client
- Optionally maintain a blacklist of invalidated tokens