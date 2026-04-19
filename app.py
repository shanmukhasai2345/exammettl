from flask import Flask, render_template, request, redirect, url_for, session
from flask_pymongo import PyMongo
import pdfkit
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/exammettl'
mongo = PyMongo(app)

# Student Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = mongo.db.users.find_one({'username': username})
        if user and user['password'] == password:
            session['username'] = username
            return redirect(url_for('exam_interface'))
    return render_template('login.html')

# Exam Interface
@app.route('/exam_interface')
def exam_interface():
    if 'username' in session:
        return render_template('exam_interface.html')
    return redirect(url_for('login'))

# Admin Dashboard
@app.route('/admin', methods=['GET', 'POST'])
def admin_dashboard():
    if request.method == 'POST':
        # Admin functionalities here
        pass
    return render_template('admin_dashboard.html')

# Generate PDF Certificate
@app.route('/generate_certificate/<student_id>')
def generate_certificate(student_id):
    # Code for generating PDF certificate
    return "Certificate generated!"

# Proctoring features
@app.route('/proctoring')
def proctoring():
    if 'username' in session:
        # Proctoring functionalities here
        return render_template('proctoring.html')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)