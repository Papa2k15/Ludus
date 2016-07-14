import sqlite3 as lite
import json
import time

def add_new_post(database,text,userID):
    #------------------------------------------------------
    #
    #
    #-------------------------------------------------------
    con = None
    try:
        con = lite.connect(database)
        with con:
            cur = con.cursor()
            cur.execute("INSERT INTO post (text,userID,datetime) VALUES(?,?,?)",
                        (text,userID,int(time.time()),))
            con.commit()
        return True
    except lite.Error:
        return False
    finally:
        if con:
            con.close()

def get_post(database, ID):
    con = None
    try:
        con = lite.connect(database)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM post WHERE ID = ?",
                        (ID,))
            con.commit()
            data = cur.fetchall()
            if len(data) > 0:
                return json.dumps({'id':data[0][0],'text':data[0][1],'likes':data[0][2], 'userID':data[0][3], 'datetime':data[0][4]})
            return {}
    except lite.Error:
        return None
    finally:
        if con:
            con.close()

def get_user_post(database, ID, userID):
    con = None
    try:
        con = lite.connect(database)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM post WHERE ID = ? and userID = ?",
                        (ID,userID,))
            con.commit()
            data = cur.fetchall()
            if len(data) > 0:
                return json.dumps({'id':data[0][0],'text':data[0][1],'likes':data[0][2], 'userID':data[0][3], 'datetime':data[0][4]})
            return {}
    except lite.Error:
        return None
    finally:
        if con:
            con.close()

def get_all_posts_for_user(database, userID):
    con = None
    posts = {}
    try:
        con = lite.connect(database)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM post WHERE userID = ?",
                        (userID,))
            con.commit()
            data = cur.fetchall()
            if len(data) > 0:
                for x in range(0,len(data)):
                    posts[x] = get_user_post(database, data[x][0], userID)
            return posts
    except lite.Error:
        return None
    finally:
        if con:
            con.close()

def get_posts_for_user_lo(database, userID, limit, offset):
    con = None
    posts = {}
    try:
        con = lite.connect(database)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM post WHERE userid = ? ORDER BY datetime DESC LIMIT ? OFFSET ?;",
                        (userID, limit, offset,))
            con.commit()
            data = cur.fetchall()
            if len(data) > 0:
                for x in range(0,len(data)):
                    posts[x] = get_user_post(database, data[x][0], userID)
            return posts
    except lite.Error:
        return None
    finally:
        if con:
            con.close()

def get_all_posts_lo(database, limit=10, offset=0):
    con = None
    posts = {}
    try:
        con = lite.connect(database)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM post ORDER BY datetime DESC LIMIT ? OFFSET ?;",
                        (limit, offset,))
            con.commit()
            data = cur.fetchall()
            if len(data) > 0:
                for x in range(0,len(data)):
                    posts[x] = get_post(database, data[x][0])
            return posts
    except lite.Error:
        return None
    finally:
        if con:
            con.close()

def remove_post(database, ID):
    con = None
    try:
        con = lite.connect(database)
        with con:
            cur = con.cursor()
            cur.execute("DELETE FROM post WHERE ID = ?",
                        (ID,))
            con.commit()
        return True
    except lite.Error:
        return False
    finally:
        if con:
            con.close()
            
def add_like(database, postID, userID):
    con = None
    try:
        con = lite.connect(database)
        with con:
            cur = con.cursor()
            cur.execute("INSERT  INTO like (postID,userID) VALUES (?,?)",
                        (postID, userID,))
            cur.execute("UPDATE post SET likes = likes + 1 WHERE ID = ?",
                        (postID,))
            con.commit()
        return True
    except lite.Error:
        return False
    finally:
        if con:
            con.close()
 
def check_like(database, postID, userID):
    con = None
    try:
        con = lite.connect(database)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM like WHERE postID = ? AND userID = ?",
                        (postID, userID,))
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
        
def remove_like(database, postID, userID):
    con = None
    try:
        con = lite.connect(database)
        with con:
            cur = con.cursor()
            cur.execute("DELETE FROM like WHERE postID = ? and userID = ?",
                        (postID, userID,))
            cur.execute("UPDATE post SET likes = likes - 1 WHERE ID = ?",
                        (postID,))          
            con.commit()
        return True
    except lite.Error:
        return False
    finally:
        if con:
            con.close()