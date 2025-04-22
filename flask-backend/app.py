# filepath: flask-backend/app.py
from flask import Flask, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(os.getenv("DATABASE_URL"), cursor_factory=RealDictCursor)
    return conn

@app.route('/api/data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM test_table;')
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)

@app.route('/')
def home():
    return "Hello, Railway!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)