import requests
import json

# Test the API endpoints directly to make sure they work properly
BASE_URL = 'http://localhost:8000'
EMAIL = 'testuser@example.com'
PASSWORD = 'testpassword123'

print("Starting API functionality test...")

# Sign in to get token
signin_response = requests.post(
    f'{BASE_URL}/api/v1/auth/signin',
    headers={'Content-Type': 'application/json'},
    data=json.dumps({'email': EMAIL, 'password': PASSWORD})
)

if signin_response.status_code == 200:
    token = signin_response.json().get('access_token')
    user_id = signin_response.json().get('user_id')
    print(f'Signed in successfully. User ID: {user_id}')
    
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    
    # Create a test task
    task_data = {'title': 'Test Update Task', 'description': 'Task for testing update functionality'}
    create_resp = requests.post(f'{BASE_URL}/api/v1/users/{user_id}/tasks', headers=headers, data=json.dumps(task_data))
    
    if create_resp.status_code == 201:
        task = create_resp.json()
        task_id = task['id']
        print(f'Task created successfully. ID: {task_id}, Title: {task["title"]}')
        
        # Test updating the task
        update_data = {'title': 'Updated Test Task Title', 'description': 'Updated description'}
        update_resp = requests.put(f'{BASE_URL}/api/v1/users/{user_id}/tasks/{task_id}', headers=headers, data=json.dumps(update_data))
        
        if update_resp.status_code == 200:
            updated_task = update_resp.json()
            print(f'Task updated successfully. New title: {updated_task["title"]}')
            
            # Test toggling completion
            toggle_resp = requests.patch(f'{BASE_URL}/api/v1/users/{user_id}/tasks/{task_id}/complete', headers=headers)
            if toggle_resp.status_code == 200:
                toggled_task = toggle_resp.json()
                print(f'Task completion toggled. Status: {toggled_task["complete"]}')
                
                # Toggle back to incomplete
                toggle_resp2 = requests.patch(f'{BASE_URL}/api/v1/users/{user_id}/tasks/{task_id}/complete', headers=headers)
                if toggle_resp2.status_code == 200:
                    toggled_back = toggle_resp2.json()
                    print(f'Task completion toggled back. Status: {toggled_back["complete"]}')
                    
                    # Clean up - delete the test task
                    delete_resp = requests.delete(f'{BASE_URL}/api/v1/users/{user_id}/tasks/{task_id}', headers=headers)
                    if delete_resp.status_code == 204:
                        print('Test task cleaned up successfully.')
                        print('All tests passed!')
                    else:
                        print(f'Failed to delete test task: {delete_resp.text}')
                else:
                    print(f'Failed to toggle task back: {toggle_resp2.text}')
            else:
                print(f'Failed to toggle task completion: {toggle_resp.text}')
        else:
            print(f'Failed to update task: {update_resp.text}')
        
        # Clean up in case of failure
        if 'delete_resp' not in locals():
            requests.delete(f'{BASE_URL}/api/v1/users/{user_id}/tasks/{task_id}', headers=headers)
    else:
        print(f'Failed to create task: {create_resp.text}')
else:
    print(f'Failed to sign in: {signin_response.text}')