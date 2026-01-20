"""Test script to check database connection"""
from backend.db.session import engine
from sqlmodel import SQLModel
from backend.models.user import User

def test_db_connection():
    try:
        print("Testing database connection...")

        # Try to create tables
        print("Creating tables if they don't exist...")
        SQLModel.metadata.create_all(bind=engine)
        print("Tables created successfully!")

        # Try to create a session
        print("Testing session creation...")
        from sqlmodel import Session

        with Session(engine) as session:
            print("Session created successfully!")

            # Try a simple query using exec() as recommended
            from sqlalchemy import select
            stmt = select(User).where(User.email == "nonexistent@example.com")
            result = session.exec(stmt)
            user = result.first()
            print(f"Query executed successfully, found user: {user}")

        print("Database connection test completed successfully!")

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_db_connection()