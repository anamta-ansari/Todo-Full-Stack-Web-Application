import requests
import json

# Test the signup endpoint
url = "http://127.0.0.1:8000/api/v1/auth/signup"
headers = {
    "Content-Type": "application/json"
}
data = {
    "email": "test@example.com",
    "password": "testpassword"
}

try:
    print("Testing signup endpoint...")
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error occurred: {str(e)}")