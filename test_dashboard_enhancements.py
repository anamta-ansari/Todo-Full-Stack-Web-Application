"""
Test script to verify the enhanced dashboard features:
- Priorities & Tags/Categories
- Search & Filter
- Sort Tasks
"""

import requests
import json
import time

# Configuration
BASE_URL = "http://localhost:8000"
HEADERS = {"Content-Type": "application/json"}

def test_dashboard_features():
    print("Testing enhanced dashboard features...")
    
    # Step 1: Sign in to get a valid token
    print("\n1. Signing in to get authentication token...")
    signin_response = requests.post(
        f"{BASE_URL}/api/v1/auth/signin",
        headers=HEADERS,
        json={
            "email": "test@example.com",
            "password": "password123"
        }
    )
    
    if signin_response.status_code != 200:
        print(f"Sign in failed: {signin_response.status_code} - {signin_response.text}")
        return
    
    token = signin_response.json().get("access_token")
    HEADERS["Authorization"] = f"Bearer {token}"
    
    # Get user info to get user ID
    user_info = requests.get(f"{BASE_URL}/api/v1/users/me", headers=HEADERS)
    if user_info.status_code != 200:
        print(f"Failed to get user info: {user_info.status_code} - {user_info.text}")
        return
        
    user_id = user_info.json()["id"]
    print(f"Authenticated as user ID: {user_id}")
    
    # Step 2: Create test tasks with different priorities and categories
    print("\n2. Creating test tasks with different priorities and categories...")
    
    test_tasks = [
        {
            "title": "High Priority Work Task",
            "description": "This is a high priority work task",
            "priority": "high",
            "category": "Work",
            "complete": False
        },
        {
            "title": "Medium Priority Personal Task",
            "description": "This is a medium priority personal task",
            "priority": "medium",
            "category": "Personal",
            "complete": False
        },
        {
            "title": "Low Priority Health Task",
            "description": "This is a low priority health task",
            "priority": "low",
            "category": "Health",
            "complete": True
        },
        {
            "title": "Another Work Task",
            "description": "Another task for work",
            "priority": "medium",
            "category": "Work",
            "complete": False
        }
    ]
    
    for task in test_tasks:
        response = requests.post(
            f"{BASE_URL}/api/v1/users/{user_id}/tasks",
            headers=HEADERS,
            json=task
        )
        if response.status_code == 201:
            print(f"Created task: {task['title']}")
        else:
            print(f"Failed to create task: {response.status_code} - {response.text}")
    
    # Step 3: Test filtering by priority
    print("\n3. Testing priority filtering...")
    for priority in ["high", "medium", "low"]:
        response = requests.get(
            f"{BASE_URL}/api/v1/users/{user_id}/tasks",
            headers=HEADERS,
            params={"priority": priority}
        )
        if response.status_code == 200:
            tasks = response.json()
            print(f"  Found {len(tasks)} tasks with priority '{priority}'")
        else:
            print(f"  Failed to filter by priority '{priority}': {response.status_code}")
    
    # Step 4: Test filtering by status
    print("\n4. Testing status filtering...")
    for status in ["completed", "pending"]:
        response = requests.get(
            f"{BASE_URL}/api/v1/users/{user_id}/tasks",
            headers=HEADERS,
            params={"status": status}
        )
        if response.status_code == 200:
            tasks = response.json()
            print(f"  Found {len(tasks)} {status} tasks")
        else:
            print(f"  Failed to filter by status '{status}': {response.status_code}")
    
    # Step 5: Test filtering by category
    print("\n5. Testing category filtering...")
    for category in ["Work", "Personal", "Health"]:
        response = requests.get(
            f"{BASE_URL}/api/v1/users/{user_id}/tasks",
            headers=HEADERS,
            params={"category": category}
        )
        if response.status_code == 200:
            tasks = response.json()
            print(f"  Found {len(tasks)} tasks in category '{category}'")
        else:
            print(f"  Failed to filter by category '{category}': {response.status_code}")
    
    # Step 6: Test search functionality
    print("\n6. Testing search functionality...")
    search_terms = ["Work", "Personal", "high priority"]
    for term in search_terms:
        response = requests.get(
            f"{BASE_URL}/api/v1/users/{user_id}/tasks",
            headers=HEADERS,
            params={"search": term}
        )
        if response.status_code == 200:
            tasks = response.json()
            print(f"  Found {len(tasks)} tasks matching search term '{term}'")
        else:
            print(f"  Failed to search for '{term}': {response.status_code}")
    
    # Step 7: Test sorting functionality
    print("\n7. Testing sorting functionality...")
    sort_options = ["created_at", "priority", "alphabetical", "category", "due_date"]
    for sort_by in sort_options:
        response = requests.get(
            f"{BASE_URL}/api/v1/users/{user_id}/tasks",
            headers=HEADERS,
            params={"sort_by": sort_by}
        )
        if response.status_code == 200:
            tasks = response.json()
            print(f"  Retrieved {len(tasks)} tasks sorted by '{sort_by}'")
        else:
            print(f"  Failed to sort by '{sort_by}': {response.status_code}")
    
    # Step 8: Clean up - delete test tasks
    print("\n8. Cleaning up - deleting test tasks...")
    all_tasks_response = requests.get(
        f"{BASE_URL}/api/v1/users/{user_id}/tasks",
        headers=HEADERS
    )
    
    if all_tasks_response.status_code == 200:
        all_tasks = all_tasks_response.json()
        for task in all_tasks:
            if task["title"].startswith(("High Priority", "Medium Priority", "Low Priority", "Another")):
                delete_response = requests.delete(
                    f"{BASE_URL}/api/v1/users/{user_id}/tasks/{task['id']}",
                    headers=HEADERS
                )
                if delete_response.status_code == 204:
                    print(f"  Deleted task: {task['title']}")
                else:
                    print(f"  Failed to delete task {task['id']}: {delete_response.status_code}")
    
    print("\nDashboard enhancement testing completed!")

if __name__ == "__main__":
    test_dashboard_features()