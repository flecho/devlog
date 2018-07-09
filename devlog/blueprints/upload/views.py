'''    
    Tips:
    A `Blueprint` object works similarly to a `Flask` application object,
    but it is not actually an application.
'''
import os
import logging
from flask import Blueprint, Flask, request, url_for, send_from_directory, redirect, flash, current_app
from flask.logging import default_handler
from werkzeug.utils import secure_filename


logger = logging.getLogger('Flask.app')
upload = Blueprint('upload', __name__,
                   template_folder='templates')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ('md')

def make_uploads_dir(upload_path):
    """ If there is no `uploads` directory,
    create one."""
    if not os.path.isdir(upload_path):
        os.makedirs(upload_path)

@upload.route("/upload", methods=['GET', 'POST'])
def upload_file():
    upload_path = os.path.join(current_app.instance_path, 'uploads')
 
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
            logger.info('upload_path: ' + upload_path)
            filename = secure_filename(file.filename)
            make_uploads_dir(upload_path)
            file.save(os.path.join(upload_path, filename))
            logger.info('file_save is done')
            return "Completed!"
#            return redirect(url_for('upload.uploaded_file', filename=filename))
        
    return '''<!doctype html>
    <title>Upload your markdown file</title>
    <h1>Upload your markdown file</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@upload.route('/upload/<filename>')
def uploaded_file(filename):
    upload_path = os.path.join(current_app.instance_path, 'uploads')
    return send_from_directory(upload_path, filename)


@upload.route('/show')
def show_uploaded_file_list():
    """ Return a list of uploaded markdown files."""
    return str(os.listdir(''))
    