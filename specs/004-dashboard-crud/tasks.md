---

description: "Task list for dashboard and CRUD integration"
---

# Tasks: Dashboard & Full CRUD Integration

**Input**: Design documents from `/specs/004-dashboard-crud/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Web app**: `backend/src/`, `frontend/src/`
- Paths shown below assume web app structure - adjust based on plan.md structure

<!--
  ============================================================================
  IMPORTANT: The tasks below are based on the actual design documents
  ============================================================================
-->

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create frontend/app/dashboard/page.tsx as protected Todo dashboard
- [x] T002 [P] Create frontend/components/dashboard/task-list.tsx component
- [x] T003 [P] Create frontend/components/dashboard/add-task-form.tsx component
- [x] T004 [P] Create frontend/components/dashboard/task-item.tsx component
- [x] T005 [P] Create frontend/components/dashboard/edit-task-modal.tsx component

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T006 Implement route protection in frontend/middleware.ts for /dashboard route
- [x] T007 Create frontend/lib/api.ts with authenticated API request functions
- [x] T008 Update frontend/lib/auth.ts with signOut() functionality
- [x] T009 Ensure backend API endpoints for tasks are properly implemented in backend/api/tasks.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Dashboard Access and Task Viewing (Priority: P1) 🎯 MVP

**Goal**: Allow authenticated users to access their protected dashboard and view all their tasks in one place

**Independent Test**: After logging in, the user can navigate to the /dashboard route and see a list of their tasks. If they have no tasks, they see an empty state. If they have tasks, they see them displayed with title, description, and completion status.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

- [ ] T010 [P] [US1] Contract test for GET /api/v1/tasks endpoint in tests/contract/test_get_tasks.py
- [ ] T011 [P] [US1] Integration test for dashboard access in tests/integration/test_dashboard_access.py

### Implementation for User Story 1

- [x] T012 [US1] Implement task list fetching in dashboard (GET /api/v1/tasks with JWT)
- [x] T013 [US1] Display tasks in the dashboard with title, description, and completion status
- [x] T014 [US1] Show empty state when user has no tasks
- [x] T015 [US1] Ensure dashboard redirects unauthenticated users to login
- [x] T016 [US1] Add loading state while fetching tasks
- [x] T017 [US1] Style task list with Tailwind CSS (cards, hover effects)

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Add New Tasks (Priority: P1)

**Goal**: Allow authenticated users to add new tasks to their dashboard to keep track of what they need to do

**Independent Test**: An authenticated user can submit a form with a task title and optional description, and the new task appears in their task list immediately.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T018 [P] [US2] Contract test for POST /api/v1/tasks endpoint in tests/contract/test_add_task.py
- [ ] T019 [P] [US2] Integration test for adding tasks in tests/integration/test_add_task.py

### Implementation for User Story 2

- [x] T020 [US2] Build add task form in dashboard (POST /api/v1/tasks with JWT)
- [x] T021 [US2] Validate required title field in add task form
- [x] T022 [US2] Handle successful task creation (new task appears in list)
- [x] T023 [US2] Handle error cases (empty title, API errors)
- [x] T024 [US2] Add loading state during task creation
- [x] T025 [US2] Style add task form with Tailwind CSS

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update and Complete Tasks (Priority: P1)

**Goal**: Allow authenticated users to update their tasks and mark them as complete to track their progress

**Independent Test**: An authenticated user can edit task details and toggle the completion status, with changes reflected immediately in the UI.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T026 [P] [US3] Contract test for PUT /api/v1/tasks/{id} endpoint in tests/contract/test_update_task.py
- [ ] T027 [P] [US3] Integration test for updating tasks in tests/integration/test_update_task.py

### Implementation for User Story 3

- [x] T028 [US3] Add edit task functionality (inline or modal, PUT /api/v1/tasks/{id})
- [x] T029 [US3] Add toggle complete button (PUT /api/v1/tasks/{id} with complete field)
- [x] T030 [US3] Implement edit modal/form with proper validation
- [x] T031 [US3] Handle successful task updates (UI updates immediately)
- [x] T032 [US3] Handle error cases for updates
- [x] T033 [US3] Add loading states for update operations
- [x] T034 [US3] Style edit components with Tailwind CSS

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Delete Tasks (Priority: P2)

**Goal**: Allow authenticated users to delete tasks that they no longer need to keep their dashboard clean and organized

**Independent Test**: An authenticated user can delete a task, and it disappears from their task list immediately.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [ ] T035 [P] [US4] Contract test for DELETE /api/v1/tasks/{id} endpoint in tests/contract/test_delete_task.py
- [ ] T036 [P] [US4] Integration test for deleting tasks in tests/integration/test_delete_task.py

### Implementation for User Story 4

- [x] T037 [US4] Add delete button to each task (DELETE /api/v1/tasks/{id})
- [x] T038 [US4] Implement confirmation dialog for deletion
- [x] T039 [US4] Handle successful task deletion (task removed from UI)
- [x] T040 [US4] Handle error cases for deletion
- [x] T041 [US4] Add loading states for delete operations
- [x] T042 [US4] Style delete button with Tailwind CSS

**Checkpoint**: At this point, all user stories should work independently

---

## Phase 7: User Story 5 - Logout and Session Management (Priority: P1)

**Goal**: Allow authenticated users to securely log out so that others cannot access their tasks on shared devices

**Independent Test**: A user can click a logout button, their session is cleared, and they are redirected to the login page.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [ ] T043 [P] [US5] Contract test for logout functionality in tests/contract/test_logout.py
- [ ] T044 [P] [US5] Integration test for logout flow in tests/integration/test_logout_flow.py

### Implementation for User Story 5

- [x] T045 [US5] Integrate logout button with signOut() in dashboard
- [x] T046 [US5] Ensure logout redirects to login page
- [x] T047 [US5] Clear authentication state on logout
- [x] T048 [US5] Test that user cannot access dashboard after logout

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T049 [P] Add loading/error/success states for all CRUD operations
- [x] T050 [P] Style dashboard with beautiful Tailwind UI (cards, gradients, hover effects, responsive)
- [x] T051 [P] Add error handling with user-friendly messages
- [x] T052 [P] Ensure responsive design works across all device sizes
- [x] T053 [P] Test full flow: signup → signin → dashboard → CRUD → logout → new user → empty list
- [x] T054 [P] Update README.md with updated run instructions and flow
- [x] T055 [P] Verify user isolation: second user login sees only own tasks (no cross-user data visible)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - Depends on task list from US1
- **User Story 3 (P1)**: Can start after Foundational (Phase 2) - Depends on task list from US1
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - Depends on task list from US1
- **User Story 5 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Components within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Contract test for GET /api/v1/tasks endpoint in tests/contract/test_get_tasks.py"
Task: "Integration test for dashboard access in tests/integration/test_dashboard_access.py"

# Launch dashboard implementation tasks:
Task: "Implement task list fetching in dashboard (GET /api/v1/tasks with JWT)"
Task: "Display tasks in the dashboard with title, description, and completion status"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence