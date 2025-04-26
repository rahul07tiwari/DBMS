from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import os
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'  # MySQL host (change if your MySQL server is hosted elsewhere)
app.config['MYSQL_USER'] = 'root'  # MySQL username
app.config['MYSQL_PASSWORD'] = '1234@'  # MySQL password
app.config['MYSQL_DB'] = 'kaushtubha'  # MySQL database name

mysql = MySQL(app)

# Function to validate email format
def validate_email(email):
    return re.match(r'^[\w\.-]+@[\w\.-]+$', email)

# Function to validate mobile number format
def validate_phone_number(phone_number):
    return re.match(r'^\d{10}$', phone_number)

# Function to validate pincode format
def validate_pincode(pincode):
    return re.match(r'^\d{6}$', pincode)

# Function to check if file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')
'''
@app.route('/availability', methods=['POST'])

def availability():
    check_in = request.form['check_in']
    check_out = request.form['check_out']
    guests = request.form['guests']

    # Redirect to rooms page with query parameters
    return redirect(url_for('rooms', check_in=check_in, check_out=check_out, guests=guests))
'''
@app.route('/Rooms')
def Rooms():
    return render_template('HTML/Rooms.html')

@app.route('/booking', methods=['GET','POST'])
def booking():
     if request.method == 'POST':
        if session.get('loggedin'):
            Name = request.form['name']
            Email = request.form['email_id']
            Phone_number = request.form['phone_no']
            Room_id = request.form['room_id']
            Address = request.form['address']
            Pincode = request.form['pincode']
            No_of_Guests= request.form['No_of_guests']
            check_in = request.form['check_in']
            check_out = request.form['check_out']
            Date = request.form['res_date']
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT COUNT(*) AS count FROM users WHERE name = %s AND email = %s AND phone_number = %s AND address = %s AND pincode = %s",
               (Name, Email, Phone_number, Address, Pincode))

    
             # Fetch the result
            result = cursor.fetchone()
            count = result[0]

            # Check if a record with the same details exists
            if count > 0:
                cursor.execute("INSERT INTO reservation (name, email_id,  phone_no, room_id, address, pincode, No_of_guests, check_in, check_out, res_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (Name, Email, Phone_number, Room_id, Address, Pincode, No_of_Guests, check_in, check_out, Date, ))
                #cursor.execute("INSERT INTO reservation (user_id) SELECT user_id FROM users WHERE email = %s", (Email,))

                mysql.connection.commit()
                cursor.close()
                message = 'Booking Successfull'
                return render_template('Index.html')
            else:
                flash("No record with the same details exists. Do not proceed with booking.")
                redirect(url_for('booking'))
     else:
         return render_template('Booking.html')
    
'''
@app.route('/filter_rooms')
def filter_rooms():
    check_in = request.args.get('check_in')
    check_out = request.args.get('check_out')
    guests = request.args.get('guests')

    filtered_rooms = [] 
    return render_template('room_cards.html', filtered_rooms=filtered_rooms)
'''
@app.route('/Facilities')
def Facilities():
    return render_template('HTML/Facilities.html')

@app.route('/Contact')
def Contact():
    return render_template('HTML/Contact.html')

@app.route('/message', methods=['POST'])
def message():
    if request.method == 'POST':
        if session.get('loggedin'):
            Name = request.form['name']
            Email = request.form['email']
            Subject = request.form['subject']
            Message = request.form['message']

            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO Contact (name, email, subject, message) VALUES (%s, %s, %s, %s)",
                    (Name, Email, Subject, Message))
            mysql.connection.commit()
            cur.close()
            message = 'Message Sent Successfully'
            return render_template('HTML/Contact.html', message=message)
        else:
            return redirect(url_for('login'))
    else:
        return render_template('contact.html')
    
@app.route('/About')
def About():
    return render_template('HTML/About.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['Name']
        email = request.form['Email']
        phone_number = request.form['Phone']
        address = request.form['Address']
        pincode = request.form['Pincode']
        dob = request.form['DOB']
        password = request.form['password']
        confirm_password = request.form['confirm']
        document = request.files['document']

        # Check if email already exists
        # Simulate the database check
        def email_already_exists():
            if email_already_exists(email):
                flash('Email already registered', 'error')
                return redirect(url_for('register'))

        # Check if mobile number already exists
        # Simulate the database check
        def phone_number_already_exists():
            if phone_number_already_exists(phone_number):
                flash('Mobile number already registered', 'error')
                return redirect(url_for('register'))

        # Validate pincode
        if not validate_pincode(pincode):
            flash('Invalid pincode! Pincode should be a 6-digit number.', 'error')
            return redirect(url_for('register'))

        # Validate mobile number
        if not validate_phone_number(phone_number):
            flash('Invalid mobile number! Mobile number should be a 10-digit number.', 'error')
            return redirect(url_for('register'))

        # Validate email format
        if not validate_email(email):
            flash('Invalid email format!', 'error')
            return redirect(url_for('register'))

        # Validate password and confirm password
        if password != confirm_password:
            flash('Password and confirm password do not match!', 'error')
            return redirect(url_for('register'))

        # Validate document file
        if not allowed_file(document.filename):
            flash('Invalid document! Please upload a valid JPG, JPEG, or PNG file.', 'error')
            return redirect(url_for('register'))

        # Save the document file
        uploads_dir = 'picture/uploads'
        app.config['UPLOAD_FOLDER'] = uploads_dir

        # Create the uploads directory if it doesn't exist
        if not os.path.exists(uploads_dir):
            os.makedirs(uploads_dir)

        document_filename = secure_filename(document.filename)
        document_path = os.path.join(uploads_dir, document_filename)
        document.save(document_path)

        # Insert user data into database
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name, email, phone_number, address, pincode, dob, password, document_path) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                    (name, email, phone_number, address, pincode, dob, password, document_path))
        mysql.connection.commit()
        cur.close()

        flash('Registration successful!', 'success')
        return redirect(url_for('index'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        cur = mysql.connection.cursor()
        cur.execute("SELECT user_id, name, email, password FROM users WHERE email = %s", (email,))
        user = cur.fetchone()
        cur.close()

        if user and user[3] == password:
            session['loggedin'] = True
            session['user_id'] = user[0]
            session['username'] = user[1]
            return redirect(url_for('profile'))
        else:
            return 'Invalid email or password'

    return render_template('login.html')

# Profile route
@app.route('/profile')
def profile():
    if 'loggedin' in session:
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))
    
    
@app.route('/my_profile')
def my_profile():
    return render_template('profile.html')
    
@app.route('/mybookings')
def my_bookings():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT reservation.room_id, check_in, check_out, res_date, Room_name, Price FROM reservation JOIN rooms ON reservation.room_id = rooms.room_id")
    bookings = cursor.fetchall()
    cursor.close()

    return render_template('mybookings.html', bookings=bookings)
# Logout route
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('loggedin', None)
    session.pop('user_id', None)
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(port=5000, debug=True)


