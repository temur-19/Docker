import requests

def send_telegram_message(message, TOKEN, chat_id):
    url  = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&test={message}'
    payload = {
        'chat_id':chat_id,
        'text':message
    }
    r = requests.post(url, data = payload)
    return r.json()


message = 'Hello world'
TOKEN = '8708774823:AAEdn0E09ajJl_4a9rCB3rOxaKJkhlo5zq4'
chat_id = '5790237488'
print(send_telegram_message(message, TOKEN, chat_id))
