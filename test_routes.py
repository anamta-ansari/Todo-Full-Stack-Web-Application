"""
Test script to check the API routes and debug the 404 error
"""

import requests
import json

# Configuration
BASE_URL = "http://localhost:8000"

def check_routes():
    print("Checking API routes...")
    
    # Check if the base API is accessible
    print("\n1. Checking base API...")
    response = requests.get(f"{BASE_URL}/")
    print(f"GET / -> Status: {response.status_code}")
    
    # Check if the docs are accessible (which means the API is running)
    print("\n2. Checking API docs...")
    response = requests.get(f"{BASE_URL}/docs")
    print(f"GET /docs -> Status: {response.status_code}")
    
    # Check the openapi.json to see the actual routes
    print("\n3. Checking OpenAPI spec...")
    response = requests.get(f"{BASE_URL}/openapi.json")
    print(f"GET /openapi.json -> Status: {response.status_code}")
    
    if response.status_code == 200:
        api_spec = response.json()
        paths = list(api_spec.get('paths', {}).keys())
        print(f"Available paths ({len(paths)}):")
        for path in sorted(paths)[:10]:  # Show first 10 paths
            print(f"  - {path}")
        if len(paths) > 10:
            print(f"  ... and {len(paths)-10} more")
    
    # Try to register a test user to get a valid token
    print("\n4. Creating a test user...")
    register_response = requests.post(
        f"{BASE_URL}/api/v1/auth/signup",
        headers={"Content-Type": "application/json"},
        json={
            "email": "test_user_404@example.com",
            "password": "password123",
            "name": "Test User 404"
        }
    )
    
    if register_response.status_code in [200, 201]:
        print("Test user created successfully or already exists")
        response_json = register_response.json()
        token = response_json.get("access_token")
        user_id = response_json.get("user", {}).get("id")
    else:
        print(f"Registration failed: {register_response.status_code} - {register_response.text}")
        return
    
    print(f"Using user ID: {user_id}")
    
    # Test the specific route that's failing
    print(f"\n5. Testing GET /api/v1/users/{user_id}/tasks with authentication...")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    
    response = requests.get(
        f"{BASE_URL}/api/v1/users/{user_id}/tasks",
        headers=headers
    )
    print(f"GET /api/v1/users/{user_id}/tasks -> Status: {response.status_code}")
    if response.status_code != 200:
        print(f"Response: {response.text}")
    
    # Test with query parameters that the dashboard uses
    print(f"\n6. Testing with query parameters...")
    response = requests.get(
        f"{BASE_URL}/api/v1/users/{user_id}/tasks",
        headers=headers,
        params={
            "priority": "all",
            "status": "all", 
            "category": "all",
            "search": "",
            "sort_by": "created_at"
        }
    )
    print(f"GET /api/v1/users/{user_id}/tasks with params -> Status: {response.status_code}")
    if response.status_code != 200:
        print(f"Response: {response.text}")
    
    print("\nRoute check completed!")

if __name__ == "__main__":
    check_routes()