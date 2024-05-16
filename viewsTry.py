from flask import Blueprint, render_template, request, redirect, url_for, flash
from auth import authenticate_user, register_user, register_service_provider

auth_blueprint = Blueprint('auth', __name__, template_folder='templates')

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = authenticate_user(username, password)
        if user:
            # Lakukan tindakan setelah login berhasil
            return redirect(url_for('dashboard'))
        else:
            flash('Username atau password salah', 'error')
    return render_template('auth/login.html')

@auth_blueprint.route('/register/user', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        register_user(username, email, password)
        flash('Pendaftaran berhasil', 'success')
        return redirect(url_for('login'))
    return render_template('auth/register_user.html')

@auth_blueprint.route('/register/provider', methods=['GET', 'POST'])
def register_provider():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        register_service_provider(name, email, phone, password)
        flash('Pendaftaran berhasil', 'success')
        return redirect(url_for('login'))
    return render_template('auth/register_provider.html')
