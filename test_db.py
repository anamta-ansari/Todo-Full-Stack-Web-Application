from backend.db.session import engine
from backend.models.user import User
from sqlmodel import Session, select

# Test database connection
try:
    print("Attempting to connect to database...")
    with Session(engine) as session:
        print("Connected to database successfully!")
        
        # Try to query users table
        statement = select(User)
        users = session.exec(statement).all()
        print(f"Number of users in database: {len(users)}")
        
        print("Database connection test passed!")
except Exception as e:
    print(f"Database connection test failed: {e}")
    import traceback
    traceback.print_exc()