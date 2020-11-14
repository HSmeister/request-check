import requests
import os
import logging
import time

from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
FROM_NUM = os.getenv('FROM_NUMBER')
TO_NUM = os.getenv('TO_NUMBER')
TIME_DELAY = 60

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

logging.basicConfig(
    filename='requesting.log',
    level=logging.INFO
    )


def send_sms(message):
    message = client.messages.create(
        body=message,
        from_=FROM_NUM,
        to=TO_NUM,
       )


while True:
    try:
        answer = requests.get('https://httpstat.us/404').raise_for_status()
        logging.info(answer.status_code)
        time.sleep(TIME_DELAY)
    except:
        message = f'Сервис недоступен.\
             Повторю попытку через {TIME_DELAY} секунд'
        logging.error(message)
        send_sms(message)
        time.sleep(TIME_DELAY)
