from flask import Flask, jsonify, request
from database_connect import get_db_connection  # Import the database connection function

def api_loginlog_get_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('select * from fetch_top_10_login_logs() LIMIT 20;')
    messages = cursor.fetchall()
    cursor.close()
    conn.close()
    
    # Format the data
    formatted_messages = [
            {'id': msg[0]
            , 'usrname': msg[1]
            , 'usrtype': msg[2]
            , 'datetime': msg[3]
            , 'datetime_string': msg[4]
            } for msg in messages]
    return jsonify(formatted_messages)

def api_loginlog_post_data(data):
    # Extract data from the request
    username = request.json.get('username')
    usertype = request.json.get('usertype')

    if not username or not usertype:
        return jsonify({"error": "Username and usertype are required!"}), 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO login_log (username, usertype) VALUES (%s,%s) RETURNING id;', (username,usertype))
    message_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({"message": "Data added successfully!", "id": message_id}), 201
