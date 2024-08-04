from flask import Blueprint, abort, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from quik_note.model import Note
from quik_note.utils import csrf_protect, generate_unique_id
from quik_note.note.dao import NoteDAO

note = Blueprint('note', __name__)
note_dao = NoteDAO()


@note.route('/notes')
@login_required
def notes():
    notes = note_dao.get_user_note(current_user.id)
    return render_template('notes.html', notes=notes)



@note.route('/notes/')
@note.route('/notes/<id>')
@login_required
def note_page(id = None):
    if id is None:
        return render_template('note.html', note=None)
    note = note_dao.get_note(id)
    if note is None:
        flash('Note Not Found')
        return abort(404)
    return render_template('note.html', note=note)


@note.post('/notes/')
@note.post('/notes/<id>')
@login_required
@csrf_protect
def create_note_page(id = None):
    title = request.form.get('title')
    content = request.form.get('content')

    if title == '' and content == '':
        flash('Note is empty')
        return abort(200)

    if id is None:
        unique_id = generate_unique_id()
        note = Note(unique_id, current_user.id, title, content)
        response = note_dao.create_note(note)
        flash(response[0])
    else:
        note = Note(id, current_user.id, title, content)
        response = note_dao.update_note(note)
        flash(response[0])

    return redirect(url_for('note.notes'))


@note.route('/notes/delete/<id>')
@login_required
def note_delete_note(id):
    message = note_dao.delete_note(str(id))
    flash(message[0])
    return redirect(url_for('note.notes'))
