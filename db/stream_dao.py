import sqlite3 as lite
import json
import time
from datetime import datetime

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
            return None
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
            return None
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

def get_comment(database, ID):
    con = None
    try:
        con = lite.connect(database)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM comment WHERE ID = ?",
                        (ID,))
            con.commit()
            data = cur.fetchall()
            if len(data) > 0:
                return json.dumps({'id':data[0][0],'postID':data[0][1],'text':data[0][2],'likes':data[0][3],'userID':data[0][4]})
            return None
    except lite.Error:
        return None
    finally:
        if con:
            con.close()

def get_post_comments(database, postID):
    con = None
    comment = {}
    try:
        con = lite.connect(database)
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM comment WHERE postID = ?",
                        (postID,))
            con.commit()
            data = cur.fetchall()
            if len(data) > 0:
                for x in range(0,len(data)):
                    comment[x] = get_comment(database, data[x][0])
            return comment
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
            cur.execute("DELETE FROM comment WHERE postID = ?",
                        (ID,))
            con.commit()
        return True
    except lite.Error:
        return False
    finally:
        if con:
            con.close()
            
def remove_comment(database, postID, ID):
    con = None
    try:
        con = lite.connect(database)
        with con:
            cur = con.cursor()
            cur.execute("DELETE FROM comment WHERE postID = ? and ID = ?",
                        (postID, ID,))
            con.commit()
        return True
    except lite.Error:
        return False
    finally:
        if con:
            con.close()