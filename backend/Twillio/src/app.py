from helper.openai_api import text_complition,text_complete
from helper.twilio_api import send_message
from flask import Flask, request
from dotenv import load_dotenv
from src.test import msql_connection,msql_connection2
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
        sql_results = msql_connection("Select * from customer")
        for res in sql_results:
            print(res)
            print(res[0])
            if(str(res[0])==message):
                print("1")
                name = "aryan"
                disease = ""
                if res[5] != "null":
                    disease += res[5] + " "
                if res[6] != "null":
                    disease += res[6] + " "
                if res[7] != "null":
                    disease += res[7] + " "
                if res[8] != "null":
                    disease += res[8] + " "
                if res[8] != "null":
                    disease += res[9] + " " 
                if("high")in res[10]:
                    disease += "my diabetes is high" 
                if("high")in res[11]:
                    disease += "my lipids is high"  
                if("high")in res[12]:
                    disease += "thyroid is high"
                print("2")
                break
        else:
            send_message(sender_id, "Wrong Id")
            return 'Ok', 200
        
        print('oye2')
        result = text_complition(name,disease)
        if result['status'] == 1:
            print('oye3')
            send_message(sender_id, result['response'])
        result2 = text_complete(name,disease,result)
        if result2['status'] == 1:
            print('oye5')
            print(result2['response'])
            # sql_results = msql_connection2("insert into article (customer_id, article) values(" + message + "," + result2['response']+");")
            print(sql_results)
        else:
            print("No article")
    except:
        pass
    return 'OK', 200
