from flask import render_template, request, redirect, url_for, flash, session
from app import app

# Dummy user for example
USER = {'email': 'test@example.com', 'password': 'test123'}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email == USER['email'] and password == USER['password']:
            session['email'] = email
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'email' not in session:
        return redirect(url_for('login'))
    return f"Welcome {session['email']}! You are logged in."

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))
