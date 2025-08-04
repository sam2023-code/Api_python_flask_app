from flask import Flask, jsonify, request
from database_connect import get_db_connection  # Import the database connection function

#from flask_cors import CORS
#app = Flask(__name__, template_folder='templates')  # Ensure this line exists
#CORS(app, resources={r"*": {"origins": "*"}})

def api_messageboard_get_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('select * from messageboard ;')
    messages = cursor.fetchall()
    cursor.close()
    conn.close()
    
    # Format the data
    formatted_messages = [
            {'id': msg[0]
            , 'content': msg[1]
            , 'timestamp': msg[2]
            , 'taskfinish': msg[3]
            } for msg in messages]
    return jsonify(formatted_messages)


def api_messageboard_post_data(data):
    # Extract data from the request
    msg_content = request.json.get('content')

    if not msg_content :
        return jsonify({"error": "content are required!"}), 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO messageboard (content) VALUES (%s) RETURNING id;', (msg_content , ))
    message_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({"message": "Data added successfully!", "id": message_id}), 201


def api_messageboard_update_status_by_id(id , taskfinish):

    msg_id = id
    msg_taskfinish = taskfinish

    print(msg_id)  
    print(msg_taskfinish)  

    if not msg_taskfinish :
        return jsonify({"error": "content are required!"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Check if the message_to_be_update exists
    cursor.execute('SELECT * FROM messageboard WHERE id = %s', (msg_id,))
    message_to_be_update = cursor.fetchone()
    
    if message_to_be_update is None:
        return jsonify({'error': 'message not found'}), 404
    
    # Delete the message
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE messageboard SET taskfinish = %s WHERE id = %s', (msg_taskfinish , msg_id ))
    conn.commit()
    cursor.close()
    conn.close()
   
    # Format the data, since message_to_be_update is a single tuple
    return jsonify({'message': 'Message updated successfully'}), 200

def api_messageboard_delete_data_by_id(id):

    int_var_id = id
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Check if the message_to_be_delete exists
    cursor.execute('SELECT * FROM messageboard WHERE id = %s', (int_var_id,))
    message_to_be_delete = cursor.fetchone()
    
    if message_to_be_delete is None:
        return jsonify({'error': 'message not found'}), 404
    
    # Delete the message
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM messageboard WHERE id = %s', (int_var_id,))
    conn.commit()
    cursor.close()
    conn.close()
   
    # Format the data, since message_to_be_delete is a single tuple
    return jsonify({'message': 'Message deleted successfully'}), 200