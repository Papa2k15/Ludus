from flask import Flask
from flask.templating import render_template
from flask.globals import request, session
from util.database_gen import delete_all_tables, build_all_tables
import cgi
from flask.helpers import make_response, url_for
import time
from db import user_dao, security_dao, user_profile_dao
from util.app_constants import pg_responses, MONTHS
import json
import hashlib
from datetime import datetime
from util.app_config import gen_secret_key
from werkzeug.utils import redirect
from werkzeug.exceptions import abort

pg_app = Flask(__name__)
pg_app.secret_key = gen_secret_key()
ps_database = 'C:/Users/Owner/git/Ludus/util/databases/pg.db'

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

@pg_app.route('/update_profile/<ID>')
def update_profile(ID):
    print session.get('cuid')
    print ID
    if not session.get('cuid'):
        return redirect('/')
    if session.get('cuid') != ID:
        print 'abort'
        abort(401) 
    current_user = json.loads(user_dao.get_user_by_id(ps_database, ID))
    current_user_profile = json.loads(user_profile_dao.get_user_prof(ps_database, ID))
    return render_template('update_profile.html', user=current_user, about=current_user_profile,
                           months = MONTHS)

#Error Pages
@pg_app.errorhandler(401)
def unauthorized_access(e):
    current_user = json.loads(user_dao.get_user_by_id(ps_database,  session.get('cuid')))
    return render_template('error_pages/401.html',user=current_user), 401

def date_calc(dob):
    return time.strftime('%B %d, %Y', time.localtime(int(dob))) 

def age_calc(dob):
    year = int(time.strftime('%B %d, %Y', time.localtime(int(dob)))[-4:])
    return  "(" + str(datetime.now().year - year) + " Years Old)"

pg_app.jinja_env.filters['date_calc'] = date_calc
pg_app.jinja_env.filters['age_calc'] = age_calc


if __name__ == "__main__":
    print 'deleting tables'
    delete_all_tables(ps_database)
    print 'building tables'
    build_all_tables(ps_database)       
    pg_app.run(host='0.0.0.0', debug=True)
