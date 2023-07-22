from helper.openai_api import text_complition
from helper.twilio_api import send_message
from flask import Flask, request
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
texts = [{"id": 2001,"phone_number": "whatsapp:+916386098082","name": "Aryan","health_condition":"Diabetes"},
        {"id": 2002,"phone_number": "whatsapp:+916386098082","name": "Aman","health_condition":"Thyroid"}]



@app.route('/')
def home():
    return 'Successfully Working!'


print('oye0')


@app.route('/twilio/receiveMessage', methods=['POST'])
def receiveMessage():
    try:
        # Extract incoming parameters from Twilio
        name = None
        disease = None
        message = request.form['Body']
        sender_id = request.form['From']
        print("oyee2")
        for text in texts:
            print(text)
            print(text['id'])
            if(str(text['id']) == message):
                name = text["name"]
                disease = text["health_condition"]
                print(name,disease)
                break
        else:
            send_message(sender_id, "Wrong Id")
            return 'Ok', 200
        
        print('oye2')
        # Get response from Openai
        result = text_complition(name,disease)
        if result['status'] == 1:
            print('oye3')
            send_message(sender_id, result['response'])
    except:
        pass
    return 'OK', 200
