from flask import Flask, request, jsonify
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.service_account import Credentials

app = Flask(__name__)

# Configura Google Drive
SCOPES = ['https://www.googleapis.com/auth/drive.file']
creds = Credentials.from_service_account_file('service_account.json', scopes=SCOPES)
service = build('drive', 'v3', credentials=creds)
FOLDER_ID = 'ID_CARTELLA_DRIVE'

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['foto']
    f.save(f.filename)
    file_metadata = {'name': f.filename, 'parents':[FOLDER_ID]}
    media = MediaFileUpload(f.filename, mimetype='image/jpeg')
    service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    return jsonify({'success': True})

