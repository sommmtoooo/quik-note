from flask import request, session, abort
from functools import wraps
from os import urandom
from uuid import uuid4
from itsdangerous import URLSafeSerializer, base64_decode, base64_encode

from quik_note.config import Config

def generate_unique_id() -> str:
    return str(uuid4())


serializer = URLSafeSerializer(Config.SECRET_KEY)

def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = serializer.dumps(base64_encode(urandom(24)).decode('utf-8'))
    return session['_csrf_token']


def validate_csrf_token(token):
    try:
        return token == session['_csrf_token']
    except Exception as error:
        return False


def csrf_protect(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        token = request.form.get('_csrf_token')
        if not token or not validate_csrf_token(token):
            abort(403)
        session.pop('_csrf_token', None)
        return func(*args, **kwargs)
    return decorated_function

