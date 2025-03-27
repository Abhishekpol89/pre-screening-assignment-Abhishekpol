import os
import psycopg2

DATABASE_URL = os.getenv("DATABASE_URL")

def get_db_connection():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        print("Connected successfully")
        return conn
    except Exception as e:
        print(f"Database connection failed: {e}")

conn = get_db_connection()

