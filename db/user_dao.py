import sqlite3 as lite
import random
import json
from util.app_constants import user_id_length, end, start, alpha_list, num_list,\
    char_bit, user_pre
    
def add_user(database, firstname, lastname, email, username, dateofbirth, gender):
    #------------------------------------------------------
    #
    #-------------------------------------------------------
    con = None
    blogzone_id = None
    try:
        con = lite.connect(database)
        with con:
            cur = con.cursor()
            blogzone_id = get_id(database)
            cur.execute("INSERT INTO user (ID, firstname, lastname, email, username, dateofbirth, gender) VALUES(?, ?, ?, ?, ?, ?, ?)",
                        (blogzone_id, firstname, lastname, email, username, dateofbirth, gender, ))
            con.commit()
        return True, blogzone_id
    except lite.Error:
        return False, -1
    finally:
        if con:
            con.close()

def get_user(database, email):
    con = None
    user = None
    try:
        con = lite.connect(database)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM user WHERE email = ?",
                        (email,))
            con.commit()
            data = cur.fetchall()
            if len(data) > 0:
                user = json.dumps({'id':data[0][0],'firstname':data[0][1],'lastname':data[0][2],
                                     'email':data[0][3], 'username':data[0][4], 'dateofbirth':data[0][5], 'gender':data[0][6] })
                return user
            else:
                return None
    except lite.Error:
        return None
    finally:
        if con:
            con.close()

def get_user_by_username(database, username):
    con = None
    user = None
    try:
        con = lite.connect(database)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM user WHERE username = ?",
                        (username,))
            con.commit()
            data = cur.fetchall()
            if len(data) > 0:
                user = json.dumps({'id':data[0][0],'firstname':data[0][1],'lastname':data[0][2],
                                     'email':data[0][3], 'username':data[0][4], 'dateofbirth':data[0][5], 'gender':data[0][6] })
                return user
            else:
                return None
    except lite.Error:
        return None
    finally:
        if con:
            con.close()

def get_user_by_id(database, identification):
    con = None
    user = None
    try:
        con = lite.connect(database)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM user WHERE id = ?",
                        (identification,))
            con.commit()
            data = cur.fetchall()
            if len(data) > 0:
                user = json.dumps({'id':data[0][0],'firstname':data[0][1],'lastname':data[0][2],
                                     'email':data[0][3], 'username':data[0][4], 'dateofbirth':data[0][5], 'gender':data[0][6] })
                return user
            else:
                return None
    except lite.Error:
        return None
    finally:
        if con:
            con.close()

def get_all_users(database, orderby, a_d):
    con = None
    users = {}
    try:
        con = lite.connect(database)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM user ORDER BY "+orderby+" "+a_d+";")
            con.commit()
            data = cur.fetchall()
            if len(data) > 0:
                for x in range(0,len(data)):
                    users[x] = get_user(database, data[x][3])
                return users
            else:
                return None
    except lite.Error:
        return None
    finally:
        if con:
            con.close()

def remove_user(database, email):
    con = None
    try:
        con = lite.connect(database)
        with con:
            cur = con.cursor()
            cur.execute("DELETE FROM user WHERE email = ?",
                        (email,))
            con.commit()
        return True
    except lite.Error:
        return False
    finally:
        if con:
            con.close()

def update_user(database,updated_user):
    con = None
    try:
        con = lite.connect(database)
        with con:
            con.rollback()
            cur = con.cursor()
            cur.execute("UPDATE user SET firstname = ?, lastname = ?, email = ?, username = ?, dateofbirth = ?, gender = ? WHERE ID = ?;",
                        (updated_user['firstname'], updated_user['lastname'], updated_user['email'], 
                         updated_user['username'], updated_user['dateofbirth'], updated_user['gender'], updated_user['id']))
            con.commit()
        return True
    except lite.Error:
        return False
    finally:
        if con:
            con.close()
       
#Helper Methods
def get_id(database):
    id_builder = ''
    indexer = 0
    while(indexer < user_id_length):
        selector = random.randrange(start,end)
        ralpha = alpha_list[random.randrange(start,len(alpha_list))]
        rnum = num_list[random.randrange(start,len(num_list))]
        if selector == char_bit:
            id_builder += ralpha
        else:
            id_builder += rnum
        indexer += 1
    while(check_id_exists(database,id_builder)):
        id_builder = ''
        id_builder = get_id(database)
    return user_pre + id_builder

def check_id_exists(database,account_id):
    con = None
    try:
        con = lite.connect(database)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM user WHERE ID = ?",
                        (account_id,))
            con.commit()
            if len(cur.fetchall()) > 0:
                return True
            return False
    except lite.Error:
        return False
    finally:
        if con:
            con.close()

def check_email_exists(database,email):
    con = None
    try:
        con = lite.connect(database)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM user WHERE email = ?",
                        (email,))
            con.commit()
            if len(cur.fetchall()) > 0:
                return True
            return False
    except lite.Error:
        return False
    finally:
        if con:
            con.close()

def check_username_exists(database,username):
    con = None
    try:
        con = lite.connect(database)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM user WHERE username = ?",
                        (username,))
            con.commit()
            if len(cur.fetchall()) > 0:
                return True
            return False
    except lite.Error:
        return False
    finally:
        if con:
            con.close()

def get_users_size(database):
    con = None
    try:
        con = lite.connect(database)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM user;")
            con.commit()
            data = cur.fetchall()
            if len(data) > 0:
                return len(data)
            else:
                return 0
    except lite.Error:
        return -1
    finally:
        if con:
            con.close()
            
# search user database
def query_user_dao(database, query):
    search_query = query.lstrip().rstrip().split(' ')
    con = None
    users = {}
    try:
        con = lite.connect(database)
        with con:
            con.rollback()
            cur = con.cursor()
            for q in search_query:
                querybuilder = " SELECT * FROM user WHERE ID LIKE '" + q + "%'" \
                " UNION" \
                " SELECT * FROM user WHERE firstname LIKE '" + q + "%'" \
                " UNION" \
                " SELECT * FROM user WHERE lastname LIKE '" + q + "%'" \
                " UNION" \
                " SELECT * FROM user WHERE email LIKE '" + q + "%'" \
                " UNION " \
                " SELECT * FROM user WHERE username LIKE '" + q + "%'" \
                " UNION " \
                " SELECT * FROM user WHERE ID LIKE '%" + q + "%'" \
                " UNION" \
                " SELECT * FROM user WHERE firstname LIKE '%" + q + "%'" \
                " UNION" \
                " SELECT * FROM user WHERE lastname LIKE '%" + q + "%'" \
                " UNION" \
                " SELECT * FROM user WHERE email LIKE '%" + q + "%'" \
                " UNION " \
                " SELECT * FROM user WHERE username LIKE '%" + q + "%'" \
                " UNION " \
                " SELECT * FROM user WHERE ID LIKE '%" + q + "'" \
                " UNION" \
                " SELECT * FROM user WHERE firstname LIKE '%" + q + "'" \
                " UNION" \
                " SELECT * FROM user WHERE lastname LIKE '%" + q + "'" \
                " UNION" \
                " SELECT * FROM user WHERE username LIKE '%" + q + "'" \
                " UNION" \
                " SELECT * FROM user WHERE email LIKE '%" + q + "';"
            cur.execute(querybuilder)
            con.commit()
            data = cur.fetchall()
            if len(data) > 0:
                for x in range(0,len(data)):
                    users[x] = get_user(database, data[x][3])
                return users
            return None
    except lite.Error:
        return None
    finally:
        if con:
            con.close()