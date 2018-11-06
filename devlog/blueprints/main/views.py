'''
    
    Tips:
    A `Blueprint` object works similarly to a `Flask` application object,
    but it is not actually an application.
'''
from flask import Blueprint, render_template, current_app
import mistune

main = Blueprint('main', __name__,
                 template_folder='templates')


def get_markdown_files():
    """ I would like to view mark down languages."""
    pass


def get_markdown_file():
    # If you care about performance, it is better to re-use the Markdown instance
    import os    
    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'example.md')
    # whether file exists or not.
    if not os.path.isfile(file_path):
        return "No markdown file for name {} yet.".format(file_path)
    
    markdown = None
    renderer = mistune.Renderer(escape=True, hard_wrap=True)
    markdown = mistune.Markdown(renderer=renderer)
    with open(file_path, 'rt') as f:
        result = markdown(f.read())
    return result


@main.route("/")
def home():
    # return "Hello, World!"
    welcome_msg = "Welcome to devlog!"
    markdown_file = get_markdown_file()
    return render_template('main/home.html', welcome_msg=welcome_msg, markdown_file=markdown_file)
