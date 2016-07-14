from flask import Flask
from flask.templating import render_template
from flask.globals import request, session
from util.database_gen import delete_all_tables, build_all_tables
import cgi
from flask.helpers import make_response, url_for, flash
import time
from db import user_dao, security_dao, user_profile_dao, stream_dao
from util.app_constants import pg_responses, MONTHS
import json
import hashlib
from datetime import datetime
from util.app_config import gen_secret_key
from werkzeug.utils import redirect, secure_filename
from werkzeug.exceptions import abort
import os

UPLOAD_FOLDER = os.path.join('static','img')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

pg_app = Flask(__name__)
pg_app.secret_key = gen_secret_key()
ps_database = 'C:/Users/Owner/git/Ludus/util/databases/pg.db'
pg_app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@pg_app.route('/upload_img/<pt>/<ID>',methods=["POST"])
def pg_photo_upload(pt,ID):
    if request.method == 'POST':
        photo = request.files['photo']
        save_path = os.path.join(pg_app.config['UPLOAD_FOLDER'],session.get('cuid'))
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        print save_path
        if photo and allowed_file(photo.filename):
            filename = secure_filename(photo.filename)
            save_name = None
            user = None
            if pt == "profile":
                save_name = session.get('cuid') + '_profile.' + filename.split('.')[1]
                user = json.loads(user_profile_dao.get_user_prof(ps_database, session.get('cuid')))
                user['profilephoto'] = "..\\" + save_path + "\\" + save_name
            else:
                save_name = session.get('cuid') + '_bg.' + filename.split('.')[1]
                user = json.loads(user_profile_dao.get_user_prof(ps_database, session.get('cuid')))
                user['coverphoto'] = "..\\" + save_path + "\\"  + save_name
            user_profile_dao.update_user_prof(ps_database, user)
            os.remove(os.path.join(save_path,save_name))
            photo.save(os.path.join(save_path,save_name))
            return redirect(url_for('update_profile',ID=session.get('cuid'))) 
    return redirect(url_for('update_user_profile', ID=session.get('cuid')))         
           
@pg_app.route('/')
def index():
    return render_template('index.html', months = MONTHS)

@pg_app.route('/login', methods=["POST"])
def pg_login():
    username = cgi.escape(request.form['username'].lower())
    password = cgi.escape(request.form['password'])
    login_password = hashlib.md5(password.encode()).hexdigest()
    user_found = user_dao.get_user_by_username(ps_database, username)
    if user_found is not None:
        uf = json.loads(user_found)
        us = json.loads(security_dao.get_security(ps_database, uf['id']))
        if us['password'] == login_password:
            session['cuid'] = uf['id']
            return make_response(json.dumps({'id':uf['id'],'login_resp':pg_responses.LOGIN_SUC}),200)
    return make_response(json.dumps({'login_resp':pg_responses.INV_LOGIN}),200)

@pg_app.route('/register', methods=["POST"])
def pg_register():
    firstname = cgi.escape(request.form['firstname'].lower())
    lastname = cgi.escape(request.form['lastname'].lower())
    username = cgi.escape(request.form['username'].lower())
    if user_dao.check_username_exists(ps_database, username) is True:
        return make_response(json.dumps(pg_responses.USERNAME_IN_USE),200)
    email = cgi.escape(request.form['email'].lower())
    if user_dao.check_email_exists(ps_database, email) is True:
        return make_response(json.dumps(pg_responses.EMAIL_IN_USE),200)
    password = cgi.escape(request.form['password'])
    month = cgi.escape(request.form['month'])
    if(len(month) == 1):
        month = "0" + month
    day = cgi.escape(request.form['day'])
    if(len(day) == 1):
        day = "0" + day
    year = cgi.escape(request.form['year'])
    dateofbirth = int(time.mktime(time.strptime(month+"/"+day+"/"+year, "%m/%d/%Y")))
    gender = cgi.escape(request.form['gender'])
    user_add_results = user_dao.add_user(ps_database, firstname, lastname, email, username, dateofbirth, gender)
    if True in user_add_results and security_dao.add_security(ps_database, user_add_results[1], password) is True and user_profile_dao.add_user_prof(ps_database, user_add_results[1]) is True:
        return make_response(json.dumps(pg_responses.REG_SUCCES),200)
    return make_response(json.dumps(pg_responses.REG_FAILED),200)

@pg_app.route('/logout', methods=["GET"])
def pg_logout():
    session['cuid'] = None
    return redirect(url_for('index'))

#Views
@pg_app.route('/user_profile/<ID>')
def user_profile(ID):
    if not session.get('cuid'):
        return redirect('/')
    current_user = json.loads(user_dao.get_user_by_id(ps_database, ID))
    current_user_profile = json.loads(user_profile_dao.get_user_prof(ps_database, ID))
    return render_template('profile.html', user=current_user, about=current_user_profile)

@pg_app.route('/feed')
def stream():
    if not session.get('cuid'):
        return redirect('/')
    current_user = json.loads(user_dao.get_user_by_id(ps_database, session.get('cuid')))
    current_user_profile = json.loads(user_profile_dao.get_user_prof(ps_database, session.get('cuid')))
    return render_template('feed.html', user=current_user, about=current_user_profile)

@pg_app.route('/game')
def game():
    if not session.get('cuid'):
        return redirect('/')
    current_user = json.loads(user_dao.get_user_by_id(ps_database, session.get('cuid')))
    current_user_profile = json.loads(user_profile_dao.get_user_prof(ps_database, session.get('cuid')))
    return render_template('game_page.html', user=current_user, about=current_user_profile)


@pg_app.route('/update_profile/<ID>')
def update_user_profile(ID):
    if not session.get('cuid'):
        return redirect('/')
    if session.get('cuid') != ID:
        abort(401) 
    current_user = json.loads(user_dao.get_user_by_id(ps_database, ID))
    current_user_profile = json.loads(user_profile_dao.get_user_prof(ps_database, ID))
    current_user_security = json.loads(security_dao.get_security(ps_database, ID))
    return render_template('update_profile.html', user=current_user, about=current_user_profile,
                           security=current_user_security, dob=iso_date_string(current_user['dateofbirth']))

#Create Methods
@pg_app.route('/newpost', methods=['POST'])
def new_post():
    post_text = cgi.escape(request.form['post'])
    if stream_dao.add_new_post(ps_database, post_text, session.get('cuid')) is True:
        return make_response(json.dumps(pg_responses.POST_SUCCES),200)
    return make_response(json.dumps(pg_responses.POST_ERROR),200)

#Update Methods
@pg_app.route('/update_user/<ID>', methods=["POST"])
def update_user(ID):
    fetch_user = json.loads(user_dao.get_user_by_id(ps_database, session.get('cuid')))
    firstname = cgi.escape(request.form['firstname'].lower())
    lastname = cgi.escape(request.form['lastname'].lower())
    username = cgi.escape(request.form['username'].lower())
    if fetch_user['username'] != username:
        if user_dao.check_username_exists(ps_database, username) is True:
            return make_response(json.dumps(pg_responses.USERNAME_IN_USE),200)
    email = cgi.escape(request.form['email'].lower())
    if fetch_user['email'] != email:
        if user_dao.check_email_exists(ps_database, email) is True:
            return make_response(json.dumps(pg_responses.EMAIL_IN_USE),200)
    dateofbirth = int(time.mktime(time.strptime(cgi.escape(request.form['dateofbirth']), "%B %d, %Y")))
    gender = cgi.escape(request.form['gender'])
    fetch_user['firstname'] = firstname
    fetch_user['lastname'] = lastname
    fetch_user['username'] = username
    fetch_user['email'] = email
    fetch_user['dateofbirth'] = dateofbirth
    fetch_user['gender'] = gender
    if user_dao.update_user(ps_database, fetch_user) is True:
        return make_response(json.dumps(pg_responses.UPDT_SUCCES),200)
    return make_response(json.dumps(pg_responses.UPDT_ERROR),200)

@pg_app.route('/update_profile/<ID>', methods=["POST"])
def update_profile(ID):
    fetch_user_profile = json.loads(user_profile_dao.get_user_prof(ps_database, session.get('cuid')))
    biography = cgi.escape(request.form['biography'].lower())
    xbxgt = cgi.escape(request.form['xbxgt'].lower())
    plsgt = cgi.escape(request.form['plsgt'].lower())
    stmgt = cgi.escape(request.form['stmgt'].lower())
    fetch_user_profile['biography'] = biography
    fetch_user_profile['xbxgt'] = xbxgt
    fetch_user_profile['plsgt'] = plsgt
    fetch_user_profile['stmgt'] = stmgt
    if user_profile_dao.update_user_prof(ps_database, fetch_user_profile) is True:
        return make_response(json.dumps(pg_responses.UPDT_SUCCES),200)
    return make_response(json.dumps(pg_responses.UPDT_ERROR),200)
    
@pg_app.route('/update_security/<ID>', methods=["POST"])
def update_security(ID):
    password = cgi.escape(request.form['password'].lower())
    fetch_sec = json.loads(security_dao.get_security(ps_database, ID))
    fetch_sec['password'] = password
    if security_dao.update_security(ps_database, fetch_sec, True) is True:
        return make_response(json.dumps(pg_responses.UPDT_SUCCES),200)
    return make_response(json.dumps(pg_responses.UPDT_ERROR),200)

@pg_app.route('/like/<postID>', methods=["POST"])
def like_post(postID):
    if stream_dao.check_like(ps_database, postID, session.get('cuid')) is False:
        if stream_dao.add_like(ps_database, postID, session.get('cuid')) is True:
            return make_response('GOOD',200)
    else: 
        if stream_dao.remove_like(ps_database, postID, session.get('cuid')) is True:
            return make_response('GOOD',200)
    return make_response('BAD',200)

#GET METHODS
@pg_app.route('/fetch_post/<postID>')
def fetch_post(postID):
    if not session.get('cuid'):
        return redirect('/')
    post = json.loads(stream_dao.get_post(ps_database, postID))
    return make_response(json.dumps({'post':post}),200)

@pg_app.route('/stream/<limit>/<offset>')
def fetch_stream(limit,offset):
    if not session.get('cuid'):
        return redirect('/')
    return make_response(json.dumps(stream_dao.get_all_posts_lo(ps_database, limit, offset)),200)

@pg_app.route('/user_stream/<limit>/<offset>')
def fetch_user_stream(limit,offset):
    if not session.get('cuid'):
        return redirect('/')
    return make_response(json.dumps(stream_dao.get_posts_for_user_lo(ps_database, session.get('cuid'), limit, offset)),200)

@pg_app.route('/user_info/<ID>')
def fetch_user_info_n_profile(ID):
    info = user_dao.get_user_by_id(ps_database, ID)
    profile = user_profile_dao.get_user_prof(ps_database, ID)
    return make_response(json.dumps({'info':info,'profile':profile}),200)
    
#Error Pages
@pg_app.errorhandler(401)
def unauthorized_access(e):
    current_user = json.loads(user_dao.get_user_by_id(ps_database,  session.get('cuid')))
    current_user_profile = json.loads(user_profile_dao.get_user_prof(ps_database, session.get('cuid')))
    return render_template('error_pages/401.html',user=current_user, about=current_user_profile), 401

def date_calc(dob):
    return time.strftime('%B %d, %Y', time.localtime(int(dob))) 

def age_calc(dob):
    year = int(time.strftime('%B %d, %Y', time.localtime(int(dob)))[-4:])
    return  "(" + str(datetime.now().year - year) + " Years Old)"

def iso_date_string(date):
    return time.strftime("%Y %m %d",time.localtime(int(date)))

def post_datetime_string(date):
    return time.strftime("%B %d, %Y at %I:%M %p",time.localtime(int(date)))

def get_date_tuple(date):
    return time.strptime(date_calc(date), "%B %d, %Y") 

pg_app.jinja_env.filters['date_calc'] = date_calc
pg_app.jinja_env.filters['age_calc'] = age_calc


if __name__ == "__main__":
    delete_all_tables(ps_database)
    build_all_tables(ps_database)       
    pg_app.run(host='0.0.0.0', debug=True)
