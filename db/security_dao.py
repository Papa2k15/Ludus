import sqlite3 as lite
import json
import hashlib
from util.app_config import gen_secret_key

def add_security(database, user_id,  password):
    #------------------------------------------------------
    #
    #
    #-------------------------------------------------------
    con = None
    try:
        con = lite.connect(database)
        with con:
            cur = con.cursor()
            cur.execute("INSERT INTO security (userid, password) VALUES(?, ?)",
                        (user_id, hashlib.md5(password.encode()).hexdigest(),))
            con.commit()
        return True
    except lite.Error:
        return False
    finally:
        if con:
            con.close()

def get_security(database, user_id):
    con = None
    security = None
    try:
        con = lite.connect(database)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM security WHERE userid = ?",
                        (user_id,))
            con.commit()
            data = cur.fetchall()
            if len(data) > 0:
                security = json.dumps({'userid':data[0][0],'password':data[0][1],
                                     'showonline':data[0][2],'lastlogin':data[0][3]})
                return security
            else:
                return None
    except lite.Error:
        return None
    finally:
        if con:
            con.close()

def remove_security(database, user_id):
    con = None
    try:
        con = lite.connect(database)
        with con:
            cur = con.cursor()
            cur.execute("DELETE FROM security WHERE userid = ?",
                        (user_id,))
            con.commit()
        return True
    except lite.Error:
        return False
    finally:
        if con:
            con.close()

def update_security(database,updated_security, password_change):
    con = None
    try:
        con = lite.connect(database)
        with con:
            con.rollback()
            cur = con.cursor()
            if password_change is True:
                cur.execute("UPDATE security SET password = ?, showonline = ?, lastlogin = ? WHERE userid = ?;",
                        (hashlib.md5(updated_security['password'].encode()).hexdigest(), updated_security['showonline'], updated_security['lastlogin'], 
                         updated_security['userid']))
            else:
                cur.execute("UPDATE security SET password = ?, showonline = ?, lastlogin = ? WHERE userid = ?;",
                        (updated_security['password'], updated_security['showonline'], updated_security['lastlogin'], 
                         updated_security['userid']))
            con.commit()
        return True
    except lite.Error:
        return False
    finally:
        if con:
            con.close()

def forgot_password_entry(database, user_id):
    #------------------------------------------------------
    #
    #
    #-------------------------------------------------------
    con = None
    try:
        con = lite.connect(database)
        with con:
            cur = con.cursor()
            key = hashlib.md5(gen_secret_key().encode()).hexdigest()
            cur.execute("INSERT INTO forgotpassword (userid, resetkey) VALUES(?, ?)",
                        (user_id, key,))
            con.commit()
        return True, key
    except lite.Error:
        return False, -1
    finally:
        if con:
            con.close()

def get_user_from_key(database, key):
    con = None
    try:
        con = lite.connect(database)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM forgotpassword WHERE resetkey = ?",
                        (key,))
            con.commit()
            data = cur.fetchall()
            if len(data) > 0:
                return data[0][0]
            return None
    except lite.Error:
        return None
    finally:
        if con:
            con.close()    

def generate_new_hash(database, user_id):
    con = None
    try:
        con = lite.connect(database)
        with con:
            cur = con.cursor()
            key = hashlib.md5(gen_secret_key().encode()).hexdigest()
            cur.execute("UPDATE forgotpassword SET resetkey = ? WHERE userid = ?;",
                        (key, user_id))
            con.commit()
        return True, key
    except lite.Error:
        return False, -1
    finally:
        if con:
            con.close()
 
def check_forgot_password(database, user_id):
    con = None
    try:
        con = lite.connect(database)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM forgotpassword WHERE userid = ?",
                        (user_id,))
            con.commit()
            data = cur.fetchall()
            if len(data) > 0:
                return True
            return False
    except lite.Error:
        return False
    finally:
        if con:
            con.close()        

def check_forgot_password_key(database, key):
    con = None
    try:
        con = lite.connect(database)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM forgotpassword WHERE resetkey = ?",
                        (key,))
            con.commit()
            data = cur.fetchall()
            if len(data) > 0:
                return True
            return False
    except lite.Error:
        return False
    finally:
        if con:
            con.close()     
                   
def forgot_password_remove(database, user_id):
    #------------------------------------------------------
    #
    #
    #-------------------------------------------------------
    con = None
    try:
        con = lite.connect(database)
        with con:
            cur = con.cursor()
            cur.execute("DELETE FROM forgotpassword WHERE userid = ?",
                        (user_id,))
            con.commit()
        return True
    except lite.Error:
        return False
    finally:
        if con:
            con.close()
            
