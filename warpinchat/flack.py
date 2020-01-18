from flask import Blueprint, render_template


main = Blueprint('main', __name__)


@main.route('/')
def session():
    """Serve client-side application."""
    return render_template('session.html')
