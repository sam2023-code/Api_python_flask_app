from flask import Flask, jsonify, request
from database_connect import get_db_connection  # Import the database connection function


def api_employees_get_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('select id, first_name as firstName, last_name as lastName from employees ;')
    messages = cursor.fetchall()
    cursor.close()
    conn.close()
    
    # Format the data
    formatted_messages = [
            {'id': msg[0]
            , 'firstName': msg[1]
            , 'lastName': msg[2]
            } for msg in messages]
    return jsonify(formatted_messages)

def api_employees_get_data_by_id(id):

    int_var_id = id
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, first_name, last_name FROM employees WHERE id = %s', (int_var_id,))
    employee = cursor.fetchone()
    cursor.close()
    conn.close()
   
    if employee is None:
        return jsonify({'error': 'Employee not found'}), 404

    # Format the data, since employee is a single tuple
    formatted_messages = {
        'id': employee[0],
        'firstName': employee[1],
        'lastName': employee[2]
    }
    return jsonify(formatted_messages)


def api_employees_post_data(data):
    # Extract data from the request
    firstName = request.json.get('firstName')
    lastName = request.json.get('lastName')

    if not firstName or not lastName:
        return jsonify({"error": "firstName and lastName are required!"}), 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO employees (first_name, last_name) VALUES (%s,%s) RETURNING id;', (firstName,lastName))
    message_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({"message": "Data added successfully!", "id": message_id}), 201


def api_employees_delete_data_by_id(id):

    int_var_id = id
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Check if the employee exists
    cursor.execute('SELECT * FROM employees WHERE id = %s', (int_var_id,))
    employee = cursor.fetchone()
    
    if employee is None:
        return jsonify({'error': 'Employee not found'}), 404
    
    # Delete the employee
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM employees WHERE id = %s', (int_var_id,))
    conn.commit()
    cursor.close()
    conn.close()
   
    # Format the data, since employee is a single tuple
    return jsonify({'message': 'Employee deleted successfully'}), 200