from dotenv import load_dotenv
load_dotenv()

from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()


account_sid = 'ACafe016a96302db453e919120302b2d40'
auth_token = '67e89101f2020e50258e8bbe7b6ce58c'
client = Client(account_sid, auth_token)


def send_message(to: str, message: str) -> None:
    print(message)
    print(to)
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body= message,
            to=to
        )
        print("oyee4")
    except Exception as inst:
        # print(message)
        print(type(inst))
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body= "twillo exception",
            to=to
        )
        # message = client.messages.create(
        #     from_='whatsapp:+14155238886',
        #     body= message1[1],
        #     to=to
        # )
        print("oyee5")