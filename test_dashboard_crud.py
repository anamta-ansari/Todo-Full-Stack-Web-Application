import requests
import json
import time

# Configuration
BASE_URL = "http://localhost:8000"
EMAIL = "testuser@example.com"
PASSWORD = "testpassword123"

def test_dashboard_crud():
    print("Testing Dashboard CRUD Operations...")

    # Step 1: Sign up a user or sign in if already exists
    print("\n1. Attempting to sign up user...")
    signup_response = requests.post(
        f"{BASE_URL}/api/v1/auth/signup",
        headers={"Content-Type": "application/json"},
        data=json.dumps({
            "email": EMAIL,
            "password": PASSWORD
        })
    )

    if signup_response.status_code in [200, 201]:
        print("[SUCCESS] User signed up successfully")
        response_data = signup_response.json()
        token = response_data.get('access_token')
        user_id = response_data.get('user_id')
    elif signup_response.status_code == 409:  # Conflict - user already exists
        print("[INFO] User already exists, signing in instead...")
        signin_response = requests.post(
            f"{BASE_URL}/api/v1/auth/signin",
            headers={"Content-Type": "application/json"},
            data=json.dumps({
                "email": EMAIL,
                "password": PASSWORD
            })
        )

        if signin_response.status_code == 200:
            print("[SUCCESS] User signed in successfully")
            response_data = signin_response.json()
            token = response_data.get('access_token')
            user_id = response_data.get('user_id')
        else:
            print(f"[ERROR] Failed to sign in: {signin_response.text}")
            return False
    else:
        print(f"[ERROR] Failed to sign up: {signup_response.text}")
        return False

    # Step 2: Sign in to get token (if not returned from signup)
    if not token:
        print("\n2. Signing in to get token...")
        signin_response = requests.post(
            f"{BASE_URL}/api/v1/auth/signin",
            headers={"Content-Type": "application/json"},
            data=json.dumps({
                "email": EMAIL,
                "password": PASSWORD
            })
        )

        if signin_response.status_code == 200:
            print("[SUCCESS] User signed in successfully")
            response_data = signin_response.json()
            token = response_data.get('access_token')
            user_id = response_data.get('user_id')
        else:
            print(f"[ERROR] Failed to sign in: {signin_response.text}")
            return False

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # Step 3: Create a task
    print("\n3. Creating a task...")
    task_data = {
        "title": "Test Task",
        "description": "This is a test task for CRUD operations"
    }

    create_response = requests.post(
        f"{BASE_URL}/api/v1/users/{user_id}/tasks",
        headers=headers,
        data=json.dumps(task_data)
    )

    if create_response.status_code == 201:
        print("[SUCCESS] Task created successfully")
        created_task = create_response.json()
        task_id = created_task.get('id')
        print(f"  Task ID: {task_id}")
    else:
        print(f"[ERROR] Failed to create task: {create_response.text}")
        return False

    # Step 4: Get all tasks
    print("\n4. Retrieving all tasks...")
    get_tasks_response = requests.get(
        f"{BASE_URL}/api/v1/users/{user_id}/tasks",
        headers=headers
    )

    if get_tasks_response.status_code == 200:
        tasks = get_tasks_response.json()
        print(f"[SUCCESS] Retrieved {len(tasks)} tasks")
        if len(tasks) > 0:
            print(f"  First task: {tasks[0]['title']}")
    else:
        print(f"[ERROR] Failed to retrieve tasks: {get_tasks_response.text}")
        return False

    # Step 5: Update the task
    print("\n5. Updating the task...")
    update_data = {
        "title": "Updated Test Task",
        "description": "This is an updated test task for CRUD operations",
        "complete": False
    }

    update_response = requests.put(
        f"{BASE_URL}/api/v1/users/{user_id}/tasks/{task_id}",
        headers=headers,
        data=json.dumps(update_data)
    )

    if update_response.status_code == 200:
        print("[SUCCESS] Task updated successfully")
        updated_task = update_response.json()
        print(f"  Updated title: {updated_task['title']}")
    else:
        print(f"[ERROR] Failed to update task: {update_response.text}")
        return False

    # Step 6: Toggle task completion
    print("\n6. Toggling task completion...")
    toggle_response = requests.patch(
        f"{BASE_URL}/api/v1/users/{user_id}/tasks/{task_id}/complete",
        headers=headers
    )

    if toggle_response.status_code == 200:
        print("[SUCCESS] Task completion toggled successfully")
        toggled_task = toggle_response.json()
        print(f"  Completed status: {toggled_task['complete']}")
    else:
        print(f"[ERROR] Failed to toggle task completion: {toggle_response.text}")
        return False

    # Step 7: Delete the task
    print("\n7. Deleting the task...")
    delete_response = requests.delete(
        f"{BASE_URL}/api/v1/users/{user_id}/tasks/{task_id}",
        headers=headers
    )

    if delete_response.status_code == 204:
        print("[SUCCESS] Task deleted successfully")
    else:
        print(f"[ERROR] Failed to delete task: {delete_response.text}")
        return False

    # Step 8: Verify task is deleted
    print("\n8. Verifying task deletion...")
    get_deleted_response = requests.get(
        f"{BASE_URL}/api/v1/users/{user_id}/tasks/{task_id}",
        headers=headers
    )

    if get_deleted_response.status_code == 404:
        print("[SUCCESS] Task successfully deleted (not found)")
    else:
        print(f"[ERROR] Task still exists: {get_deleted_response.text}")
        return False

    print("\n[SUCCESS] All CRUD operations completed successfully!")
    return True

if __name__ == "__main__":
    test_dashboard_crud()