import os
from flask import Blueprint, request, url_for, send_from_directory, redirect, flash
from werkzeug.utils import secure_filename

upload_page = Blueprint('upload_page', __name__)

UPLOAD_FOLDER = os.path.dirname(os.path.realpath(__file__)) + '/uploads'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ('md')

def make_uploads_dir():
    """ If there is no `uploads` directory,
    create one."""
    if not os.path.isdir(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

@upload_page.route("/upload", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            make_uploads_dir()
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return redirect(url_for('upload_page.uploaded_file', filename=filename))
        
    return '''<!doctype html>
    <title>Upload your markdown file</title>
    <h1>Upload your markdown file</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@upload_page.route('/upload/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


@upload_page.route('/show')
def show_uploaded_file_list():
    """ Return a list of uploaded markdown files."""
    return str(os.listdir(UPLOAD_FOLDER))
    

    
    