import json
from flask import request

from .models import Message
from . import api
from .events import send_message


# REST API TO send message and retrieve message history
@api.route('/messages', methods=['GET'])
def get_messages():
    msg_qs = Message.query.order_by(Message.created_at)
    messages = [msg.to_dict() for msg in msg_qs.all()]
    return {'messages': messages}, 200


@api.route('/messages', methods=['POST'])
def post():
    data = json.loads(request.data)
    if 'message' not in data:
        return {'error': 'invalid parameter'}, 400
    print('save message %s', data['message'])
    send_message(data)
    return {'message': 'message sent'}, 200
