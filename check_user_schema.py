"""
Check user table schema
"""

import sqlite3
from backend.db.session import DATABASE_URL

def check_user_schema():
    print("Checking user table schema...")
    
    # Connect to the database
    conn = sqlite3.connect(DATABASE_URL.replace("sqlite:///", ""))
    cursor = conn.cursor()
    
    try:
        # Check user table columns
        cursor.execute("PRAGMA table_info(user)")
        columns = [column[1] for column in cursor.fetchall()]
        
        print(f"Columns in user table: {columns}")
        
    except Exception as e:
        print(f"Error checking user schema: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    check_user_schema()