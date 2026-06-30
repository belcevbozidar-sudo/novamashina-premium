# -*- coding: utf-8 -*-
import os
import sqlite3
import sys

# Ensure correct working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

DB_PATH = 'database.db'

def create_schema(conn):
    cursor = conn.cursor()
    
    # Products table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        slug TEXT NOT NULL,
        brand TEXT NOT NULL,
        model TEXT NOT NULL,
        title TEXT NOT NULL,
        cat TEXT NOT NULL,
        state TEXT NOT NULL,
        img TEXT NOT NULL,
        price INTEGER NOT NULL,
        monthly INTEGER NOT NULL,
        fuel TEXT,
        hp TEXT,
        trans TEXT,
        loc TEXT,
        year TEXT,
        hours TEXT,
        engine TEXT,
        offer TEXT,
        views INTEGER DEFAULT 0,
        dealer TEXT,
        tank TEXT,
        desc TEXT,
        lease_ret INTEGER DEFAULT 0
    )
    ''')
    
    # Users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL
    )
    ''')
    
    # Login attempts table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS login_attempts (
        ip_address TEXT NOT NULL,
        attempt_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # Sessions table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sessions (
        token TEXT PRIMARY KEY,
        user_id INTEGER NOT NULL,
        expires_at TIMESTAMP NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    ''')
    
    conn.commit()
    print("Schema created successfully.")

def migrate_products(conn):
    # Import MACHINES from build_site.py
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    try:
        from build_site import MACHINES
    except ImportError as e:
        print(f"Error importing build_site: {e}")
        return

    cursor = conn.cursor()
    
    # Check if products already exist
    cursor.execute("SELECT COUNT(*) FROM products")
    if cursor.fetchone()[0] > 0:
        print("Products table already has data. Skipping product migration.")
        return

    for m in MACHINES:
        cursor.execute('''
        INSERT INTO products (
            id, slug, brand, model, title, cat, state, img, price, monthly,
            fuel, hp, trans, loc, year, hours, engine, offer, views, dealer, tank, desc, lease_ret
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            m.get('id'),
            m.get('slug'),
            m.get('brand'),
            m.get('model'),
            m.get('title'),
            m.get('cat'),
            m.get('state'),
            m.get('img'),
            m.get('price'),
            m.get('monthly', 0),
            m.get('fuel'),
            m.get('hp'),
            m.get('trans'),
            m.get('loc'),
            m.get('year'),
            m.get('hours'),
            m.get('engine'),
            m.get('offer'),
            m.get('views', 0),
            m.get('dealer'),
            m.get('tank'),
            m.get('desc'),
            1 if m.get('lease_ret') else 0
        ))
    
    conn.commit()
    print(f"Migrated {len(MACHINES)} products successfully.")

def create_admin_user(conn):
    # Hash password securely using Werkzeug if available, otherwise fallback to hashlib
    password = "Zlatex_M@sh1n@_2026!"
    
    try:
        from werkzeug.security import generate_password_hash
        pw_hash = generate_password_hash(password)
    except ImportError:
        # Fallback SHA256 with salt if Werkzeug isn't installed yet (it will be when running Flask)
        import hashlib
        salt = "zlatex_salt_2026_"
        pw_hash = "sha256$" + salt + "$" + hashlib.sha256((salt + password).encode('utf-8')).hexdigest()

    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users WHERE username = 'admin'")
    if cursor.fetchone()[0] > 0:
        print("Admin user already exists. Skipping user creation.")
        return

    cursor.execute("INSERT INTO users (username, password_hash) VALUES ('admin', ?)", (pw_hash,))
    conn.commit()
    print("Admin user created successfully.")

if __name__ == '__main__':
    conn = sqlite3.connect(DB_PATH)
    try:
        create_schema(conn)
        migrate_products(conn)
        create_admin_user(conn)
    finally:
        conn.close()
    print("Migration completed.")
