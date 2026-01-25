from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.db.session import engine
from backend.models.user import User
from backend.models.task import Task
from sqlmodel import SQLModel
from backend.api.health import router as health_router
from backend.api.auth import router as auth_router
from backend.api.tasks import router as tasks_router

# Import both models to ensure they're registered with SQLAlchemy
from backend.models import user, task

app = FastAPI(title="Todo Backend", version="1.0.0")

# Configure CORS for localhost with common ports
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001",
        "http://localhost:8000",
        "http://localhost:8080",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:3001",
        "http://127.0.0.1:8000",
        "http://127.0.0.1:8080",
        "http://localhost:3002",
        "http://127.0.0.1:3002"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(health_router)
app.include_router(auth_router, prefix="/api/v1")
app.include_router(tasks_router, prefix="/api/v1")

# Create database tables on startup
@app.on_event("startup")
def on_startup():
    # Create all tables if they don't exist
    SQLModel.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo Backend API"}