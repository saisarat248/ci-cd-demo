import sqlite3

def init_db():
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (name TEXT)")
    conn.commit()
    conn.close()

def add_user(name):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO users VALUES (?)", (name,))
    conn.commit()
    conn.close()

def get_users():
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    conn.close()
    return data
