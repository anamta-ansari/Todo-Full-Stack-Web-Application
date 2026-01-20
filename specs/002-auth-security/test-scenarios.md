# Test authentication functionality

## Test 1: Signup
1. Navigate to `/signup`
2. Enter a valid email and password (at least 8 characters)
3. Submit the form
4. Verify that you're redirected to the dashboard
5. Check that a JWT token is stored in localStorage

## Test 2: Signin
1. Navigate to `/signin`
2. Enter the email and password you used for signup
3. Submit the form
4. Verify that you're redirected to the dashboard
5. Check that a JWT token is stored in localStorage

## Test 3: Protected Route Access
1. Navigate directly to `/dashboard` without being logged in
2. Verify that you're redirected to `/signin`
3. Log in and verify you can access `/dashboard`

## Test 4: API Call with JWT
1. Make sure you're logged in
2. Check that API calls to `/api/v1/tasks` include the Authorization header with the JWT token
3. Verify that the backend accepts the request

## Test 5: Logout
1. Click the logout button on the dashboard
2. Verify that the JWT token is removed from localStorage
3. Verify that you're redirected to the signin page
4. Try to access `/dashboard` and verify you're redirected to `/signin`

## Test 6: User Isolation
1. Create two different user accounts
2. Log in as the first user and create some tasks
3. Log out and log in as the second user
4. Verify that the second user cannot see the first user's tasks
5. Try to access another user's task directly via API - should return 403 Forbidden