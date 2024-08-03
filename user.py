from flask import Blueprint, flash, render_template, redirect, request, url_for
from flask_login import current_user, login_user, logout_user
from utils import create_user, get_user_by_username

user = Blueprint(__name__, 'user')


@user.post('/sign-up')
def sign_up():
    username =request.form.get('username')
    password = request.form.get('password')
    message = create_user(str(username), str(password))
    flash(message[0])
    if message[2]:
        flash('Kindly Login')
        return redirect(url_for('user.sign_in_page'))
    return redirect(url_for('user.sign_up_page'))


@user.post('/sign-in')
def sign_in():
    username =request.form.get('username')
    password = request.form.get('password')

    user = get_user_by_username(str(username))
    if user != None:
        if password == 'password':
            print('valid')
            login_user(user)
            return redirect(url_for('note.notes'))
    flash('Invalid Credentials')
    return redirect(url_for('user.sign_in_page'))


@user.route('/sign-in')
def sign_in_page():
    if current_user.is_authenticated:
        return redirect(url_for('note.notes'))

    return render_template('sign-in.html')


@user.route('/sign-up')
def sign_up_page():
    if current_user.is_authenticated:
        return redirect(url_for('note.notes'))

    return render_template('sign-up.html')


@user.route('/sign-out')
def sign_out():
    logout_user()
    return redirect(url_for('index'))


