import requests
import os

from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

#Константы
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
FROM_NUM = os.getenv('FROM_NUM')
TO_NUM = os.getenv('TO_NUM')
TIME_DELAY = 60
#Константы



answer = requests.get('https://httpstat.us/200')
print(answer.raise_for_status())

def send_sms(message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        body=message,  # текст сообщения
        from_=FROM_NUM,  # номер, который был получен
       to=TO_NUM,  # твой номер, на который придёт sms
       )


