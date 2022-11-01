from flask import request, redirect, url_for,render_template,flash,session
from flask import current_app as app
from siwaketime import db
from siwaketime.config import db_session
from siwaketime.models.entries.entries import Entry
from siwaketime.models.users import User
from siwaketime.models.entries.genre_count import Genre_count
from siwaketime.models.entries.genres import Genre
from siwaketime.models.entries.titles import Title
from siwaketime.views.users import login, login_required
from sqlalchemy import func
from flask import Blueprint
from datetime import date, datetime

entry = Blueprint('entry', __name__)

ganbari_counts = 0
asobi_counts = 0
muda_counts = 0

def count_genre(genre):    
    if genre == '頑張り時間':
        global ganbari_counts
        ganbari_counts += 1
    if genre == '遊び時間':
        global asobi_counts
        asobi_counts += 1
    if genre == '無駄時間':
        global muda_counts
        muda_counts += 1

def count_reset():
    global ganbari_counts
    ganbari_counts = 0
    global asobi_counts
    asobi_counts = 0
    global muda_counts
    muda_counts = 0


@entry.route('/')
@login_required
def show_entries():
    user_id = session["id"]
    username = session["username"]
    input_day = datetime.now()
    today = input_day.date() 
    print(today)
    entries = db.session.query(Entry, Genre
        ).join(Genre, Entry.entry_id==Genre.genres_id
        ).all()
        #).join(Entry.entry_id == Title.titles_id
        #).join(Entry.entry_id == Genre_count.genre_counts_id
    #entries = db_session.query(Entry).order_by(Entry.id.desc()).filter(Entry.user_id==user_id).all()
    #sum_muda_time = db_session.query(func.sum(Entry.hour)).filter(Entry.user_id==user_id,Entry.genre=='無駄時間')
    #for sum_muda_times in sum_muda_time:
        #print(sum_muda_times[0])
    #sum_ganbari_time = db_session.query(func.sum(Entry.hour)).filter(Entry.user_id==user_id,Entry.genre=='頑張り時間')
    #for sum_ganbari_times in sum_ganbari_time:
        #print(sum_ganbari_times[0])
    #sum_asobi_time = db_session.query(func.sum(Entry.hour)).filter(Entry.user_id==user_id,Entry.genre=='趣味や遊びの時間')
    #for sum_asobi_times in sum_asobi_time:
        #print(sum_asobi_times[0])
    return render_template('entries/index.html')


@entry.route('/entries/date', methods=['POST','GET'])
@login_required
def date_entry():
    if request.method == 'POST':
        user_id = session["id"]
        date=request.form['date']
        print(date)
        entries_log = db_session.query(Entry).order_by(Entry.id.desc()).filter(Entry.user_id==user_id, Entry.created_at == date).all()
        print (entries_log)
        return redirect (url_for('entry.date_entry',entries_log=entries_log))
    else:
        return render_template('entries/date.html')
    


@entry.route('/entries', methods=['POST'])
@login_required
def add_entry():
        entry_user_id = session["id"]
        entry_username = session["username"]
        count_genre(request.form['genre_am12'])
        count_genre(request.form['genre_am1'])
        count_genre(request.form['genre_am2'])
        count_genre(request.form['genre_am3'])
        count_genre(request.form['genre_am4'])
        count_genre(request.form['genre_am5'])
        count_genre(request.form['genre_am6'])
        count_genre(request.form['genre_am7'])
        count_genre(request.form['genre_am8'])
        count_genre(request.form['genre_am9'])
        count_genre(request.form['genre_am10'])
        count_genre(request.form['genre_am11'])
        count_genre(request.form['genre_pm12'])
        count_genre(request.form['genre_pm1'])
        count_genre(request.form['genre_pm2'])
        count_genre(request.form['genre_pm3'])
        count_genre(request.form['genre_pm4'])
        count_genre(request.form['genre_pm5'])
        count_genre(request.form['genre_pm6'])
        count_genre(request.form['genre_pm7'])
        count_genre(request.form['genre_pm8'])
        count_genre(request.form['genre_pm9'])
        count_genre(request.form['genre_pm10'])
        count_genre(request.form['genre_pm11'])
        global ganbari_counts
        input_ganbari_count = ganbari_counts
        global asobi_counts
        input_asobi_count = asobi_counts
        global muda_counts
        input_muda_count = muda_counts
        #すでに登録している日付の場合はチェックし、編集画面に移動　基礎時間のhtml追加
        entry = Entry()
        entry.text = request.form['text']
        entry.date = request.form['date']
        entry.user_id = entry_user_id
        entry.username = entry_username

        genre = Genre()
        genre.genre_am12 = request.form['genre_am12']
        genre.genre_am1 = request.form['genre_am1']
        genre.genre_am2 = request.form['genre_am2']
        genre.genre_am3 = request.form['genre_am3']
        genre.genre_am4 = request.form['genre_am4']
        genre.genre_am5 = request.form['genre_am5']
        genre.genre_am6 = request.form['genre_am6']
        genre.genre_am7 = request.form['genre_am7']
        genre.genre_am8 = request.form['genre_am8']
        genre.genre_am9 = request.form['genre_am9']
        genre.genre_am10 = request.form['genre_am10']
        genre.genre_am11 = request.form['genre_am11']
        genre.genre_pm12 = request.form['genre_pm12']
        genre.genre_pm1 = request.form['genre_pm1']
        genre.genre_pm2 = request.form['genre_pm2']
        genre.genre_pm3 = request.form['genre_pm3']
        genre.genre_pm4 = request.form['genre_pm4']
        genre.genre_pm5 = request.form['genre_pm5']
        genre.genre_pm6 = request.form['genre_pm6']
        genre.genre_pm7 = request.form['genre_pm7']
        genre.genre_pm8 = request.form['genre_pm8']
        genre.genre_pm9 =  request.form['genre_pm9']
        genre.genre_pm10 = request.form['genre_pm10']
        genre.genre_pm11 = request.form['genre_pm11']

        title = Title()
        title.title_am12 =request.form['title_am12']
        title.title_am1 =request.form['title_am1']
        title.title_am2 =request.form['title_am2']
        title.title_am3 =request.form['title_am3']
        title.title_am4 =request.form['title_am4']
        title.title_am5 =request.form['title_am5']
        title.title_am6 =request.form['title_am6']
        title.title_am7 =request.form['title_am7']
        title.title_am8 =request.form['title_am8']
        title.title_am9 =request.form['title_am9']
        title.title_am10 =request.form['title_am10']
        title.title_am11 =request.form['title_am11']
        title.title_pm12 =request.form['title_pm12']
        title.title_pm1 =request.form['title_pm1']
        title.title_pm2 =request.form['title_pm2']
        title.title_pm3 =request.form['title_pm3']
        title.title_pm4 =request.form['title_pm4']
        title.title_pm5 =request.form['title_pm5']
        title.title_pm6 =request.form['title_pm6']
        title.title_pm7 =request.form['title_pm7']
        title.title_pm8 =request.form['title_pm8']
        title.title_pm9 =request.form['title_pm9']
        title.title_pm10 =request.form['title_pm10']
        title.title_pm11 =request.form['title_pm11']

        genre_count = Genre_count()
        genre_count.gannbari_count = input_ganbari_count
        genre_count.asobi_count = input_asobi_count
        genre_count.muda_count = input_muda_count

        db_session.add(entry)
        db_session.add(genre)
        db_session.add(title)
        db_session.add(genre_count)
        db_session.commit()
        count_reset()
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


#@entry.route('/entries/<int:id>/update', methods=["POST"])
#@login_required
#def update_entry(id):
#    entry = db_session.query(Entry).get(id)
#    entry.title = request.form['title']
#    entry.memo = request.form['memo']
#    entry.hour = request.form['hour']
#    entry.genre = request.form['genre']
#    entry.date = request.form['date']
#    db.session.merge()
#    db_session.commit()
#    flash('記録が更新されました')
#    return redirect (url_for('entry.show_entries'))


#@entry.route('/entries/<int:id>/delete', methods=['POST'])
#@login_required
#def delete_entry(id):
#    entry = db_session.query(Entry).get(id)
#    db_session.delete(entry)
#    db_session.commit()
#    flash('記録が削除されました')
#    return redirect (url_for('entry.show_entries'))

