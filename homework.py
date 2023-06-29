import os
import time
import requests
from dotenv import load_dotenv
from twilio.rest import Client


def get_status(user_id):
    load_dotenv()
    token = os.getenv('Token')
    params = {
        'user_ids': user_id,
        'v': '5.131',
        'access_token': token,
        'fields': 'online',
    }
    url = 'https://api.vk.com/method/users.get'
    r = requests.get(url, params=params).json()['response'][0]
    return r.get('online')


def sms_sender(sms_text):
    load_dotenv()
    number_from = os.getenv('NUMBER_FROM')
    number_to = os.getenv('NUMBER_TO')
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=sms_text,
        from_=number_from,
        to=number_to
    )
    return message.sid


if __name__ == "__main__":
    vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
