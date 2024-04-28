from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import os
import re

app4 = Flask(__name__)
app4.secret_key = 'your_secret_key'

# MySQL Configuration
app4.config['MYSQL_HOST'] = 'localhost'  # MySQL host (change if your MySQL server is hosted elsewhere)
app4.config['MYSQL_USER'] = 'root'  # MySQL username
app4.config['MYSQL_PASSWORD'] = '1234@'  # MySQL password
app4.config['MYSQL_DB'] = 'kaushtubha'  # MySQL database name

mysql = MySQL(app4)

@app4.route('/')
def profile():
    return render_template('profile.html')

if __name__ == "__main__":
    app4.run(port=2001, debug=True)