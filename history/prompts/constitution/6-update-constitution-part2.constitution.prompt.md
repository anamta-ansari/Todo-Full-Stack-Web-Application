---
id: 6
title: Update Constitution for Part 2
stage: constitution
date: 2026-01-13
surface: agent
model: Qwen
feature: none
branch: main
user: Admin
command: /sp.constitution
labels: [constitution, authentication, jwt, better-auth, security]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - null
---

## Prompt

```
/sp.constitution

## Phase II Part 2: Authentication & API Security

### Preamble

This constitution governs Part 2 of Phase II development: implementing authentication and secure API layer.  

We are building from scratch in the current root folder (frontend already has Next.js 16 from Part 1). The frontend will have sign up/sign in pages, and after login a protected dashboard for CRUD.

### Core Principles for Part 2

1. **Scope of Part 2**  

   - Implement Better Auth with JWT plugin  

   - Create signup and signin pages/forms  

   - Issue and attach JWT tokens  

   - Verify JWT in backend and enforce user isolation  

   - Protect dashboard route  

   - No CRUD UI yet (handled in Part 3)

2. **Technology for Part 2**  

   - Authentication: Better Auth with JWT  

   - Frontend: Next.js 16+ (App Router)  

   - Backend: Python FastAPI (from Part 1)  

   - Shared secret: BETTER_AUTH_SECRET (env var)

3. **Authentication Flow**  

   - Signup: email + password → user created → JWT issued  

   - Signin: email + password → JWT issued  

   - Frontend attaches JWT: Authorization: Bearer <token>  

   - Backend verifies JWT, extracts user_id  

   - Unauthorized → 401  

   - Ownership mismatch → 403

4. **Security & Isolation**  

   - Backend must filter all operations by authenticated user_id  

   - No cross-user data access allowed  

   - Protected routes redirect to login if not authenticated

5. **Project Structure Update (after Part 2)**  

   root/  

   ├── frontend/  

   │   ├── app/  

   │   │   ├── signup/page.tsx  

   │   │   ├── signin/page.tsx  

   │   │   └── dashboard/page.tsx (protected, stub for now)  

   │   ├── lib/  

   │   │   └── auth.ts  

   │   └── ...  

   ├── backend/ (from Part 1)  

   └── ... (other files from Part 1)

This constitution sets the rules for Part 2 only. Part 3 will handle dashboard CRUD.
```

## Response snapshot

Updated the project constitution to reflect the requirements for Part 2 of the Todo Full-Stack Web Application, which focuses on authentication and API security. The constitution now includes principles for implementing Better Auth with JWT, frontend authentication pages, and backend security measures.

## Outcome

- ✅ Impact: Constitution updated from v1.0.0 to v2.0.0 with Part 2 requirements
- 🧪 Tests: No automated tests run for this change
- 📁 Files: 1 file updated (constitution.md)
- 🔁 Next prompts: Ready to proceed with Part 2 specification
- 🧠 Reflection: Successfully updated constitution to cover authentication requirements

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Create Part 2 feature specification
