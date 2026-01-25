"""
Debug script to check the database connection and Task model
"""

from backend.db.session import engine
from backend.models.task import Task
from sqlmodel import select
from sqlalchemy import text

def test_db_connection():
    print("Testing database connection and Task model...")
    
    try:
        # Test basic database connectivity
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            print("[OK] Basic database connection works")

        # Test if Task table exists by querying it
        with engine.connect() as conn:
            # Try to count tasks for user ID 7 (our test user)
            stmt = select(Task).where(Task.user_id == 7)
            result = conn.execute(stmt)
            tasks = result.fetchall()
            print(f"[OK] Task query works, found {len(tasks)} tasks for user 7")

        print("[OK] All database tests passed")

    except Exception as e:
        print(f"[ERROR] Database test failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_db_connection()