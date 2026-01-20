from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy import event
from sqlmodel import Session
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get database URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./todo_app.db")  # Fallback to SQLite for testing

# For SQLite, we need to use StaticPool and check_same_thread
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        DATABASE_URL,
        connect_args={
            "check_same_thread": False,
            "timeout": 30  # Increase timeout to handle potential locking issues
        },
        poolclass=StaticPool,
        echo=True,  # Enable SQL logging for debugging
        pool_pre_ping=True  # Verify connections before use
    )

    # Enable WAL mode for better concurrency in SQLite
    @event.listens_for(engine, "connect")
    def set_sqlite_pragma(dbapi_connection, connection_record):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA journal_mode=WAL")
        cursor.close()
else:
    engine = create_engine(DATABASE_URL)

def get_session():
    with Session(engine) as session:
        yield session