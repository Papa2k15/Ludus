import sqlite3 as lite
from database_scripts import drop_all_tables_script, clear_all_tables_script,\
    user_table_script, user_profile_table_script, user_security_table_script,\
    log_table_script, TEST_user_inserts, TEST_user_sec_insert,\
    forget_password_table_script, TEST_user_prof_insert
from util.database_scripts import posts_table_script, comments_table_script,\
    TEST_stream_insert

def build_all_tables(database):
    con = None
    try:
        con = lite.connect(database)
        with con:
            database_cursor = con.cursor()
            database_cursor.executescript(user_table_script)
            database_cursor.executescript(user_profile_table_script)
            database_cursor.executescript(user_security_table_script)
            database_cursor.executescript(posts_table_script)
            database_cursor.executescript(comments_table_script)
            ##database_cursor.executescript(forget_password_table_script)
            ##database_cursor.executescript(blog_table_script)
            ##database_cursor.executescript(log_table_script)
            database_cursor.executescript(TEST_user_inserts)
            database_cursor.executescript(TEST_user_prof_insert)
            database_cursor.executescript(TEST_user_sec_insert)
            database_cursor.executescript(TEST_stream_insert)
            print "Operation Complete"
            con.commit()
            return True                  
    except lite.Error, e:
        print e
        print "SOMETHING WENT WRONG"
        return False
    finally:    
        con.close()
        
def delete_all_tables(database):
    con = None
    try:
        con = lite.connect(database)
        with con:
            database_cursor = con.cursor()
            database_cursor.executescript(drop_all_tables_script)
            con.commit()
        return True                  
    except lite.Error, e:
        print e
        print database
        return False
    finally:    
        con.close()

def clear_all_tables(database):
    con = None
    try:
        con = lite.connect(database)
        with con:
            database_cursor = con.cursor()
            database_cursor.executescript(clear_all_tables_script)
            con.commit()
            return True                  
    except lite.Error:
        return False
    finally:    
        con.close()

def build_user_table(database):
    con = None
    try:
        con = lite.connect(database)
        with con:
            database_cursor = con.cursor()
            database_cursor.executescript(user_table_script)
            con.commit()
            return True                  
    except lite.Error:
        return False
    finally:    
        con.close()    

def drop_user_table(database):
    con = None
    try:
        con = lite.connect(database)
        with con:
            database_cursor = con.cursor()
            database_cursor.execute("DROP TABLE IF EXISTS user;")
            con.commit()
            return True                  
    except lite.Error:
        return False
    finally:    
        con.close()   

def build_user_prof_table(database):
    con = None
    try:
        con = lite.connect(database)
        with con:
            database_cursor = con.cursor()
            database_cursor.executescript(user_profile_table_script)
            con.commit()
            return True                  
    except lite.Error:
        return False
    finally:    
        con.close()    

def drop_user_prof_table(database):
    con = None
    try:
        con = lite.connect(database)
        with con:
            database_cursor = con.cursor()
            database_cursor.execute("DROP TABLE IF EXISTS userprofile;")
            con.commit()
            return True                  
    except lite.Error:
        return False
    finally:    
        con.close()  

def build_security_table(database):
    con = None
    try:
        con = lite.connect(database)
        with con:
            database_cursor = con.cursor()
            database_cursor.executescript(user_security_table_script)
            con.commit()
            return True                  
    except lite.Error:
        return False
    finally:    
        con.close()    

def drop_security_table(database):
    con = None
    try:
        con = lite.connect(database)
        with con:
            database_cursor = con.cursor()
            database_cursor.execute("DROP TABLE IF EXISTS security;")
            con.commit()
            return True                  
    except lite.Error:
        return False
    finally:    
        con.close()    

def drop_blog_table(database):
    con = None
    try:
        con = lite.connect(database)
        with con:
            database_cursor = con.cursor()
            database_cursor.execute("DROP TABLE IF EXISTS blog;")
            con.commit()
            return True                  
    except lite.Error:
        return False
    finally:    
        con.close()

def build_logs_table(database):
    con = None
    try:
        con = lite.connect(database)
        with con:
            database_cursor = con.cursor()
            database_cursor.executescript(log_table_script)
            con.commit()
            return True                  
    except lite.Error:
        return False
    finally:    
        con.close()    

def drop_logs_table(database):
    con = None
    try:
        con = lite.connect(database)
        with con:
            database_cursor = con.cursor()
            database_cursor.execute("DROP TABLE IF EXISTS log;")
            con.commit()
            return True                  
    except lite.Error:
        return False
    finally:    
        con.close()

def build_post_table(database):
    con = None
    try:
        con = lite.connect(database)
        with con:
            database_cursor = con.cursor()
            database_cursor.executescript(posts_table_script)
            con.commit()
            return True                  
    except lite.Error:
        return False
    finally:    
        con.close()    

def drop_post_table(database):
    con = None
    try:
        con = lite.connect(database)
        with con:
            database_cursor = con.cursor()
            database_cursor.execute("DROP TABLE IF EXISTS post;")
            con.commit()
            return True                  
    except lite.Error:
        return False
    finally:    
        con.close()
        
def build_comment_table(database):
    con = None
    try:
        con = lite.connect(database)
        with con:
            database_cursor = con.cursor()
            database_cursor.executescript(log_table_script)
            con.commit()
            return True                  
    except lite.Error:
        return False
    finally:    
        con.close()    

def drop_comment_table(database):
    con = None
    try:
        con = lite.connect(database)
        with con:
            database_cursor = con.cursor()
            database_cursor.execute("DROP TABLE IF EXISTS comment;")
            con.commit()
            return True                  
    except lite.Error:
        return False
    finally:    
        con.close()