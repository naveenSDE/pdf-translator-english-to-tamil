import sqlite3

DB_NAME = "translations.db"


def create_table():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS translations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        original_text TEXT,
        translated_text TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_translation(original, translated):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO translations (original_text, translated_text) VALUES (?, ?)",
        (original, translated)
    )

    conn.commit()
    conn.close()