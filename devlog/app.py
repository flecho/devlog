import os
from flask import Flask
from flask_bootstrap import Bootstrap
from .blueprints.upload import upload
from .blueprints.page import page
from .blueprints.about import about


def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)
    Bootstrap(app)
    # The behavior of relative paths in config files can be flipped between "relative to the application root" (the default)
    # to "relative to instance folder" via the instance_relative_config switch to the application constructor

    app.config.from_object('config.settings')  # should use this function to load the default setting.
    app.config.from_pyfile('settings.py', silent=True)  # the default setting can be overriden by instance/settings.py

    if settings_override:
        app.config.update(settings_override)

    app.register_blueprint(upload)
    app.register_blueprint(about)
    app.register_blueprint(page)

    upload.path = os.path.join(app.instance_path, 'uploads')

    return app
