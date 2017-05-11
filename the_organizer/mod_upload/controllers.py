# Import flask dependencies
from flask import Blueprint, request, render_template
from flask import session as login_session


# Import the database object from the main app module
from app import db

# Import module forms
from app.mod_auth.forms import LoginForm

# Import module models (i.e. User)
from app.mod_auth.models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_items = Blueprint('items', __name__, url_prefix='/items')

# Set the route and accepted methods


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        # f.save('uploads/' + secure_filename(f.filename))
        folder_id = '0BwwA4oUTeiV1TGRPeTVjaWRDY1E'
        file_metadata = {
            'name': 'photo.jpg',
            'parents': '0BzR8CQ8uVXjiS1N2dFRVXzBNRWc'
        }
        media = MediaFileUpload('files/photo.jpg',
                                mimetype='image/jpeg',
                                resumable=True)
        file = drive_service.files().create(body=file_metadata,
                                            media_body=media,
                                            fields='id').execute()
        print 'File ID: %s' % file.get('id')

    else:
        return "Please Upload Something"
