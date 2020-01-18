from flask import abort

from . import db
from .utils import timestamp


class Message(db.Model):
    """The Message model."""
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.Integer, default=timestamp)
    message = db.Column(db.Text, nullable=False)

    @staticmethod
    def create(data):
        """Create a new message"""
        msg = Message()
        msg.from_dict(data)
        db.session.add(msg)
        db.session.commit()
        return msg

    def from_dict(self, data):
        """Import message data from a dictionary."""
        for field in ['message']:
            try:
                setattr(self, field, data[field])
            except KeyError:
                abort(400)

    def to_dict(self):
        """Export message to a dictionary."""
        return {
            'id': self.id,
            'created_at': self.created_at,
            'message': self.message
        }
