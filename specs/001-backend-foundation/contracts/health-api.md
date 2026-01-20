# API Contract: Backend Foundation

## Health Check Endpoint

### GET /health

#### Description
Returns the health status of the backend service.

#### Request
- Method: GET
- Path: `/health`
- Headers: None required
- Query Parameters: None
- Request Body: None

#### Response
- Status Code: 200 OK
- Content-Type: application/json

##### Success Response
```json
{
  "status": "ok"
}
```

#### Error Responses
- 503 Service Unavailable: If the database connection is down
```json
{
  "status": "error",
  "message": "Database connection failed"
}
```

#### Implementation Notes
- This endpoint should be accessible without authentication
- Should return quickly (under 100ms)
- Can be used for load balancer health checks