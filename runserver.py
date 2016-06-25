from flask import Flask
from flask.templating import render_template
from flask.globals import request
from util.database_gen import delete_all_tables, build_all_tables
import datetime
import cgi
from flask.helpers import make_response
import time
from db import user_dao, security_dao, user_profile_dao
from util.app_constants import pg_responses, ss_temp_folder, ls_temp_folder
import json

pg_app = Flask(__name__)
ps_database = 'C:/Users/Owner/OneDrive/Ludus/util/databases/pg.db'

@pg_app.route('/')
def index():
    months_choices = []
    for i in range(1,13):
        months_choices.append((i,(datetime.date(2008, i, 1).strftime('%B'))))
    return render_template('index.html', months = months_choices)

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

#Views
@pg_app.route('/ss-profile')
def ss_profile():
    return render_template(ss_temp_folder+'pgprofile.html')

@pg_app.route('/ls-profile')
def ls_profile():
    return render_template(ls_temp_folder+'pgprofile.html')

if __name__ == "__main__":
    print 'deleting tables'
    delete_all_tables(ps_database)
    print 'building tables'
    build_all_tables(ps_database)       
    pg_app.run(host='0.0.0.0', debug=True)