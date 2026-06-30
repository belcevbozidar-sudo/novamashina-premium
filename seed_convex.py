# -*- coding: utf-8 -*-
import sqlite3
import os
from convex import ConvexClient
from werkzeug.security import generate_password_hash

# Ensure correct working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

CONVEX_URL = "https://fearless-sparrow-233.eu-west-1.convex.cloud"
DB_PATH = 'database.db'

def seed():
    client = ConvexClient(CONVEX_URL)
    
    # 1. Seed Products from SQLite
    if os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        db_products = cursor.fetchall()
        
        # Check if products already exist on Convex
        convex_products = client.query("products:list")
        if len(convex_products) > 0:
            print("Products already exist in Convex. Skipping product seeding.")
        else:
            for p in db_products:
                m = dict(p)
                # Format arguments matching TypeScript expected types
                # Convex schema: price/monthly are numbers, lease_ret is boolean, hours can be string or null
                hours_val = m.get('hours')
                if hours_val == 'None' or hours_val == '':
                    hours_val = None
                
                args = {
                    "slug": m.get('slug'),
                    "brand": m.get('brand'),
                    "model": m.get('model'),
                    "title": m.get('title'),
                    "cat": m.get('cat'),
                    "state": m.get('state'),
                    "img": m.get('img'),
                    "price": int(m.get('price', 0)),
                    "monthly": int(m.get('monthly', 0)),
                    "fuel": m.get('fuel'),
                    "hp": m.get('hp'),
                    "trans": m.get('trans'),
                    "loc": m.get('loc'),
                    "year": m.get('year'),
                    "hours": hours_val,
                    "engine": m.get('engine'),
                    "offer": m.get('offer'),
                    "dealer": m.get('dealer'),
                    "tank": m.get('tank'),
                    "desc": m.get('desc'),
                    "lease_ret": True if m.get('lease_ret') == 1 else False
                }
                client.mutation("products:add", args)
            print(f"Seeded {len(db_products)} products successfully to Convex.")
        conn.close()
    else:
        print("SQLite database.db not found, cannot seed products.")

    # 2. Seed Admin User
    password = "Zlatex_M@sh1n@_2026!"
    pw_hash = generate_password_hash(password, method='pbkdf2:sha256')
    client.mutation("users:createAdmin", {"username": "admin", "passwordHash": pw_hash})
    print("Admin user seeded to Convex successfully.")

if __name__ == '__main__':
    seed()
