import json
import unittest

from warpinchat import create_app, db, socketio


class FlackTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')

        self.ctx = self.app.app_context()
        self.ctx.push()
        db.drop_all()  # just in case
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.drop_all()
        self.ctx.pop()

    def get_headers(self):
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        return headers

    def get(self, url):
        rv = self.client.get(url,
                             headers=self.get_headers())
        # clean up the database session, since this only occurs when the app
        # context is popped.
        db.session.remove()
        body = rv.get_data(as_text=True)
        if body is not None and body != '':
            try:
                body = json.loads(body)
            except Exception:
                pass
        return body, rv.status_code, rv.headers

    def post(self, url, data=None):
        d = data if data is None else json.dumps(data)
        rv = self.client.post(url, data=d, headers=self.get_headers())
        # clean up the database session, since this only occurs when the app
        # context is popped.
        db.session.remove()
        body = rv.get_data(as_text=True)
        if body is not None and body != '':
            try:
                body = json.loads(body)
            except Exception:
                pass
        return body, rv.status_code, rv.headers

    def test_message(self):
        # create a message
        r, s, h = self.post(
            '/api/messages',
            data={'message': 'hello *world*!'}
        )
        self.assertEqual(s, 200)

        # create incomplete message
        r, s, h = self.post('/api/messages', data={'foo': 'hello *world*!'})
        self.assertEqual(s, 400)

        # retrieve messages history
        r, s, h = self.get('/api/messages')
        self.assertEqual(s, 200)
        self.assertEqual(len(r['messages']), 1)

    def test_socketio(self):
        client = socketio.test_client(self.app)

        # clear old socket.io notifications
        client.get_received()

        # post a message via socketio
        client.emit('send_message', {'message': 'foo'})
        recvd = client.get_received()
        self.assertEqual(len(recvd), 1)
        self.assertEqual(recvd[0]['args'][0]['message'], 'foo')
        self.assertEqual(recvd[0]['name'], 'my event')
        self.assertEqual(recvd[0]['namespace'], '/')

        # disconnect the user
        client.disconnect()
        with self.assertRaises(RuntimeError):
            recvd = client.get_received()
