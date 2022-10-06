from flask import request, redirect, url_for, render_template, flash, session
from siwaketime import app
from siwaketime import db
from siwaketime.models.users import User
from functools import wraps
from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint

user = Blueprint('user', __name__)

def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect (url_for('user.login'))
        return view(*args, **kwargs)
    return inner


@user.route('/users/signup', methods=['GET', 'POST'])
def signup():
    """ユーザーの登録"""
    if request.method == 'POST':
        username = request.form.get("username")
        if not username:
            flash('名前を入力してください')
            return redirect(url_for('user.signup'))
        password = request.form.get("password")
        if not password:
            flash('パスワードを入力してください')
            return redirect(url_for('user.signup'))
        confirmation = request.form.get("confirmation")
        if not confirmation:
            flash('同じパスワードを入力してください')
            return redirect(url_for('user.signup'))
        if not confirmation == password:
            flash('同じパスワードを入力してください')
            return redirect(url_for('user.signup'))
        try:
            user = User(
                    username = username,
                    hash = generate_password_hash(password, method='sha256')
                    )   
            db.session.add(user)
            db.session.commit()
            flash('ユーザーの登録が完了しました')
            return redirect (url_for('user.login'))
        except:
            flash('既に存在するユーザー名です')
            return redirect(url_for('user.signup'))
    else:
        return render_template('users/signup.html')


@user.route('/users/login', methods=["GET", "POST"])
def login():
    """ログイン機能"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if not request.form.get("username"):
            flash('ユーザー名を入力してください')
            return redirect(url_for('user.login'))
        elif not request.form.get("password"):
            flash('パスワードを入力してください')
            return redirect(url_for('user.login'))
        user = User.query.filter_by(username=username).first()
        if check_password_hash(user.hash, password):
            session['logged_in'] = True
            flash('ログインが完了しました')
            return redirect(url_for('entry.show_entries'))
    else:
        return render_template('users/login.html')


@user.route("/users/logout")
@login_required
def logout():
    """Log user out"""
    session.pop('logged_in',None)
    flash('ログアウトしました')
    return redirect(url_for('user.login'))


@user.app_errorhandler(404)
def non_existant_route(error):
    return redirect(url_for('user.login'))