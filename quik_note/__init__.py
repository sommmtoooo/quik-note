from flask import Flask, abort, redirect, render_template, url_for
from flask_login import LoginManager, current_user, login_manager

from quik_note import login_manager
from quik_note.config import Config
from quik_note.user.dao import UserDAO

from quik_note.user.routes import user
from quik_note.note.routes import note
from quik_note.utils import generate_csrf_token

login_manager = LoginManager()

def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)
        
    login_manager.init_app(app)
    login_manager.login_view = 'user.sign_in_page'

    # Login Manager Loader
    @login_manager.user_loader
    def load_user(id):
        dao = UserDAO()
        return dao.get_user_by_id(id)

    @app.context_processor
    def inject_csrf_token():
        return dict(csrf_token=generate_csrf_token)


    #--------------------------------#
    #---- BLUE PRINTS ---------------#
    #--------------------------------#
    app.register_blueprint(user)
    app.register_blueprint(note)


    @app.route('/')
    def index():
        if current_user.is_authenticated:
            return redirect(url_for('note.notes'))
        return render_template('index.html')

    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html'), 404

    return app
