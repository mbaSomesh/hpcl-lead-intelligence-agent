import sqlite3

DB = "data/leads.db"

def init():

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS leads (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        company TEXT,

        industry TEXT,

        product TEXT,

        score INTEGER,

        urgency TEXT,

        source TEXT,

        signal TEXT,

        confidence REAL

    )
    """)

    conn.commit()

    conn.close()
