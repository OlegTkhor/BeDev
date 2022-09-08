from urllib import request
import requests
import time

Bot_Name= 't.me/Neural11_bot'
TOKEN = "5487238269:AAE-FeV0Dz6cZwtQoNeyTCqKTfheWjwjCAM"
ROOT_URL = f'https://api.telegram.org/bot{TOKEN}/'
sentences = [

    {"text": "When my time comes \n Forget the wrong that I’ve done.",

     "level": 1},

    {"text": "In a hole in the ground there lived a hobbit.",

     "level": 2},

    {"text": "The sky the port was the color of television, tuned to a dead channel.",

     "level": 1},

    {"text": "I love the smell of napalm in the morning.",

     "level": 0},

    {"text": "The man in black fled across the desert, and the gunslinger followed.",

     "level": 0},

    {"text": "The Consul watched as Kassad raised the death wand.",

     "level": 1},

    {"text": "If you want to make enemies, try to change something.",

     "level": 2},

    {"text": "We're not gonna take it. \n Oh no, we ain't gonna take it \nWe're not gonna take it anymore",

     "level": 1},

    {"text": "I learned very early the difference between knowing the name of something and knowing something.",

     "level": 2}

]

def get_update(url):
    url += 'getUpdates'
    request = requests.get(url)
    result = request.json()['result']
    update = dict()
    if len(result) > 0:
        for chunk in result:
            update_id = chunk.get('update_id')
            message = chunk.get('message')
            if message:
                message_id = message.get('message_id')
                message_from = message.get('from')
                message_chat = message.get('chat')
                chat_id = message_chat.get('id')
                text = message.get('text')
                update[chat_id] = text,message_id
    return update
def send_message(url, chat_id, text=''):
    url += 'sendMessage'
    request = requests.post(url, {'chat_id': chat_id, 'text': text})


def one_liner(sentenses, word,level):
    return "\n...\n".join([x['text'].lower() for x in sentenses if (word.lower() in x['text'].lower()) and (x['level'] == level) ]) or 'Nothing has been found'

while True:
    update = get_update(url=ROOT_URL)
    time.sleep(3)
    print(update)