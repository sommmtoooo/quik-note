from flask import Flask, render_template
from flask_login import LoginManager
from user import user
from utils import get_user_by_id

app = Flask(__name__)
app.config['SECRET_KEY'] = 'somethign'
app.register_blueprint(user)

login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return get_user_by_id(user_id)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('notes.html')


if __name__ ==  '__main__':
    app.run(debug=True)

