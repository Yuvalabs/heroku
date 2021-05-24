import pyrebase

config = {
    "apiKey": "AIzaSyB_k9SPujVHdm-8EHwuy9OQU1AEAhBA4Ro",
    "authDomain": "irisscan-94a4e.firebaseapp.com",
    "databaseURL": "https://irisscan-94a4e-default-rtdb.firebaseio.com",
    "projectId": "irisscan-94a4e",
    "storageBucket": "irisscan-94a4e.appspot.com",
    "messagingSenderId": "157605262331",
    "appId": "1:157605262331:web:9f18539654fca271a7515e",
    "measurementId": "G-BW0H8V7E2D"
}

firebase = pyrebase.initialize_app(config)

storage = firebase.storage()

auth=firebase.auth()

try:
    login = auth.sign_in_with_email_and_password("yuvalabs@gmail.com", "shambo1234&")
except:
    print("hello")

from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def basic():
    if request.method == 'POST':
        upload = request.files['upload']
        storage.child("Images/new.png").put(upload)
        return redirect(url_for('uploads'))
    return render_template('index.html')


@app.route('/uploads', methods=['GET', 'POST'])
def uploads():
    if request.method == 'POST':
        return redirect(url_for('basic'))
    if True:
        links = storage.child('Images/2.jpg').get_url(None)
        return render_template('upload.html', l=links)
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
