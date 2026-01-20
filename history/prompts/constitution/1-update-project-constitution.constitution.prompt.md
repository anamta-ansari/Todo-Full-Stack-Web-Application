---
id: 1
title: Update Project Constitution
stage: constitution
date: 2026-01-13
surface: agent
model: Qwen
feature: none
branch: main
user: Admin
command: /sp.constitution
labels: [constitution, backend, fastapi, sqlmodel, neon]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
 - .specify/templates/plan-template.md
 - .specify/templates/spec-template.md
 - .specify/templates/tasks-template.md
tests:
 - null
---

## Prompt

```
/sp.constitution

## Phase II: Todo Full-Stack Web Application – Part 1: Foundation & Backend Core

### Preamble

This constitution governs Part 1 of Phase II development: establishing the project foundation and backend core (FastAPI + SQLModel + Neon DB).  

We are building from scratch in the current root folder (frontend already has Next.js 16). The frontend will later show sign up/sign in and a protected dashboard for CRUD.

### Core Principles for Part 1

1. **Scope of Part 1**  

   - Set up monorepo structure, constitution, specs, plan, tasks  

   - Implement backend only: FastAPI server, SQLModel models (User, Task), Neon connection  

   - No frontend UI work yet

2. **Technology for Part 1**  

   - Backend: Python FastAPI  

   - ORM: SQLModel  

   - Database: Neon Serverless PostgreSQL  

   - No frontend changes in Part 1

3. **Project Structure (after Part 1)**  

   root/  

   ├── .spec-kit/  

   │   └── config.yaml  

   ├── specs/  

   │   ├── overview.md  

   │   ├── architecture.md  

   │   ├── database/  

   │   └── backend/  

   ├── frontend/ (existing Next.js)  

   ├── backend/  

   │   ├── main.py  

   │   ├── models/  

   │   ├── db/  

   │   └── ...  

   ├── constitution.md  

   ├── docker-compose.yml (optional)  

   └── README.md

4. **Deliverables of Part 1**  

   - Working backend server (uvicorn backend.main:app --reload)  

   - Database models and connection to Neon  

   - Correct run instructions in README
```

## Response snapshot

Updated the project constitution to reflect the requirements for Part 1 of the Todo Full-Stack Web Application. Created a new constitution document with specific principles for the backend-focused development phase. Updated related templates (plan, spec, tasks) to align with the new constitution.

## Outcome

- ✅ Impact: New constitution established for Part 1 backend development
- 🧪 Tests: No automated tests run for this change
- 📁 Files: 4 files updated to align with new constitution
- 🔁 Next prompts: Ready to proceed with spec, plan, and task creation
- 🧠 Reflection: Successfully created a focused constitution for the backend development phase

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin with feature specification based on new constitution
