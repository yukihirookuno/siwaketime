from flask import request, redirect, url_for,render_template,flash,session
from flask import current_app as app
from siwaketime import db
from siwaketime.config import db_session, engine,api_key,api_secret_key,access_token,access_token_secret,bearer_token
from siwaketime.models.entries.entries import Entry
from siwaketime.models.users import User
from siwaketime.models.entries.genre_count import Genre_count
from siwaketime.models.entries.genres import Genre
from siwaketime.models.entries.titles import Title
from siwaketime.views.users import login_required
from sqlalchemy import func
import tweepy
from flask import Blueprint


entry = Blueprint('entry', __name__)

doryoku_counts = 0
asobi_counts = 0
muda_counts = 0
kihon_counts = 0


def count_genre(genre):    
    if genre == '努力時間':
        global doryoku_counts
        doryoku_counts += 1
    if genre == '遊び時間':
        global asobi_counts
        asobi_counts += 1
    if genre == '無駄時間':
        global muda_counts
        muda_counts += 1
    if genre == '基本時間':
        global kihon_counts
        kihon_counts +=1
        

def count_reset():
    global doryoku_counts
    doryoku_counts = 0
    global asobi_counts
    asobi_counts = 0
    global muda_counts
    muda_counts = 0
    global kihon_counts
    kihon_counts = 0


def search_tweets():
    client = tweepy.Client(bearer_token = bearer_token, consumer_key = api_key, consumer_secret = api_secret_key, access_token = access_token, access_token_secret = access_token_secret)
    QUERY = ["#仕訳時間 -is:retweet"]
    MAX_RESULTS = 10
    tweets = client.search_recent_tweets(query = QUERY, max_results = MAX_RESULTS)
    tweet_url_list = []
    n=0
    if tweets is not None:
        for tweet in tweets[n]:
            tweet_url_list.append(f"https://twitter.com/user/status/{tweet.data['id']}")
            n+=1
    return tweet_url_list


@entry.route('/')
@login_required
def show_entries():
    user_id = session["id"]
    username = session["username"]
    search_date = session["date"]
    check_entry = db_session.query(
        Entry
    ).filter(Entry.user_id==user_id, Entry.date==search_date).all()
    if check_entry == []:
        session['check_recorded'] = None
    else:
        session['check_recorded'] = 'ok'
    entry = None
    entries = db_session.query(
            Entry, Genre, Title, Genre_count
        ).join(
            Genre, Entry.entry_id==Genre.genres_id
        ).join(
            Title, Entry.entry_id==Title.titles_id
        ).join(
            Genre_count, Entry.entry_id==Genre_count.genre_counts_id
        ).filter(Entry.user_id==user_id, Entry.date==search_date
        ).all()
    sum_doryoku = db_session.query(func.sum(Genre_count.doryoku_count)).filter(Genre_count.username==username).all()
    tmp_sum_doryoku =sum_doryoku[0]
    convert_sum_doryoku=tmp_sum_doryoku[0]
    if convert_sum_doryoku==None:
        convert_sum_doryoku=0

    sum_asobi = db_session.query(func.sum(Genre_count.asobi_count)).filter(Genre_count.username==username).all()
    tmp_sum_asobi =sum_asobi[0]
    convert_sum_asobi=tmp_sum_asobi[0]
    if convert_sum_asobi==None:
        convert_sum_asobi=0

    sum_muda= db_session.query(func.sum(Genre_count.muda_count)).filter(Genre_count.username==username).all()
    tmp_sum_muda =sum_muda[0]
    convert_sum_muda=tmp_sum_muda[0]
    if convert_sum_muda==None:
        convert_sum_muda=0
    
    sum_kihon = db_session.query(func.sum(Genre_count.kihon_count)).filter(Genre_count.username==username).all()
    tmp_sum_kihon =sum_kihon[0]
    convert_sum_kihon=tmp_sum_kihon[0]
    if convert_sum_kihon==None:
        convert_sum_kihon=0


    tweet_url_list=search_tweets()
    if session['check_recorded'] == 'ok':
        for entry in entries:
            return render_template('entries/index.html',entry=entry,sum_doryoku=convert_sum_doryoku,sum_asobi=convert_sum_asobi,sum_muda=convert_sum_muda,sum_kihon=convert_sum_kihon,search_date=search_date,username=username,url_list=tweet_url_list) 
    else: return render_template('entries/index.html',entry=entry,sum_doryoku=convert_sum_doryoku,sum_asobi=convert_sum_asobi,sum_muda=convert_sum_muda,sum_kihon=convert_sum_kihon,search_date=search_date,username=username,url_list=tweet_url_list)





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
        global doryoku_counts
        input_doryoku_count = doryoku_counts
        global asobi_counts
        input_asobi_count = asobi_counts
        global muda_counts
        input_muda_count = muda_counts
        global kihon_counts
        input_kihon_count = kihon_counts
        input_date = request.form['date']
        date_check = db_session.query(Entry.date
            ).filter(Entry.user_id==entry_user_id, Entry.date == input_date
            ).all()
        if date_check != []:
            flash('この日は、すでに記録が存在しています。記録を編集したい場合は、編集ページから行ってください。')
            count_reset()
            return redirect(url_for('entry.show_entries'))
        entry = Entry()
        entry.text = request.form['text']
        entry.date = input_date
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
        genre_count.doryoku_count = input_doryoku_count
        genre_count.asobi_count = input_asobi_count
        genre_count.muda_count = input_muda_count
        genre_count.kihon_count = input_kihon_count
        genre_count.username = entry_username

        db_session.add(entry)
        db_session.add(genre)
        db_session.add(title)
        db_session.add(genre_count)
        db_session.commit()
        session["check_recorded"]="ok"
        session["date"]=input_date
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
    genre = db_session.query(Genre).get(id)
    title = db_session.query(Title).get(id)
    genre_count = db_session.query(Genre_count).get(id)
    return render_template('entries/show.html', entry=entry,genre=genre,title=title,genre_count=genre_count)


@entry.route('/entries/<int:id>/edit', methods=['GET'])
@login_required
def edit_entry(id):
    entry = db_session.query(Entry).get(id)
    genre = db_session.query(Genre).get(id)
    title = db_session.query(Title).get(id)
    genre_count = db_session.query(Genre_count).get(id)
    return render_template('entries/edit.html', entry=entry,genre=genre,title=title,genre_count=genre_count)


@entry.route('/entries/<int:id>/update', methods=["POST"])
@login_required
def update_entry(id):
    entry = db_session.query(Entry).get(id)
    genre = db_session.query(Genre).get(id)
    title = db_session.query(Title).get(id)
    genre_count = db_session.query(Genre_count).get(id)

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

    global doryoku_counts
    input_doryoku_count = doryoku_counts
    global asobi_counts
    input_asobi_count = asobi_counts
    global muda_counts
    input_muda_count = muda_counts
    global kihon_counts
    input_kihon_count = kihon_counts

    entry.text = request.form['text']
    entry.user_id = entry_user_id
    entry.username = entry_username

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

    genre_count.doryoku_count = input_doryoku_count
    genre_count.asobi_count = input_asobi_count
    genre_count.muda_count = input_muda_count
    genre_count.kihon_count = input_kihon_count
    genre_count.username = entry_username

    db_session.merge(entry)
    db_session.merge(genre)
    db_session.merge(title)
    db_session.merge(genre_count)
    db_session.commit()
    count_reset()
    flash('記録が更新されました')
    return redirect (url_for('entry.show_entries'))


@entry.route('/entries/<int:id>/delete', methods=['POST'])
@login_required
def delete_entry(id):
    entry = db_session.query(Entry).get(id)
    genre = db_session.query(Genre).get(id)
    title = db_session.query(Title).get(id)
    genre_count = db_session.query(Genre_count).get(id)
    db_session.delete(entry)
    db_session.delete(genre)
    db_session.delete(title)
    db_session.delete(genre_count)
    db_session.commit()
    flash('記録が削除されました')
    return redirect (url_for('entry.show_entries'))


@entry.route ('/entries/search', methods=['GET'])
@login_required
def search_entry():
    return render_template('entries/search.html')


@entry.route('/entries/search_date', methods=['POST'])
@login_required
def search_date_entry():
    input_date = request.form['search_date']
    session["date"] = input_date
    return redirect(url_for('entry.show_entries'))
