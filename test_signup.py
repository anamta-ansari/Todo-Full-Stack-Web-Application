import requests
import json

# Test the signup endpoint
url = "http://localhost:8000/api/v1/auth/signup"
headers = {"Content-Type": "application/json"}
data = {
    "email": "test@example.com",
    "password": "password123"
}

try:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")