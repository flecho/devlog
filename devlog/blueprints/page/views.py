'''
    
    Tips:
    A `Blueprint` object works similarly to a `Flask` application object,
    but it is not actually an application.
'''
from flask import Blueprint

page = Blueprint('page', __name__,
                 template_folder='templates')

@page.route("/")
def home():
    return "Hello, World!"