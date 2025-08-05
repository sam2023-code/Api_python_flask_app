from flask import Flask, jsonify, request
from twilio.rest import Client

def twilio_send_sms(data):

    from_phone = "+17622499901"
    #from_whatsapp = "whatsapp:" + "+14155238886"
    sms_token = request.json.get('json_token')
    sms_phone = request.json.get('json_phone')
    sms_content = request.json.get('json_content')

    #return message.sid
    if sms_token != "sam240423" :
        return jsonify({"error": "Token not match!"}), 400


    # Your Account SID and Auth Token from twilio.com/console
    account_sid = 'ACbce8410561ad8b6f314e7056e19020a0'
    auth_token = 'ffda275dd92b634e291d29ff7e9098a0'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_=from_phone,
        body=sms_content,
        to= sms_phone
        #to='+85296324758'
    )

    #return message.sid
    return jsonify({"message": "SMS sendout successfully!", "id": message.sid}), 201
