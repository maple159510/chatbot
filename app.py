import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine

from transitions import State

from transitions.extensions import GraphMachine as Machine

API_TOKEN = '519466420:AAEqkUKvoHwqHCAcmSVN6zQmRk-TY4YPid0'
WEBHOOK_URL = 'https://f9fcd1c9.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'state1',
        'state2',
        'state3',
        'state4'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state4',
            'conditions': 'is_going_to_state4'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state1',
                'state2',
                'state3',
                'state4'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    print(update.message.text)
    if update.message.text != '':
        update.message.reply_text('Hello!\nThis is the Go-bot.\nIf you want to answer a question about Basic Problem--SET, please type "play a".\nIf you want to answer a question about Technical Problem--EAT, please type "play b".\nIf you want to answer a question about Technical Problem--BROKE EYE, please type "play c".\nIf you want to answer a question about Advanced Problem--DEATH LIVE, please type "play d".\n')
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
    machine.graph.draw('fsm.png',prog = 'dot')
