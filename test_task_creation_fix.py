"""
Test script to verify the task creation fix
"""

import requests
import json

# Configuration
BASE_URL = "http://localhost:8000"
HEADERS = {"Content-Type": "application/json"}

def test_task_creation_fix():
    print("Testing task creation fix...")
    
    # Try to create a task with all the new fields
    print("\n1. Testing task creation with priority and category...")
    
    # First, let's try to register a test user
    print("\n2. Creating a test user...")
    register_response = requests.post(
        f"{BASE_URL}/api/v1/auth/signup",
        headers=HEADERS,
        json={
            "email": "test_user@example.com",
            "password": "password123",
            "name": "Test User"
        }
    )
    
    if register_response.status_code == 200:
        print("Test user created successfully")
        user_data = register_response.json()
        token = user_data.get("access_token")
        user_id = user_data.get("user", {}).get("id")
    elif register_response.status_code == 400 and "already registered" in register_response.text:
        print("Test user already exists, signing in...")
        # Sign in to get token
        signin_response = requests.post(
            f"{BASE_URL}/api/v1/auth/signin",
            headers=HEADERS,
            json={
                "email": "test_user@example.com",
                "password": "password123"
            }
        )
        
        if signin_response.status_code == 200:
            token = signin_response.json().get("access_token")
            # Get user ID
            user_response = requests.get(
                f"{BASE_URL}/api/v1/users/me",
                headers={"Authorization": f"Bearer {token}"}
            )
            user_id = user_response.json().get("id")
        else:
            print(f"Sign in failed: {signin_response.status_code} - {signin_response.text}")
            return
    else:
        print(f"Registration failed: {register_response.status_code} - {register_response.text}")
        return
    
    HEADERS["Authorization"] = f"Bearer {token}"
    
    print(f"Using user ID: {user_id}")
    
    # Now test creating a task with all fields
    test_task = {
        "title": "Test task with priority and category",
        "description": "This is a test task to verify the fix",
        "complete": False,
        "priority": "high",
        "category": "Work",
        "due_date": None
    }
    
    response = requests.post(
        f"{BASE_URL}/api/v1/users/{user_id}/tasks",
        headers=HEADERS,
        json=test_task
    )
    
    if response.status_code == 201:
        task_data = response.json()
        print(f"✓ Successfully created task with ID: {task_data['id']}")
        print(f"  Title: {task_data['title']}")
        print(f"  Priority: {task_data['priority']}")
        print(f"  Category: {task_data['category']}")
        
        # Clean up - delete the test task
        delete_response = requests.delete(
            f"{BASE_URL}/api/v1/users/{user_id}/tasks/{task_data['id']}",
            headers=HEADERS
        )
        if delete_response.status_code == 204:
            print(f"✓ Cleaned up test task {task_data['id']}")
        else:
            print(f"⚠ Could not clean up test task: {delete_response.status_code}")
    else:
        print(f"✗ Failed to create task: {response.status_code} - {response.text}")
    
    # Also test creating a task with minimal fields
    print("\n3. Testing task creation with minimal fields...")
    minimal_task = {
        "title": "Minimal test task",
        "description": "Task with minimal fields",
        "complete": False
    }
    
    response = requests.post(
        f"{BASE_URL}/api/v1/users/{user_id}/tasks",
        headers=HEADERS,
        json=minimal_task
    )
    
    if response.status_code == 201:
        task_data = response.json()
        print(f"✓ Successfully created minimal task with ID: {task_data['id']}")
        print(f"  Title: {task_data['title']}")
        print(f"  Priority (should be default): {task_data['priority']}")
        print(f"  Category (should be null): {task_data['category']}")
        
        # Clean up - delete the test task
        delete_response = requests.delete(
            f"{BASE_URL}/api/v1/users/{user_id}/tasks/{task_data['id']}",
            headers=HEADERS
        )
        if delete_response.status_code == 204:
            print(f"✓ Cleaned up minimal test task {task_data['id']}")
        else:
            print(f"⚠ Could not clean up test task: {delete_response.status_code}")
    else:
        print(f"✗ Failed to create minimal task: {response.status_code} - {response.text}")
    
    print("\nTask creation fix test completed!")

if __name__ == "__main__":
    test_task_creation_fix()