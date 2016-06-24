import sqlite3 as lite
import json

def add_user_prof(database, ID):
    #------------------------------------------------------
    #
    #
    #-------------------------------------------------------
    con = None
    try:
        con = lite.connect(database)
        with con:
            cur = con.cursor()
            cur.execute("INSERT INTO userprofile (ID) VALUES(?)",
                        (ID,))
            con.commit()
        return True
    except lite.Error:
        return False
    finally:
        if con:
            con.close()

def get_user_prof(database, ID):
    con = None
    try:
        con = lite.connect(database)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM userprofile WHERE ID = ?",
                        (ID,))
            con.commit()
            data = cur.fetchall()
            if len(data) > 0:
                return json.dumps({'id':data[0][0],'biography':data[0][1],'profilephoto':data[0][2]})
            return None
    except lite.Error:
        return None
    finally:
        if con:
            con.close()

def remove_user_prof(database, ID):
    con = None
    try:
        con = lite.connect(database)
        with con:
            cur = con.cursor()
            cur.execute("DELETE FROM userprofile WHERE ID = ?",
                        (ID,))
            con.commit()
        return True
    except lite.Error:
        return False
    finally:
        if con:
            con.close()

def update_user_prof(database,updated_user_prof):
    con = None
    try:
        con = lite.connect(database)
        with con:
            con.rollback()
            cur = con.cursor()
            cur.execute("UPDATE userprofile SET biography = ?, profilephoto = ?, WHERE ID = ?;",
                        (updated_user_prof['biography'], updated_user_prof['profilephoto'], updated_user_prof['id']))
            con.commit()
        return True
    except lite.Error:
        return False
    finally:
        if con:
            con.close()