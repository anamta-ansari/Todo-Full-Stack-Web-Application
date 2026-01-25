"""
Migration script to add missing columns to the task table
"""

import sqlite3
from backend.db.session import DATABASE_URL

def migrate_database():
    print("Starting database migration...")
    
    # Connect to the database
    conn = sqlite3.connect(DATABASE_URL.replace("sqlite:///", ""))
    cursor = conn.cursor()
    
    try:
        # Check if priority column exists
        cursor.execute("PRAGMA table_info(task)")
        columns = [column[1] for column in cursor.fetchall()]
        
        print(f"Current columns in task table: {columns}")
        
        # Add priority column if it doesn't exist
        if 'priority' not in columns:
            print("Adding 'priority' column...")
            cursor.execute("ALTER TABLE task ADD COLUMN priority TEXT DEFAULT 'medium'")
        
        # Add category column if it doesn't exist
        if 'category' not in columns:
            print("Adding 'category' column...")
            cursor.execute("ALTER TABLE task ADD COLUMN category TEXT")
        
        # Add due_date column if it doesn't exist
        if 'due_date' not in columns:
            print("Adding 'due_date' column...")
            cursor.execute("ALTER TABLE task ADD COLUMN due_date TIMESTAMP")
        
        # Commit the changes
        conn.commit()
        print("Database migration completed successfully!")
        
    except Exception as e:
        print(f"Error during migration: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    migrate_database()