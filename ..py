import sqlite3
import json
from datetime import datetime

conn = sqlite3.connect('staff.db')
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")

cursor.execute("""
CREATE TABLE IF NOT EXISTS game(
    vergil_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vergil_name TEXT,               
    vergil_price TEXT,
    nationality TEXT
):
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS proget (
    proget_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    proget_name TEXT,
    proget_data data,
)
""")
with open(
     "r", encoding="utf-8"
) as f:
    games = json.load(f)

for  game in games:

    cursor.execute("""
    INSERT INTO games (
    vergil_id, vergil_name, vergil_price,  nationality
    )
    VALUES (?, ?, ?, ?)
                   
""",(
    game["vergil_id"],
    game["vergil_name"],
    game["vergil_price"],
    game["nationality"]
))

    
    game_id = cursor.lastrowid
cursor.execute("""
            INSERT INTO games (proget_id, proget_name, proget_data,  )
            VALUES (?, ?, ?)

""", (
    game_id,
    parse_data_safe(game.get("ver"))
))

cursor.execute