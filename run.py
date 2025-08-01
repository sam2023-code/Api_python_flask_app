from flask import Flask,render_template, jsonify, request
import psycopg2
from psycopg2 import sql
from database_connect import get_db_connection  # Import the database connection function
from api_loginlog import api_loginlog_get_data , api_loginlog_post_data  # Import the function from aaa.py

app = Flask(__name__, template_folder='templates')  # Ensure this line exists

@app.route('/')
def home():
    return render_template('index.html')  # Ensure this template exists

@app.route('/api/test', methods=['GET'])
def get_test():
    data = {"message": "Hello, World!","status": "success"}
    return jsonify(data)

@app.route('/api/data', methods=['GET'])
def data_loginlog_get():
    return api_loginlog_get_data() 

@app.route('/api/data', methods=['POST'])
def data_loginlog_post():
    return api_loginlog_post_data(request.json)


if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=5000) # to make it accessible externally.
    #app.run(debug=True, port=5000)  # Run the app with debug mode and port 5000
    app.run(debug=True,host='0.0.0.0')  # Run the app with debug mode and port 5000