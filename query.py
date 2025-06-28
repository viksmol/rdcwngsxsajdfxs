import sqlite3

conn = sqlite3.connect("vergil_db")
cursor = conn.cursor()

def execute_query(query, params=()):
    try:
        cursor.execute(query, params)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(f"помилка при виконанні запиту: {e}")

print("\nназва в алфавітном порядку")

execute_query("""
        SELECT proget_name
        FROM vergil
        ORDER vergil_name ACS

""")