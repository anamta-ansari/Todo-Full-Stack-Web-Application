# Research: Authentication & API Security

## Decision: Authentication Solution
**Rationale**: Selected Better Auth with JWT plugin for its ease of integration with Next.js and comprehensive authentication features. Better Auth provides built-in signup/signin forms and handles JWT token issuance automatically.

## Decision: Frontend Authentication Flow
**Rationale**: Using Next.js App Router with middleware to protect routes. The middleware will check for valid JWT tokens and redirect unauthenticated users to the login page.

## Decision: Backend JWT Verification
**Rationale**: Implementing JWT verification middleware in FastAPI to validate tokens on each authenticated request and extract the user_id for enforcing ownership.

## Decision: User Isolation Strategy
**Rationale**: Adding user_id filter to all database queries in the backend to ensure users can only access their own data. This will be implemented as a dependency in FastAPI.

## Decision: Shared Secret Management
**Rationale**: Using environment variables (BETTER_AUTH_SECRET) for the shared secret between frontend and backend, stored in .env files and loaded with python-dotenv.

## Alternatives Considered
- For authentication: NextAuth.js vs Clerk vs Better Auth → Chose Better Auth for its JWT plugin support
- For route protection: Client-side vs Middleware → Chose middleware for better security
- For token storage: localStorage vs cookies → Following Better Auth's recommended approach
- For backend auth: Custom JWT verification vs libraries → Chose python-jose for JWT handling