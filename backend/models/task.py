from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING, Optional
from datetime import datetime

# Handle circular import
if TYPE_CHECKING:
    from .user import User

class TaskBase(SQLModel):
    title: str = Field(nullable=False, max_length=255)
    description: Optional[str] = Field(default=None)
    complete: bool = Field(default=False)

    def validate_title(self):
        """Validate that the title does not exceed 255 characters"""
        if len(self.title) > 255:
            raise ValueError("Title must not exceed 255 characters")

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    title: Optional[str] = Field(default=None, max_length=255)
    description: Optional[str] = Field(default=None)
    complete: Optional[bool] = Field(default=None)

class TaskRead(TaskBase):
    id: int
    user_id: int
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

class Task(TaskBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", nullable=False)
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

    # Temporarily removing relationship to fix circular import issue
    # user: "User" = Relationship(back_populates="tasks")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.validate_title()