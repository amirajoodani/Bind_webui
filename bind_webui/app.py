
import os
from flask import Flask, render_template, request, redirect, url_for,session
import subprocess

app = Flask(__name__)

app.secret_key = 'your_secret_key'
sample_username = 'admin'
sample_password = 'password'
logged_in = False




# Function to parse BIND zone files and extract DNS records
def execute_record_script():
    try:
        script_path = 'record.sh'
        
        # Check if the script exists
        if os.path.exists(script_path):
            # Execute the script and capture its output
            output = os.popen(f'bash {script_path}').read()

            print(f"Script Output: {output}")

            # Split the output into lines
            lines = output.splitlines()

            # Format the output as a list of dictionaries
            result = [{"line": line} for line in lines]
        else:
            result = [{"error": "record.sh script not found"}]

        return result

    except Exception as e:
        print(f"Error parsing BIND zone files: {e}")
        return []



# Route to display DNS records
@app.route('/', methods=['GET', 'POST'])
def login():
    global logged_in

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(f"Entered Username: {username}, Password: {password}")
        # Check if the provided credentials are valid (replace this with your authentication logic)
        if username == sample_username and password == sample_password:
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid credentials')

    return render_template('login.html', error=None)

# Route for the login page
#@app.route('/login', methods=['GET', 'POST'])
#def login():
#    if request.method == 'POST':
#        username = request.form['username']
#        password = request.form['password']

        # Check if the provided credentials are valid (replace this with your authentication logic)
#        if username == sample_username and password == sample_password:
#            session['logged_in'] = True
#            return redirect(url_for('index'))
#        else:
#            return render_template('login.html', error='Invalid credentials')
#
#    return render_template('login.html', error=None)

# Route for the logout action
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))


#@app.route('/index')
#def index():
#    global logged_in
#    global dns_records
#    if logged_in:
#        dns_records = execute_record_script()
#        return render_template('index.html', records=dns_records)
#
#   else:
#        return redirect(url_for('login'))

@app.route('/index')
def index():
    global logged_in
    global dns_records
    if 'logged_in' in session and session['logged_in']:
        dns_records = execute_record_script()
        return render_template('index.html', records=dns_records, logged_in=True)
    else:
        return redirect(url_for('login'))
