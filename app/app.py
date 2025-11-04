from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    try:
        # Connect to MySQL service (service name 'db' acts as hostname)
        conn = mysql.connector.connect(
            host='db',
            user='flaskuser',
            password='flaskpass',
            database='flaskdb'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        db_name = cursor.fetchone()
        conn.close()
        return f"Connected to MySQL database: {db_name[0]}"
    except mysql.connector.Error as err:
        return f"Error connecting to MySQL: {err}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
