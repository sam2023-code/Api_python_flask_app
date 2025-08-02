from flask import Flask, jsonify, request
from database_connect import get_db_connection  # Import the database connection function


def api_login_auth_post_check(data):
    # Extract data from the request
    login_user = request.json.get('username')
    login_pass = request.json.get('password')

    if login_user == "jason" and login_pass == "20240423":
        func_loginlog_insert(login_user,"user")
        return jsonify({'message': 'Login successfully'}), 200
    
    elif login_user == "admin" and login_pass == "pass":
        func_loginlog_insert(login_user,login_user)
        return jsonify({'message': 'Login successfully'}), 200
    
    else:
        # Display an error message
        return jsonify({"error": "Login fail, username / password invalid."}), 400


def func_loginlog_insert(v_username, v_usertype):
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO login_log (username, usertype) VALUES (%s,%s) RETURNING id;', (v_username,v_usertype))
    message_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    
