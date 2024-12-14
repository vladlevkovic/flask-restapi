import sqlite3

def init():
    conn = sqlite3.connect('project.sqlite3')
    cursor = conn.cursor()
    create_table_query = '''CREATE TABLE IF NOT EXISTS quotes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        author TEXT NOT NULL,
        quote TEXT NOT NULL UNIQUE
    )'''
    cursor.execute(create_table_query)
    conn.commit()
    conn.close()

def get_db_connection():
    conn = sqlite3.connect('project.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn

def get_quote(quote_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    quote = cursor.execute('SELECT * FROM quotes WHERE id = ?', (quote_id,)).fetchone()
    print(quote)
    conn.close()
    return quote

def create(author, quote):
    conn = get_db_connection()
    cursor = conn.cursor()
    index = cursor.execute('INSERT INTO quotes (author, quote) VALUES (?, ?)', (author, quote))
    conn.commit()
    conn.close()
    return index

def update(author, quote, quote_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE quotes SET author=?, quote=? WHERE id=?", (author, quote, quote_id))
    conn.commit()
    conn.close()
    return 200

def quote_delete(quote_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM quotes WHERE id=?", (quote_id,))
    conn.commit()
    conn.close()
    return 200
