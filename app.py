from flask import Flask , render_template ,request,jsonify
import firebase_admin
from firebase_admin import credentials, auth, firestore

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)
firebaseConfig = {
  'apiKey': "AIzaSyAGEj-3FnOTx9XFygjcZ5XrhPje2mY4w7s",
  'authDomain': "seeker-aa1ec.firebaseapp.com",
  'databaseURL': "https://seeker-aa1ec-default-rtdb.firebaseio.com",
  'projectId': "seeker-aa1ec",
  'storageBucket': "seeker-aa1ec.firebasestorage.app",
  'messagingSenderId': "42245521307",
  'appId': "1:42245521307:web:963e794ad242509d5feb3e",
  'measurementId': "G-54VQX6D9X0"
};
app = Flask(__name__)
db = firestore.client()

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/dark.html')
def dark():
    return render_template('dark.html')
@app.route('/signin.html',methods=["GET", "POST"])
def signin_page():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        try:
            user = auth.get_user_by_email(email)  # Example: Firebase check
            # You might need to verify password here using Firebase
            # If successful:
            return render_template('/')  # redirect to your index page
        except:
            flash("Invalid credentials. Try again.")
            return redirect(url_for("signin"))

    return render_template("signin.html")
@app.route('/signup.html')
def signup():
    return render_template('signup.html')
@app.route('/darksignin.html')
def darksign():
    return render_template('darksignin.html')
@app.route('/darksignup.html')
def darkup():
    return render_template('darksignup.html')
@app.route('/about.html')
def about():
    return render_template('about.html')
@app.route('/darkabout.html')
def darkabout():
    return render_template('darkabout.html')
@app.route('/privacy.html')
def privacy():
    return render_template('privacy.html')
@app.route('/priv_D.html')
def priv_D():
    return render_template('priv_D.html')
if __name__ == '__main__':
    app.run(debug=True)
