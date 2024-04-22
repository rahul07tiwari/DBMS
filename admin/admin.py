from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_mysqldb import MySQL

app1= Flask(__name__)
app1.secret_key = 'your_secret_key'

# MySQL Configuration
app1.config['MYSQL_HOST'] = 'localhost'  # MySQL host (change if your MySQL server is hosted elsewhere)
app1.config['MYSQL_USER'] = 'root'  # MySQL username
app1.config['MYSQL_PASSWORD'] = '1234@'  # MySQL password
app1.config['MYSQL_DB'] = 'kaushtubha'  # MySQL database name

mysql = MySQL(app1)

@app1.route('/')
def admin_page():
    return render_template('admin.html')

@app1.route('/admin_Panel')
def admin_Panel():
    if 'username' in session:
        return render_template('admin_Panel.html')
    return redirect(url_for('admin_page'))

@app1.route('/login', methods=['POST'])
def login():
    admin_name = request.form['admin_name']
    admin_pass = request.form['admin_password']
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM admin WHERE admin_name=%s AND admin_pass=%s", (admin_name, admin_pass))
    user = cur.fetchone()
    cur.close()

    if user:
        session['username'] = admin_name
        return redirect(url_for('admin_Panel'))
    else:
        message = 'Invalid username or password'
    return render_template('admin.html', message=message)

@app1.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
      session.pop('username', None)
      return redirect(url_for('admin_page'))
    else:
        return redirect(url_for('admin_page'))

@app1.route('/Settings')
def Settings():
    if request.method == 'POST':
        switch_state = request.form.get('shutdown_state')

        # Perform database update based on the switch state
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE settings SET shutdown = %s", (shutdown_state,))
        mysql.connection.commit()
        cursor.close()

        # Redirect back to the settings page
        return redirect(url_for('Settings'))

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT site_title, site_about, shutdown FROM Settings")
    settings_data = cursor.fetchone()
    cursor.close()
    
    # Pass the fetched data to the template
    site_title = settings_data[0]
    site_about = settings_data[1]
    shutdown_state = settings_data[2]
    return render_template('Settings.html', site_title=site_title, site_about=site_about, shutdown_state=shutdown_state)

if __name__ == "__main__":
    app1.run(port=3000, debug=True)
