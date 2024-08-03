from flask import Blueprint, render_template
from flask_login import login_required

note = Blueprint(__name__, 'note')

@note.route('/notes')
@login_required
def notes():
    return render_template('notes.html')

@note.route('/notes/')
@note.route('/notes/<id>')
@login_required
def note_page(id = None):
    return render_template('note.html')
