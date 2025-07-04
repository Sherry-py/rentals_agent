import json
import sqlite3

def save_to_json(results, filename='domain_listings.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"已保存到 {filename}")

def save_to_sqlite(results, dbname='domain_listings.db'):
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS listings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        price TEXT,
        address TEXT
    )
    ''')

    for item in results:
        cursor.execute('''
        INSERT INTO listings (title, price, address) VALUES (?, ?, ?)
        ''', (item.get('title'), item.get('price'), item.get('address')))
    conn.commit()
    conn.close()
    print(f"已保存到 {dbname}")