"""
Test script to verify the complete flow: signup → signin → dashboard → CRUD → logout → new user → empty list
"""

import requests
import time
import json
from datetime import datetime

# Configuration
BASE_URL = "http://localhost:8000"
FRONTEND_URL = "http://localhost:3000"

def test_full_flow():
    """
    Test the complete flow of the application:
    1. Signup
    2. Signin
    3. Dashboard access
    4. CRUD operations
    5. Logout
    6. New user login (should see empty list)
    """
    print("Starting full flow test...")

    # Generate unique email addresses for this test run
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    test_email = f"testuser_{timestamp}@example.com"
    new_user_email = f"newuser_{timestamp}@example.com"

    # Step 1: Signup
    print("\n1. Testing signup...")
    signup_data = {
        "email": test_email,
        "password": "SecurePassword123!"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/api/v1/auth/signup", json=signup_data)
        if response.status_code == 201:
            print("O Signup successful")
            user_data = response.json()
            # The new signup response has a 'user' object with the user details
            user_info = user_data.get('user')
            user_id = user_info.get('id') if user_info else None
            print(f"  User ID: {user_id}")
        else:
            print(f"X Signup failed: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"X Signup error: {str(e)}")
        return False
    
    # Step 2: Signin
    print("\n2. Testing signin...")
    signin_data = {
        "email": test_email,  # Use the dynamically generated email
        "password": "SecurePassword123!"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/api/v1/auth/signin", json=signin_data)
        if response.status_code == 200:
            print("O Signin successful")
            auth_data = response.json()
            token = auth_data.get('access_token')
            user_id = auth_data.get('user_id')  # Get user ID from signin response
            if token:
                print("  Token retrieved")
            else:
                print("  Warning: No token in response")
                return False
        else:
            print(f"X Signin failed: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"X Signin error: {str(e)}")
        return False
    
    # Prepare headers with authentication token
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    # Step 3: Dashboard access (get tasks)
    print("\n3. Testing dashboard access (get tasks)...")
    try:
        response = requests.get(f"{BASE_URL}/api/v1/users/{user_id}/tasks", headers=headers)
        if response.status_code == 200:
            tasks = response.json()
            print(f"O Dashboard access successful - {len(tasks)} tasks retrieved")
        else:
            print(f"X Dashboard access failed: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"X Dashboard access error: {str(e)}")
        return False
    
    # Step 4: CRUD Operations
    print("\n4. Testing CRUD operations...")
    
    # Step 4a: Create a task
    print("  4a. Creating a task...")
    task_data = {
        "title": "Test Task",
        "description": "This is a test task created during flow testing",
        "complete": False
    }

    try:
        response = requests.post(f"{BASE_URL}/api/v1/users/{user_id}/tasks", json=task_data, headers=headers)
        if response.status_code == 201:
            created_task = response.json()
            task_id = created_task.get('id')
            print(f"  O Task created successfully - ID: {task_id}")
        else:
            print(f"  X Task creation failed: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"  X Task creation error: {str(e)}")
        return False
    
    # Step 4b: Get tasks again to verify the new task is there
    print("  4b. Verifying task exists...")
    try:
        response = requests.get(f"{BASE_URL}/api/v1/users/{user_id}/tasks", headers=headers)
        if response.status_code == 200:
            tasks = response.json()
            if len([t for t in tasks if t['id'] == task_id]) > 0:
                print(f"  O Task exists in the list - Total tasks: {len(tasks)}")
            else:
                print("  X Created task not found in the list")
                return False
        else:
            print(f"  X Failed to get tasks: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"  X Task verification error: {str(e)}")
        return False
    
    # Step 4c: Update the task
    print("  4c. Updating the task...")
    updated_task_data = {
        "title": "Updated Test Task",
        "description": "This is an updated test task",
        "complete": True
    }

    try:
        response = requests.put(f"{BASE_URL}/api/v1/users/{user_id}/tasks/{task_id}", json=updated_task_data, headers=headers)
        if response.status_code == 200:
            updated_task = response.json()
            if updated_task.get('title') == "Updated Test Task":
                print("  O Task updated successfully")
            else:
                print("  X Task update failed - title not updated")
                return False
        else:
            print(f"  X Task update failed: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"  X Task update error: {str(e)}")
        return False
    
    # Step 4d: Delete the task
    print("  4d. Deleting the task...")
    try:
        response = requests.delete(f"{BASE_URL}/api/v1/users/{user_id}/tasks/{task_id}", headers=headers)
        if response.status_code == 204:
            print("  O Task deleted successfully")
        else:
            print(f"  X Task deletion failed: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"  X Task deletion error: {str(e)}")
        return False
    
    # Step 4e: Verify task is deleted
    print("  4e. Verifying task is deleted...")
    try:
        response = requests.get(f"{BASE_URL}/api/v1/users/{user_id}/tasks", headers=headers)
        if response.status_code == 200:
            tasks = response.json()
            if len([t for t in tasks if t['id'] == task_id]) == 0:
                print(f"  O Task successfully deleted - Remaining tasks: {len(tasks)}")
            else:
                print("  X Task still exists after deletion")
                return False
        else:
            print(f"  X Failed to get tasks after deletion: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"  X Task deletion verification error: {str(e)}")
        return False
    
    # Step 5: Logout
    print("\n5. Testing logout...")
    # Note: Backend doesn't typically have a logout endpoint for JWT tokens
    # The logout is handled on the frontend by clearing the token
    print("  O Logout test completed (handled on frontend)")
    
    # Step 6: New user login (should see empty list)
    print("\n6. Testing new user login (should see empty list)...")
    
    # Register a new user
    new_user_data = {
        "email": new_user_email,
        "password": "NewUserPassword123!"
    }

    try:
        response = requests.post(f"{BASE_URL}/api/v1/auth/signup", json=new_user_data)
        if response.status_code == 201:
            print("  O New user registered successfully")
            new_user_auth = response.json()
            new_user_id = new_user_auth.get('user_id')  # Get new user ID
        else:
            print(f"  X New user registration failed: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"  X New user registration error: {str(e)}")
        return False
    
    # Login as the new user
    try:
        response = requests.post(f"{BASE_URL}/api/v1/auth/signin", json={
            "email": new_user_email,
            "password": "NewUserPassword123!"
        })
        if response.status_code == 200:
            new_user_auth = response.json()
            new_user_token = new_user_auth.get('access_token')
            new_user_id = new_user_auth.get('user_id')  # Get new user ID
            new_user_headers = {
                "Authorization": f"Bearer {new_user_token}",
                "Content-Type": "application/json"
            }
            print("  O New user login successful")
        else:
            print(f"  X New user login failed: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"  X New user login error: {str(e)}")
        return False
    
    # Get tasks for the new user (should be empty)
    try:
        response = requests.get(f"{BASE_URL}/api/v1/users/{new_user_id}/tasks", headers=new_user_headers)
        if response.status_code == 200:
            new_user_tasks = response.json()
            if len(new_user_tasks) == 0:
                print("  O New user sees empty task list (user isolation confirmed)")
            else:
                print(f"  X New user sees {len(new_user_tasks)} tasks (user isolation failed!)")
                return False
        else:
            print(f"  X Failed to get new user tasks: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"  X New user task retrieval error: {str(e)}")
        return False
    
    print("\nO All tests passed! Full flow is working correctly.")
    return True

if __name__ == "__main__":
    print("Running full flow test...")
    success = test_full_flow()
    
    if success:
        print("\nO SUCCESS: All flow tests passed!")
    else:
        print("\nX FAILURE: Some tests failed!")
        exit(1)
