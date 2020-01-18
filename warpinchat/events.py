from . import socketio
from .models import Message


@socketio.on('send_message')
def send_message(data):
    # store message to db
    Message.create(data)
    socketio.emit('my event', data, broadcast=True)


@socketio.on('subscribe')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my event', json['message'])
