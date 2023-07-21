from helper.openai_api import text_complition
from helper.twilio_api import send_messag
from flask import Flask, request
from dotenv import load_dotenv 
load_dotenv()

app = Flask(__name__)


@app.route('/handle_data', methods=['POST'])
def home():
    projectpath = request.form['projectFilepath']
print('oye0')

# @app.route('/twilio/receiveMessage', methods=['POST'])
# def receiveMessage():
#     try:
#         # Extract incoming parameters from Twilio
#         message = request.form['Body']
#         print('oye1')
#         sender_id = request.form['From']
#         print('oye2')

#         # Get response from Openai
#         result = text_complition(message)
#         if result['status'] == 1:
#             print('oye3')
#             send_message(sender_id, result['response'])
#     except:
#         pass
    # return 'OK', 200
