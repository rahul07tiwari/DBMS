from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'  # MySQL host (change if your MySQL server is hosted elsewhere)
app.config['MYSQL_USER'] = 'root'  # MySQL username
app.config['MYSQL_PASSWORD'] = '1234@'  # MySQL password
app.config['MYSQL_DB'] = 'kaushtubha'  # MySQL database name

mysql = MySQL(app)

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/Rooms')
def Rooms():
    return render_template('HTML/Rooms.html')

@app.route('/Facilities')
def Facilities():
    return render_template('HTML/Facilities.html')

@app.route('/Contact')
def Contact():
    return render_template('HTML/Contact.html')

@app.route('/About')
def About():
    return render_template('HTML/About.html')

if __name__ == "__main__":
    app.run(port=5000, debug=True)

