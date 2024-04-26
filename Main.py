from flask import Flask, render_template, request, redirect, session, flash, jsonify
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'  # MySQL host (change if your MySQL server is hosted elsewhere)
app.config['MYSQL_USER'] = 'root'  # MySQL username
app.config['MYSQL_PASSWORD'] = '1234@'  # MySQL password
app.config['MYSQL_DB'] = 'kaushtubha'  # MySQL database name

mysql = MySQL(app)

# Configure file upload
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# Create the upload directory if it doesn't exist
upload_dir = app.config['UPLOAD_FOLDER']
if not os.path.exists(upload_dir):
    os.makedirs(upload_dir)

# Function to check if file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Function to validate PIN code
def validate_pincode(pincode):
    return len(pincode) == 6 and pincode.isdigit()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data from the modal
        name = request.form['Name']
        email = request.form['Email']
        phone_number = request.form['Phone']
        address = request.form['Address']
        pincode = request.form['Pincode']
        dob = request.form['DOB']
        password = request.form['password']
        confirm_password = request.form['confirm']
        document = request.files['document']

        # Check if email or phone number already exists
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s OR phone_number = %s", (email, phone_number))
        user = cur.fetchone()
        cur.close()

        if user:
            return jsonify({'message': 'Email or phone number already exists!', 'status': 'error'})

        # Validate pincode
        if not validate_pincode(pincode):
            return jsonify({'message': 'Invalid pincode! Pincode should be a 6-digit number.', 'status': 'error'})

        # Validate password
        if password != confirm_password:
            return jsonify({'message': 'Password and confirm password do not match!', 'status': 'error'})

        # Securely save the document
        if document and allowed_file(document.filename):
            filename = secure_filename(document.filename)
            document_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            document.save(document_path)
        else:
            return jsonify({'message': 'Invalid document! Please upload a valid JPG, JPEG, or PNG file.', 'status': 'error'})

        # Insert user data into database
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name, email, phone_number, address, pincode, dob, password, document_path) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                    (name, email, phone_number, address, pincode, dob, password, document_path))
        mysql.connection.commit()
        cur.close()

        return jsonify({'message': 'Registration successful!', 'status': 'success'})

    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    # Query the database to find the user with the provided email
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE email = %s", (email,))
    users = cur.fetchone()
    cur.close()

    if users:
        # Check if the provided password matches the password in the database
        if password == users['password']:
            session['users'] = email  # Start the session
            return jsonify({'status': 'success'})
    
    # If login fails, return an error response
    return jsonify({'status': 'error', 'message': 'Invalid email or password'})



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


