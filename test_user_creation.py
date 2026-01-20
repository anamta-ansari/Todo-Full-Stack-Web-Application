import sys
import os
sys.path.insert(0, os.path.abspath('.'))

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

print("Environment loaded")

# Test imports
try:
    from backend.models.user import User, UserCreate, UserRead
    print("User models imported successfully")
except Exception as e:
    print(f"Error importing user models: {e}")
    import traceback
    traceback.print_exc()

# Test creating a user object
try:
    user_create = UserCreate(email="test@example.com", password="password123")
    print(f"UserCreate object created: {user_create}")
except Exception as e:
    print(f"Error creating UserCreate object: {e}")
    import traceback
    traceback.print_exc()

# Test database session
try:
    from backend.db.session import get_session, engine
    print("DB session imported successfully")
    
    # Test creating a session
    from sqlmodel import Session
    with Session(engine) as session:
        print("Database session created successfully")
except Exception as e:
    print(f"Error with database session: {e}")
    import traceback
    traceback.print_exc()

# Test creating a user in the database
try:
    from passlib.context import CryptContext
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    from backend.models.user import User
    from sqlmodel import Session
    from backend.db.session import engine
    
    hashed_password = pwd_context.hash("password123")
    db_user = User(email="test@example.com", password_hash=hashed_password)
    
    print(f"User object created: {db_user}")
    
    # Try to add to database
    with Session(engine) as session:
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        print(f"User added to database with ID: {db_user.id}")
        
        # Test model validation
        user_read = UserRead.model_validate(db_user)
        print(f"UserRead object created: {user_read}")
        
except Exception as e:
    print(f"Error creating user in database: {e}")
    import traceback
    traceback.print_exc()