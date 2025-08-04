from flask import Flask,render_template, jsonify, request
from flask_cors import CORS
import psycopg2
from psycopg2 import sql
from database_connect import get_db_connection  # Import the database connection function
from api_loginlog import api_loginlog_get_data , api_loginlog_post_data,api_loginlog_post_data_visitor  # Import the function from aaa.py
from api_employees import api_employees_get_data,api_employees_get_data_by_id , api_employees_post_data, api_employees_delete_data_by_id
from api_messageboard import api_messageboard_get_data,api_messageboard_post_data,api_messageboard_update_status_by_id,api_messageboard_delete_data_by_id
from api_login_auth import api_login_auth_post_check

app = Flask(__name__, template_folder='templates')  # Ensure this line exists
#CORS(app, resources={r"/api/*": {"origins": "*"}})
CORS(app, resources={r"*": {"origins": "*"}})
app.json.sort_keys = False # dont want to sort the json column name

@app.route('/')
def home():
    return render_template('index.html')  # Ensure this template exists

@app.route('/api_list')
def api_list():
    return render_template('api_list.html')  # Ensure this template exists
    #home_page = str(request.base_url).replace(str(request.path),"")

@app.route('/api/test', methods=['GET'])
def get_test():
    data = {"message": "Hello, World!","status": "success"}
    return jsonify(data)

@app.route('/api/login-logs/top10', methods=['GET'])
def data_loginlog_get():
    return api_loginlog_get_data() 

@app.route('/api/login-logs', methods=['POST'])
def data_loginlog_post():
    return api_loginlog_post_data(request.json)

@app.route('/api/login-logs/visitor', methods=['POST'])
def data_loginlog_post_visitor():
    return api_loginlog_post_data_visitor(request.json)


@app.route('/users', methods=['GET'])
def data_employees_get():
    return api_employees_get_data() 

@app.route('/users/<int:id>', methods=['GET'])
def data_employees_get_by_id(id):
    return api_employees_get_data_by_id(id)

@app.route('/users', methods=['POST'])
def data_employees_post():
    return api_employees_post_data(request.json) 

@app.route('/users/delete_user/<int:id>', methods=['DELETE'])
def data_employees_delete_by_id(id):
    return api_employees_delete_data_by_id(id)

@app.route('/api/messages', methods=['GET'])
def data_messageboard_get():
    return api_messageboard_get_data() 

@app.route('/api/messages', methods=['POST'])
def data_messageboard_post():
    return api_messageboard_post_data(request.json) 

@app.route('/api/messages/<int:id>', methods=['PUT'])
def data_messageboard_update(id):
    api_taskfinish = request.json.get('taskfinish')
    return api_messageboard_update_status_by_id(id, api_taskfinish) 

@app.route('/api/messages/<int:id>', methods=['DELETE'])
def data_messageboard_delete_by_id(id):
    return api_messageboard_delete_data_by_id(id)

@app.route('/api/auth/login', methods=['POST'])
def data_login_post():
    return api_login_auth_post_check(request.json) 

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=5000) # to make it accessible externally.
    app.run(debug=True,host='0.0.0.0')  # Run the app with debug mode and port 5000
    #context = (r'ssl/cert.pem', r'ssl/key.pem')
    #app.run(host="0.0.0.0", port=8443, ssl_context=context)