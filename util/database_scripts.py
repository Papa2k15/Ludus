user_table_script = """
    CREATE TABLE "user" (
    'ID'                TEXT PRIMARY KEY,
    `firstname`         TEXT NOT NULL,
    `lastname`          TEXT NOT NULL,
    `email`             TEXT UNIQUE NOT NULL,
    `username`          TEXT UNIQUE NOT NULL,
    `dateofbirth`       TEXT NOT NULL,
    `gender`            TEXT NOT NULL,    
    `membersince`       TEXT NOT NULL    
    );
    """

forget_password_table_script = """
    CREATE TABLE "forgotpassword" (
    `userid`             TEXT DEFAULT '',
    `resetkey`           TEXT DEFAULT ''
    );
    """

user_profile_table_script = """
    CREATE TABLE "userprofile" (
    'ID'                TEXT PRIMARY KEY,
    `biography`         TEXT DEFAULT '',
    `profilephoto`      TEXT DEFAULT '',
    `consoles`          TEXT DEFAULT '',
    `genres`            TEXT DEFAULT '',
    `xbxgt`             TEXT DEFAULT '',
    `plsgt`             TEXT DEFAULT '',
    `stmgt`             TEXT DEFAULT ''
    );
    """

user_security_table_script = """
    CREATE TABLE "security" (
    `userid`            TEXT NOT NULL UNIQUE,
    `password`          TEXT NOT NULL,
    `showonline`        TEXT NOT NULL DEFAULT '1',
    `lastlogin`         TEXT
    );
    """   

log_table_script = """
    CREATE TABLE "log" (
    'ID'              INTEGER PRIMARY KEY AUTOINCREMENT,
    `event`           TEXT NOT NULL,
    `eventdate`       TEXT NOT NULL,
    `eventtime`       TEXT NOT NULL,
    `userid`          TEXT NOT NULL
    );
    """
 
drop_all_tables_script = """
    DROP TABLE IF EXISTS "user";
    DROP TABLE IF EXISTS "userprofile";
    DROP TABLE IF EXISTS "security";
    DROP TABLE IF EXISTS "log";
    DROP TABLE IF EXISTS "forgotpassword";
    """

clear_all_tables_script = """
    DELETE FROM "user";
    DELETE FROM "userprofile";
    DELETE FROM "security";
    DELETE FROM "log";
    DELETE FROM "forgotpassword";
    """

#Insert Test data
TEST_user_inserts = """
insert into user (ID, firstname, lastname, email, username, dateofbirth, gender, membersince) values ('pg_E634B2B4N11UG0U', 'Jack', 'Elliott', 'jelliott0@unesco.org', 'jelliott0', '526021307', 'male', '1467432000');
insert into user (ID, firstname, lastname, email, username, dateofbirth, gender, membersince) values ('pg_RR53SDDOEFGDP93', 'Gregory', 'Daniels', 'gldaniel@ncsu.edu', 'papa2k15', '740116800', 'male', '1467432000');
"""

TEST_user_prof_insert = """
insert into userprofile (ID, biography) values ('pg_E634B2B4N11UG0U', 'neque vestibulum eget vulputate ut ultrices vel augue vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere');
insert into userprofile (ID, biography) values ('pg_RR53SDDOEFGDP93', 'diam neque vestibulum eget vulputate ut ultrices vel augue vestibulum ante ipsum primis in faucibus orci luctus');
"""

TEST_user_sec_insert = """
insert into security (userid, password) values ('pg_E634B2B4N11UG0U','8c6f66b742021eabac66922cd45a6240');
insert into security (userid, password) values ('pg_RR53SDDOEFGDP93','8c6f66b742021eabac66922cd45a6240');
"""