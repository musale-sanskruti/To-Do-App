from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash, session

auth_bp = Blueprint('auth', __name__) #A Blueprint is a way to organize a group of related routes and views in a Flask application.

#dummy user data for authentication
user_credentials = {
    'username': 'testuser',
    'password': 'testpass'
}

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
     if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == user_credentials['username'] and password == user_credentials['password']:
          session['user'] = username
          flash('Login successful!', 'success')
        else:
           flash('Invalid username or password', 'warning')
     return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('auth.login'))