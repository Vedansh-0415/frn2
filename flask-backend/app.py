# filepath: flask-backend/app.py
from flask import Flask, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = psycopg2.connect(os.getenv("DATABASE_URL"), cursor_factory=RealDictCursor)
    return conn

@app.route('/api/data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM your_table;')
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)

if __name__ == '__main__':
    app.run(debug=True)