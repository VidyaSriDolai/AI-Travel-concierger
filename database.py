import sqlite3

def init_db():
    conn = sqlite3.connect("tripsage.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT,
            message TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_message(role, message):
    conn = sqlite3.connect("tripsage.db")
    c = conn.cursor()
    c.execute("INSERT INTO chat_history (role, message) VALUES (?, ?)", (role, message))
    conn.commit()
    conn.close()