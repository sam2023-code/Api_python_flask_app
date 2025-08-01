from flask import Flask,render_template, jsonify, request
import psycopg2
from psycopg2 import sql

app = Flask(__name__, template_folder='templates')  # Ensure this line exists

# Database connection configuration
DB_HOST = 'database-1.ce9ca6cwmebj.us-east-1.rds.amazonaws.com'
DB_PORT = '5432'
DB_NAME = 'postgre_aws'
DB_USER = 'postgres'  # replace with your PostgreSQL username
DB_PASS = 'postgres_pass'    # replace with your PostgreSQL password

# Connect to PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    return conn
    


@app.route('/')
def home():
    return render_template('index.html')  # Ensure this template exists

@app.route("/about/")
def about():
    return render_template('about.html')

@app.route('/api/test', methods=['GET'])
def get_test():
    # Sample data to return
    data = {
        "message": "Hello, World!",
        "status": "success"
    }
    return jsonify(data)

@app.route('/api/data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM login_log;')
    messages = cursor.fetchall()
    cursor.close()
    conn.close()
    
    # Format the data
    formatted_messages = [{'id': msg[0], 'message': msg[1]} for msg in messages]
    return jsonify(formatted_messages)

@app.route('/api/data', methods=['POST'])
def post_data():
    new_message = request.json.get('message')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO messages (message) VALUES (%s) RETURNING id;', (new_message,))
    message_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({"message": "Data added successfully!", "id": message_id}), 201

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=5000) # to make it accessible externally.
    #app.run(debug=True, port=5000)  # Run the app with debug mode and port 5000
    app.run(debug=True,host='0.0.0.0')  # Run the app with debug mode and port 5000