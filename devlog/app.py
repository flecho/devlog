import os
from flask import (Flask, flash, render_template,
                   url_for)
from upload import upload_page

app = Flask(__name__)  # An instance of this class will be our WSGI application.
app.register_blueprint(upload_page)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/markdown/<name>")
def markdown(name=None):
    return render_template('', name=name)

# Have to make api that stores the received `.md` file to `temp` directory.


