from flask import Flask, render_template
from flask_login import LoginManager
from user import user
from note import note 
from utils import get_user_by_id

app = Flask(__name__)
app.config['SECRET_KEY'] = 'somethign'
app.register_blueprint(user)
app.register_blueprint(note)

login_manager = LoginManager(app)
login_manager.login_view = 'user.sign_in_page'

@login_manager.user_loader
def load_user(id):
    return get_user_by_id(id)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ ==  '__main__':
    app.run(debug=True)

