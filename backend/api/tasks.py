# backend/api/tasks.py
import logging
from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlmodel import Session, select
from typing import List
from backend.models.task import Task, TaskCreate, TaskUpdate, TaskRead
from backend.models.user import User
from backend.db.session import get_session
from backend.dependencies.auth import get_current_user

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter(tags=["tasks"])

@router.get("/users/{user_id}/tasks", response_model=List[TaskRead])
def get_tasks(
    user_id: int,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Get all tasks for the specified user
    """
    # Verify that the user ID in the path matches the authenticated user
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Cannot access tasks for another user"
        )

    # Only return tasks that belong to the current user
    statement = select(Task).where(Task.user_id == current_user.id)
    tasks = session.exec(statement).all()
    return tasks

@router.get("/users/{user_id}/tasks/{task_id}", response_model=TaskRead)
def get_task(
    user_id: int,
    task_id: int,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Get a specific task for the specified user
    """
    # Verify that the user ID in the path matches the authenticated user
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Cannot access tasks for another user"
        )

    # Get the task and verify it belongs to the current user
    db_task = session.get(Task, task_id)

    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    if db_task.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Task does not belong to authenticated user"
        )

    return db_task


@router.post("/users/{user_id}/tasks", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(
    request: Request,
    user_id: int,
    task: TaskCreate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Create a new task for the specified user
    """
    # Log the incoming request
    logger.info(f"Creating task for user_id={user_id} by authenticated user_id={current_user.id}")

    # Verify that the user ID in the path matches the authenticated user
    if current_user.id != user_id:
        logger.warning(f"User {current_user.id} attempted to create task for user {user_id}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Cannot create tasks for another user"
        )

    try:
        # Validate the incoming data
        if not task.title or task.title.strip() == "":
            logger.error("Task creation failed: Title is required and cannot be empty")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Title is required and cannot be empty"
            )

        # Additional validation can be added here if needed

        # Create task with the authenticated user's ID
        db_task = Task(
            title=task.title,
            description=task.description,
            complete=task.complete,
            user_id=current_user.id
        )

        session.add(db_task)
        session.commit()
        session.refresh(db_task)

        logger.info(f"Successfully created task {db_task.id} for user {current_user.id}")
        return db_task

    except HTTPException:
        # Re-raise HTTP exceptions as-is
        raise
    except ValueError as ve:
        # Handle validation errors from the model
        logger.error(f"Task creation validation error: {str(ve)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Validation error: {str(ve)}"
        )
    except Exception as e:
        # Handle any other unexpected errors
        logger.error(f"Unexpected error during task creation: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred while creating the task"
        )


@router.put("/users/{user_id}/tasks/{task_id}", response_model=TaskRead)
def update_task(
    user_id: int,
    task_id: int,
    task_update: TaskUpdate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Update a task if it belongs to the specified user
    """
    # Verify that the user ID in the path matches the authenticated user
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Cannot update tasks for another user"
        )

    # Get the task and verify it belongs to the current user
    db_task = session.get(Task, task_id)

    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    if db_task.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Task does not belong to authenticated user"
        )

    # Update the task
    task_data = task_update.dict(exclude_unset=True)
    for key, value in task_data.items():
        setattr(db_task, key, value)

    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task


@router.patch("/users/{user_id}/tasks/{task_id}/complete", response_model=TaskRead)
def toggle_task_completion(
    user_id: int,
    task_id: int,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Toggle the completion status of a task for the specified user
    """
    # Verify that the user ID in the path matches the authenticated user
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Cannot toggle completion for another user's task"
        )

    # Get the task and verify it belongs to the current user
    db_task = session.get(Task, task_id)

    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    if db_task.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Task does not belong to authenticated user"
        )

    # Toggle the completion status
    db_task.complete = not db_task.complete
    session.add(db_task)
    session.commit()
    session.refresh(db_task)

    return db_task


@router.delete("/users/{user_id}/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    user_id: int,
    task_id: int,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Delete a task if it belongs to the specified user
    """
    # Verify that the user ID in the path matches the authenticated user
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Cannot delete tasks for another user"
        )

    # Get the task and verify it belongs to the current user
    db_task = session.get(Task, task_id)

    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    if db_task.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Task does not belong to authenticated user"
        )

    # Delete the task
    session.delete(db_task)
    session.commit()
    return