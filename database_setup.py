import sqlite3

def setup_database():
    conn = sqlite3.connect('pursepal.db')
    cursor = conn.cursor()
    
    # Create table for users if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE,
        balance REAL NOT NULL DEFAULT 0.0
    )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
