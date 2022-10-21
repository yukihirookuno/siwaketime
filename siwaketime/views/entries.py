from flask import request, redirect, url_for,render_template,flash,session
from flask import current_app as app
from datetime import datetime
from siwaketime import db
from siwaketime.config import JST, db_session
from siwaketime.models.entries import Entry
from siwaketime.views.users import login_required
from sqlalchemy import func
from flask import Blueprint

entry = Blueprint('entry', __name__)

@entry.route('/')
@login_required
def show_entries():
    user_id = session["id"]
    username = session["username"]
    entries = db_session.query(Entry).order_by(Entry.id.desc()).filter(Entry.user_id==user_id).all()
    sum_muda_time = db_session.query(func.sum(Entry.hour)).filter(Entry.user_id==user_id).group_by(Entry.genre).all()
    for sum_muda_times in sum_muda_time:
        print(sum_muda_times[0])
    sum_ganbari_time = db_session.query(func.sum(Entry.hour)).filter(Entry.user_id==user_id,Entry.genre=='頑張った時間')
    for sum_ganbari_times in sum_ganbari_time:
        print(sum_ganbari_times[0])
    sum_asobi_time = db_session.query(func.sum(Entry.hour)).filter(Entry.user_id==user_id,Entry.genre=='趣味や遊びの時間')
    for sum_asobi_times in sum_asobi_time:
        print(sum_ganbari_times[0])
    return render_template('entries/index.html', entries=entries, sum_muda_time=sum_ganbari_times[0], sum_ganbari_time=sum_ganbari_times[0],sum_asobi_time=sum_asobi_times[0])


@entry.route('/entries', methods=['POST'])
@login_required
def add_entry():
        entry_user_id = session["id"]
        entry_username = session["username"]
        dt = datetime.now(JST)
        dt = dt.replace(microsecond = 0)
        entry = Entry(
                title = request.form['title'],
                memo = request.form['memo'],
                hour = request.form['hour'],
                genre = request.form['genre'],
                user_id = entry_user_id,
                username = entry_username,
                created_at = dt
                )
        db_session.add(entry)
        db_session.commit()
        flash('記録の登録が完了しました')
        return redirect (url_for('entry.show_entries'))  


@entry.route ('/entries/new', methods=['GET'])
@login_required
def new_entry():
    return render_template('entries/new.html')


@entry.route('/entries/<int:id>',methods=['GET'])
@login_required
def show_entry(id):
    entry = db_session.query(Entry).get(id)
    return render_template('entries/show.html', entry=entry)


@entry.route('/entries/<int:id>/edit', methods=['GET'])
@login_required
def edit_entry(id):
    entry = db_session.query(Entry).get(id)
    return render_template('entries/edit.html', entry=entry)


@entry.route('/entries/<int:id>/update', methods=["POST"])
@login_required
def update_entry(id):
    entry = db_session.query(Entry).get(id)
    entry.title = request.form['title']
    entry.memo = request.form['memo']
    entry.hour = request.form['hour']
    entry.genre = request.form['genre']
    db_session.merge(entry)
    db_session.commit()
    flash('記録が更新されました')
    return redirect (url_for('entry.show_entries'))


@entry.route('/entries/<int:id>/delete', methods=['POST'])
@login_required
def delete_entry(id):
    entry = db_session.query(Entry).get(id)
    db_session.delete(entry)
    db_session.commit()
    flash('記録が削除されました')
    return redirect (url_for('entry.show_entries'))

