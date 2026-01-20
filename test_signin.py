import time
import requests
import json

time.sleep(2)  # Wait for server to be ready

# Test the signin endpoint with the same credentials
url = "http://127.0.0.1:8000/api/v1/auth/signin"
headers = {
    "Content-Type": "application/json"
}
data = {
    "email": "test@example.com",
    "password": "testpassword"
}

try:
    print("Testing signin endpoint...")
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error occurred: {str(e)}")