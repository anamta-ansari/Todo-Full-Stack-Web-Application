from fastapi import APIRouter, HTTPException
from typing import Dict
from backend.db.session import engine
from sqlmodel import select
from backend.models.user import User

router = APIRouter()

@router.get("/health", response_model=Dict[str, str])
async def health_check():
    """
    Health check endpoint to verify the backend server is running and healthy.
    Returns status ok if the server is operational.
    """
    try:
        # Simple database connectivity check
        with engine.connect() as conn:
            # Attempt a simple query to check DB connectivity
            result = conn.execute(select(User).limit(1))
        
        return {"status": "ok"}
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Database connection failed: {str(e)}")