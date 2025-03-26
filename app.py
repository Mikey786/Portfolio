from flask import Flask, request, jsonify, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# Route to display the form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Connect to the SQLite3 database
    conn = sqlite3.connect('form.db')
    cursor = conn.cursor()

    # Insert the form data into the database
    cursor.execute('''
    INSERT INTO form_data (name, email, message)
    VALUES (?, ?, ?)
    ''', (name, email, message))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    # Return a JSON message indicating success
    return jsonify({"message": "Form submitted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)