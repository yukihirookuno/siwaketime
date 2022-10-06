from flask import request, redirect, url_for,render_template,flash,session
from siwaketime import app
from siwaketime import db
from siwaketime.models.entries import Entry
from siwaketime.views.users import login_required
from flask import Blueprint

entry = Blueprint('entry', __name__)

@entry.route('/')
@login_required
def show_entries():
    entries = Entry.query.order_by(Entry.id.desc()).all()
    return render_template('entries/index.html', entries=entries)


@entry.route('/entries', methods=['POST'])
@login_required
def add_entry():
        entry = Entry(
                title = request.form['title'],
                memo = request.form['memo'],
                hour = request.form['hour'],
                genre = request.form['genre']
                )
        db.session.add(entry)
        db.session.commit()
        flash('記録の登録が完了しました')
        return redirect (url_for('entry.show_entries'))  


@entry.route ('/entries/new', methods=['GET'])
@login_required
def new_entry():
    return render_template('entries/new.html')


@entry.route('/entries/<int:id>',methods=['GET'])
@login_required
def show_entry(id):
    entry = Entry.query.get(id)
    return render_template('entries/show.html', entry=entry)


@entry.route('/entries/<int:id>/edit', methods=['GET'])
@login_required
def edit_entry(id):
    entry = Entry.query.get(id)
    return render_template('entries/edit.html', entry=entry)


@entry.route('/entries/<int:id>/update', methods=["POST"])
@login_required
def update_entry(id):
    entry = Entry.query.get(id)
    entry.title = request.form['title']
    entry.memo = request.form['memo']
    entry.hour = request.form['hour']
    entry.genre = request.form['genre']
    db.session.merge(entry)
    db.session.commit()
    flash('記録が更新されました')
    return redirect (url_for('entry.show_entries'))


@entry.route('/entries/<int:id>/delete', methods=['POST'])
@login_required
def delete_entry(id):
    entry = Entry.query.get(id)
    db.session.delete(entry)
    db.session.commit()
    flash('記録が削除されました')
    return redirect (url_for('entry.show_entries'))

