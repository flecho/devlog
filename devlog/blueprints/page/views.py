'''
    
    Tips:
    A `Blueprint` object works similarly to a `Flask` application object,
    but it is not actually an application.
'''
from flask import Blueprint, render_template, current_app
import mistune

page = Blueprint('page', __name__,
                 template_folder='templates')


def get_markdown_files():
    """ I would like to view mark down languages."""
    pass

def get_markdown_file():
    # If you care about performance, it is better to re-use the Markdown instance
    import os
    file_path = os.path.join(current_app.instance_path, 'uploads', 'jinja2.md')
    markdown = None
    renderer = mistune.Renderer(escape=True, hard_wrap=True)
    markdown = mistune.Markdown(renderer=renderer)
    with open(file_path, 'rt') as f:
        result = markdown(f.read().decode('utf-8'))
    return result

@page.route("/")
def home():
    # return "Hello, World!"
    markdown_file = get_markdown_file()
    return render_template('page/home.html', welcome_msg="Hello, World!", markdown_file=markdown_file)
