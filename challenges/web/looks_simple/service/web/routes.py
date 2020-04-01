#! /usr/bin/env python3
from contextlib import contextmanager
from datetime import datetime
from flask import abort, escape, Flask, flash, redirect, render_template, Response, request, session, url_for
from functools import wraps
from hashlib import sha256
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from sqlalchemy import Column, MetaData, String, Table, TIMESTAMP
from werkzeug.serving import run_simple
from werkzeug.debug import DebuggedApplication
from werkzeug.wsgi import get_host
import re
import os
import secrets
import sqlalchemy as db

## OPTIONS ##
DEBUG = True

## DEBUGGER PIN CHALLENGE ##
DEBUG_PIN = None
ACCESS_EP = secrets.token_urlsafe(32)

# Flask Setup #
app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_urlsafe(16)
app.config['PREFERRED_URL_SCHEME'] = 'https'

HOST = os.environ.get('HOST')
LOCAL_IP = os.environ.get('LOCAL_IP')

@app.context_processor
def inject_vars():
    return dict(HOST=HOST)

# Database Full Access #
# @TODO: Change credentials before to full access creds before deployment
engine_full = db.create_engine('postgresql://looks_simple_w:looks_simple@db/looks_simple')
metadata = MetaData(engine_full, schema='looks_simple')
user_table = Table(
    'users', metadata,
    Column('username', String(60), primary_key=True),
    Column('description', String(10000), nullable=True),
    Column('password', String(255), nullable=False)
)
post_table = Table(
    'posts', metadata,
    Column('id', String(32), primary_key=True),
    Column('title', String(255), nullable=False),
    Column('content', String(100000), nullable=False),
    Column('date_posted', TIMESTAMP(True), nullable=False)
)

# Database Read Access #
# @TODO: Change credentials before to read-only creds before deployment
engine_ro = db.create_engine('postgresql://looks_simple_ro:looks_simple@db/looks_simple')
metadata_ro = MetaData(engine_ro, schema='looks_simple')
user_table_ro = Table(
    'users', metadata_ro,
    Column('username', String(60), primary_key=True),
    Column('description', String(10000), nullable=True),
    Column('password', String(255), nullable=False)
)
post_table_ro = Table(
    'posts', metadata_ro,
    Column('id', String(32), primary_key=True),
    Column('title', String(255), nullable=False),
    Column('content', String(100000), nullable=False),
    Column('date_posted', TIMESTAMP(True), nullable=False)
)

def authenticated_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if not session.get('user'):
            flash('You need to be logged in!', 'danger')
            return redirect(url_for('login', _scheme='https', _external=True))
        return f(*args, **kwargs)
    return wrap

def unauthenticated_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if session.get('user'):
            return redirect(url_for('home', _scheme='https', _external=True))
        return f(*args, **kwargs)
    return wrap

def admin_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        user = session.get('user')
        if user['username'] not in ['superadmin', 'admin']:
            return redirect(url_for('home', _scheme='https', _external=True))
        return f(*args, **kwargs)
    return wrap

def csrf_token(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        csrf_token = session.get('csrf_token')
        if not csrf_token:
            session['csrf_token'] = secrets.token_urlsafe(48)
        if request.method != 'GET':
            if not csrf_token:
                return abort(403)
            elif request.form.get('csrfToken') != csrf_token:
                return abort(403)
            session['csrf_token'] = secrets.token_urlsafe(48)
        return f(*args, **kwargs)
    return wrap

def insert(table, values):
    stmt = table.insert().values(**values)
    try:
        with engine_full.connect() as conn:
            conn.execute(stmt)
    except Exception as e:
        return False, e
    return True, None

def update(table, values, where_clause):
    stmt = table.update().values(**values).where(where_clause)
    try:
        with engine_full.connect() as conn:
            conn.execute(stmt)
    except Exception as e:
        return False, e
    return True, None

@contextmanager
def query(table, where_clause=None):
    yielded = False
    if not isinstance(where_clause, type(None)):
        stmt = table.select().where(where_clause)
    else:
        stmt = table.select()
    try:
        with engine_ro.connect() as conn:
            result = conn.execute(stmt)
            all_ = result.fetchall()
            ret_val = list()
            for item in all_:
                joined = dict(zip(result.keys(), item))
                ret_val.append(joined)
    except Exception as e:
        yielded = True
        yield None, e
    if not yielded:
        yield ret_val, None
        result.close()

# Password Methods #
def hash_pwd(password):
    if isinstance(password, str):
        password = password.encode('utf-8')
    pw_hash = sha256()
    pw_hash.update(password)
    return pw_hash.hexdigest()

def verify_pwd(password, hashed):
    if isinstance(password, str):
        password = password.encode('utf-8')
    pw_hash = sha256()
    pw_hash.update(password)
    return pw_hash.hexdigest() == hashed

@app.after_request
def add_protections(response):
    csp = """default-src \'self\'; script-src \'self\' \'unsafe-eval\' cdnjs.cloudflare.com;
        style-src \'self\' fonts.googleapis.com cdnjs.cloudflare.com;
        font-src cdnjs.cloudflare.com fonts.gstatic.com;"""
    csp = re.sub('\n', ' ', csp)
    response.headers['Content-Security-Policy'] = csp
    response.headers['X-XSS-Protection'] = '0'
    return response

@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('login', _scheme='https', _external=True), 301)

@app.route('/login', methods=['GET', 'POST'])
@unauthenticated_required
@csrf_token
def login():
    if request.method == 'GET':
        return render_template('regular/login.html')
    username = request.form.get('username') or ''
    password = request.form.get('password') or ''
    if username == 'superadmin':
        if request.headers.get('X-Real-IP') != LOCAL_IP:
            flash('Cannot login as superadmin from web', 'danger')
            return render_template('regular/login.html')
    with query(user_table_ro, (user_table_ro.c.username == username)) as (result, exc):
        if result == None:
            flash('Unknown error occured!', 'danger')
            return render_template('regular/login.html')
        if not result:
            flash('Incorrect username or password!', 'danger')
            return render_template('regular/login.html')
        if verify_pwd(password, result[0].get('password')):
            session['user'] = result[0]
            return redirect(url_for('home', _scheme='https', _external=True))
    flash('Incorrect username or password!', 'danger')
    return render_template('regular/login.html')

@app.route('/logout', methods=['GET'])
def logout():
    if not session.get('user'):
        flash('Not authenticated...', 'danger')
    else:
        session.clear()
        flash('Successfully logged out!', 'success')
    return redirect(url_for('login', _scheme='https', _external=True))

@app.route('/register', methods=['GET', 'POST'])
@unauthenticated_required
@csrf_token
def register():
    if request.method == 'GET':
        return render_template('regular/register.html')
    username = request.form.get('username')
    password = request.form.get('password')
    confirm_password = request.form.get('confirmPassword')
    if not (username and password and confirm_password):
        flash('Please check your inputs!', 'danger')
        return render_template('regular/register.html')
    if password != confirm_password:
        flash('Please check your password inputs!', 'danger')
        return render_template('regular/register.html')
    hashed = hash_pwd(password)
    success, exc = insert(user_table, {'username': username, 'password': hashed})
    if not success:
        if isinstance(exc, db.exc.IntegrityError):
            flash('Username already registered!', 'danger')
        else:
            flash('Unknown error occured...', 'danger')
        return render_template('regular/register.html')
    flash('User successfully registered!', 'success')
    return redirect(url_for('login', _scheme='https', _external=True))

@app.route('/home', methods=['GET'])
@authenticated_required
def home():
    with query(post_table_ro) as (result, exc):
        posts = []
        if result != None:
            result = sorted(result, key=lambda x: x['date_posted'])
            result.reverse()
            for index, item in enumerate(result):
                item['index'] = index
                item['content'] = re.sub('\r', '', item['content'])
                item['content'] = re.sub('\n', '<br>', item['content'])
                posts.append(item)
    return render_template('authenticated/home.html', posts=posts)

@app.route('/new-post', methods=['GET', 'POST'])
@authenticated_required
@csrf_token
def new_post():
    if request.method == 'GET':
        return render_template('authenticated/new-post.html', title='', content='')
    title = request.form.get('title') or ''
    content = request.form.get('content') or ''
    if not title or not content:
        return render_template('authenticated/new-post.html', title=title, content=content)
    date_posted = datetime.now()
    id_ = secrets.token_urlsafe(24)
    title = escape(title)
    content = escape(content)
    success, exc = insert(post_table, {'id': id_, 'title': title, 'content': content, 'date_posted': date_posted})
    if not success:
        flash('Unknown error occured!', 'danger')
        return render_template('authenticated/new-post.html')
    flash('New post added!', 'success')
    return render_template('authenticated/new-post.html')

@app.route('/post/<id_>', methods=['GET'])
@authenticated_required
def post(id_):
    row = None
    try:
        with engine_ro.connect() as conn:
            result = conn.execute(f'SELECT id, title, content FROM looks_simple.posts WHERE id = \'{id_}\'')
            row = result.first()
            result.close()
            if row:
                row = dict(zip(result.keys(), row))
            else:
                code = 404
                return render_template('authenticated/single-post.html', post=row, code=code), code
    except Exception as e:
        code = 500
        return render_template('authenticated/single-post.html', post=row, code=code), code
    return render_template('authenticated/single-post.html', post=row)

@app.route('/update-profile', methods=['GET', 'POST'])
@authenticated_required
@csrf_token
def update_profile():
    user = session.get('user')
    if request.method == 'GET':
        return render_template('authenticated/profile.html')
    username = user['username']
    description = request.form.get('description') or ''
    success, exc = update(user_table, {'description': description}, (user_table.c.username == username))
    if success:
        user['description'] = description
        flash('Profile successfully updated!', 'success')
    else:
        print(exc)
        flash('Unknown error occured!', 'success')
    return render_template('authenticated/profile.html')

def renderer_wait_js(browser):
    wait = WebDriverWait(browser, 15)
    try:
        wait.until(lambda driver: driver.execute_script('return jQuery.active') == 0)
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    except Exception as e:
        raise e

@app.route('/admin', methods=['GET', 'POST'])
@authenticated_required
@admin_required
@csrf_token
def admin():
    rendered = ''
    if request.method == 'POST':
        url = request.form.get('url') or ''
        try:
            browser = Remote('http://selenium:4444/wd/hub', DesiredCapabilities.CHROME)
            # TODO: Replace with appropriate hostname and port
            browser.get(HOST)
            browser.add_cookie({'name': 'session', 'value': request.cookies.get('session')})
            browser.get(url)
            renderer_wait_js(browser)
            rendered = browser.page_source
        except Exception as e:
            pass
    return render_template('authenticated/admin.html', rendered=rendered)

def setup_db():
    metadata.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
    setup_db()