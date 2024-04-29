from flask import Flask
from flask_mysqldb import MySQL

app3 = Flask(__name__)
app3.secret_key = 'your_secret_key'

# MySQL Configuration
app3.config['MYSQL_HOST'] = 'localhost'  # MySQL host (change if your MySQL server is hosted elsewhere)
app3.config['MYSQL_USER'] = 'root'  # MySQL username
app3.config['MYSQL_PASSWORD'] = '1234@'  # MySQL password
app3.config['MYSQL_DB'] = 'kaushtubha'  # MySQL database name

mysql = MySQL(app3)

@app3.route('/')
def all_in_one():
    with app3.app_context():
        # Create 'admin' table if it doesn't exist and insert values
        cur = mysql.connection.cursor()
        cur.execute("SHOW TABLES LIKE 'admin'")
        result = cur.fetchone()
        if result is None:
            cur.execute("CREATE TABLE admin (sr_no int primary key auto_increment NOT NULL, admin_name varchar(50) NOT NULL, admin_pass varchar(100) NOT NULL)")
            cur.execute("INSERT INTO admin (admin_name, admin_pass) VALUES ('Rahul Tiwari', 'Speaks456@'), ('Neeraj Singh', 'Fraud456@'), ('Sudhanshu Kaul', 'Fraud420@')")
            mysql.connection.commit()

        # Create 'users' table if it doesn't exist
        cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                phone_number VARCHAR(20) UNIQUE NOT NULL,
                address VARCHAR(255) NOT NULL,
                pincode VARCHAR(6) NOT NULL,
                dob DATE NOT NULL,
                password VARCHAR(255) NOT NULL,
                document_path VARCHAR(255) NOT NULL
            )
        ''')
        # Create 'Settings' table if it doesn't exist
        cur = mysql.connection.cursor()
        cur.execute("SHOW TABLES LIKE 'settings'")
        result = cur.fetchone()
        if result is None:
            cur.execute('''
            CREATE TABLE IF NOT EXISTS Settings (
            sr_no int AUTO_INCREMENT PRIMARY KEY,
            site_title varchar(50) NOT NULL,
            site_about varchar(255) NOT NULL,
            shutdown boolean NOT NULL
            )
        ''')
            cur.execute("INSERT INTO Settings VALUES (1, 'Hotel Kaushtubha', 'Lorem ipsum dolor sit amet consectetur adipisicing elit.Quisquam distinctio nulla adipisci tempora error nostrum recusandae, possimus similique perspiciatis qui.', '0')")
            mysql.connection.commit()
        
        cur = mysql.connection.cursor()
        cur.execute("SHOW TABLES LIKE 'Contact'")
        result = cur.fetchone()
        if result is None:
            cur.execute('''
            CREATE TABLE IF NOT EXISTS Contact (
            sr_no int AUTO_INCREMENT PRIMARY KEY,
            Name varchar(50) NOT NULL,
            Email varchar(255) NOT NULL,
            Subject varchar(50) NOT NULL,
            Message varchar(200) NOT NULL
            )
        ''')
    return 'Tables created and values inserted successfully'

if __name__ == "__main__":
    app3.run(port=2000, debug=True)


