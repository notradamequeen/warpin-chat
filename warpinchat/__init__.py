import os

from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

from config import config

# Flask extensions
db = SQLAlchemy()
socketio = SocketIO()
api = Blueprint('api', __name__)

# Import models so that they are registered with SQLAlchemy
from . import models  # noqa
# Import Socket.IO events so that they are registered with Flask-SocketIO
from . import events  # noqa


def create_app(config_name=None, main=True):
    if config_name is None:
        config_name = os.environ.get('FLACK_CONFIG', 'development')
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize db
    db.init_app(app)
    if main:
        # Initialize socketio server
        # Socket.IO
        socketio.init_app(app)

    # Register web application routes
    from .flack import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Register API routes
    from .views import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
