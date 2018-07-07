import os
from flask import (Flask, flash, render_template,
                   url_for)
from upload import upload_page

def create_app():
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)
    # The behavior of relative paths in config files can be flipped between "relative to the application root" (the default)
    # to "relative to instance folder" via the instance_relative_config switch to the application constructor

    app.config.from_object('config.settings')  # should use this function to load the default setting.
    app.config.from_pyfile('settings.py', silent=True)  # the default setting can be overriden by instance/settings.py
    app.register_blueprint(upload_page)

    @app.route("/")
    def index():
        return "Hello, World!"
    # It is declared, but not used.

    @app.route("/markdown/<name>")
    def markdown(name=None):
        return render_template('', name=name)

    return app
# Have to make api that stores the received `.md` file to `temp` directory.


