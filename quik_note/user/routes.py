from flask import Blueprint, flash, render_template, redirect, request, url_for
from flask_login import current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from quik_note.user.dao import UserDAO
from quik_note.utils import csrf_protect

user = Blueprint('user',__name__)
user_dao = UserDAO()

@user.post('/sign-up')
@csrf_protect
def sign_up():
    username =request.form.get('username')
    password = request.form.get('password')
    message = user_dao.create_user(str(username), generate_password_hash(str(password)))
    flash(message[0])
    if message[2]:
        flash('Kindly Login')
        return redirect(url_for('user.sign_in_page'))
    return redirect(url_for('user.sign_up_page'))


@user.post('/sign-in')
@csrf_protect
def sign_in():
    username =request.form.get('username')
    password = request.form.get('password')

    user = user_dao.get_user_by_username(str(username))
    if user != None:
        if check_password_hash(str(user.password), str(password)):
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


