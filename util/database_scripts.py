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
    `profilephoto`      TEXT DEFAULT '../static/img/default-profile.png',
    `consoles`          TEXT DEFAULT '',
    `genres`            TEXT DEFAULT '',
    `xbxgt`             TEXT DEFAULT '',
    `plsgt`             TEXT DEFAULT '',
    `stmgt`             TEXT DEFAULT '',
    `coverphoto`        TEXT DEFAULT '../static/img/default-bg.png'
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

posts_table_script = """
    CREATE TABLE "post" (
    `ID`            INTEGER PRIMARY KEY AUTOINCREMENT,
    `text`          TEXT NOT NULL,
    `likes`         INTEGER default 0,
    `userID`        TEXT NOT NULL,
    `datetime`      TEXT NOT NULL
    );
    """   

comments_table_script = """
    CREATE TABLE "comment" (
    `ID`            INTEGER PRIMARY KEY AUTOINCREMENT,
    `postID`        TEXT NOT NULL,
    `text`          TEXT NOT NULL,
    `likes`         INTEGER default 0,
    `userID`        TEXT NOT NULL
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
    DROP TABLE IF EXISTS "post";
    DROP TABLE IF EXISTS "comment";
    DROP TABLE IF EXISTS "log";
    DROP TABLE IF EXISTS "forgotpassword";
    """

clear_all_tables_script = """
    DELETE FROM "user";
    DELETE FROM "userprofile";
    DELETE FROM "security";
    DELETE FROM "post";
    DELETE FROM "comment";
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

TEST_stream_insert = """
insert into post (id, text, likes, userID, datetime) values (1, 'Ruby', 298, 'pg_RR53SDDOEFGDP93', 1692135743);
insert into post (id, text, likes, userID, datetime) values (2, 'Craig', 241, 'pg_RR53SDDOEFGDP93', 1493400991);
insert into post (id, text, likes, userID, datetime) values (3, 'Todd', 478, 'pg_RR53SDDOEFGDP93', 1822486777);
insert into post (id, text, likes, userID, datetime) values (4, 'Jimmy', 414, 'pg_RR53SDDOEFGDP93', 1727868165);
insert into post (id, text, likes, userID, datetime) values (5, 'Johnny', 311, 'pg_RR53SDDOEFGDP93', 1795160552);
insert into post (id, text, likes, userID, datetime) values (6, 'Eric', 486, 'pg_RR53SDDOEFGDP93', 1920617886);
insert into post (id, text, likes, userID, datetime) values (7, 'Clarence', 366, 'pg_RR53SDDOEFGDP93', 1584756159);
insert into post (id, text, likes, userID, datetime) values (8, 'Katherine', 55, 'pg_RR53SDDOEFGDP93', 1623020654);
insert into post (id, text, likes, userID, datetime) values (9, 'Dennis', 141, 'pg_RR53SDDOEFGDP93', 1478609225);
insert into post (id, text, likes, userID, datetime) values (10, 'Carl', 489, 'pg_RR53SDDOEFGDP93', 1594631473);
insert into post (id, text, likes, userID, datetime) values (11, 'Amanda', 246, 'pg_RR53SDDOEFGDP93', 1554033595);
insert into post (id, text, likes, userID, datetime) values (12, 'Victor', 151, 'pg_RR53SDDOEFGDP93', 1900571477);
insert into post (id, text, likes, userID, datetime) values (13, 'Benjamin', 491, 'pg_RR53SDDOEFGDP93', 1599980171);
insert into post (id, text, likes, userID, datetime) values (14, 'Alice', 461, 'pg_RR53SDDOEFGDP93', 1942642402);
insert into post (id, text, likes, userID, datetime) values (15, 'Craig', 461, 'pg_RR53SDDOEFGDP93', 1946219110);
insert into post (id, text, likes, userID, datetime) values (16, 'Mary', 62, 'pg_RR53SDDOEFGDP93', 1874041618);
insert into post (id, text, likes, userID, datetime) values (17, 'Catherine', 489, 'pg_RR53SDDOEFGDP93', 1492066963);
insert into post (id, text, likes, userID, datetime) values (18, 'Donna', 375, 'pg_RR53SDDOEFGDP93', 1887045348);
insert into post (id, text, likes, userID, datetime) values (19, 'Diana', 116, 'pg_RR53SDDOEFGDP93', 1708227537);
insert into post (id, text, likes, userID, datetime) values (20, 'Steven', 246, 'pg_RR53SDDOEFGDP93', 1816856086);
insert into post (id, text, likes, userID, datetime) values (21, 'Lori', 331, 'pg_RR53SDDOEFGDP93', 1601198028);
insert into post (id, text, likes, userID, datetime) values (22, 'Diana', 461, 'pg_RR53SDDOEFGDP93', 1776626247);
insert into post (id, text, likes, userID, datetime) values (23, 'Robin', 359, 'pg_RR53SDDOEFGDP93', 1962824446);
insert into post (id, text, likes, userID, datetime) values (24, 'Lisa', 75, 'pg_RR53SDDOEFGDP93', 1579148381);
insert into post (id, text, likes, userID, datetime) values (25, 'Judy', 379, 'pg_RR53SDDOEFGDP93', 1962563190);
insert into post (id, text, likes, userID, datetime) values (26, 'Brandon', 56, 'pg_RR53SDDOEFGDP93', 1685099111);
insert into post (id, text, likes, userID, datetime) values (27, 'Jean', 348, 'pg_RR53SDDOEFGDP93', 1657282442);
insert into post (id, text, likes, userID, datetime) values (28, 'Helen', 384, 'pg_RR53SDDOEFGDP93', 1937948347);
insert into post (id, text, likes, userID, datetime) values (29, 'Deborah', 49, 'pg_RR53SDDOEFGDP93', 1778004495);
insert into post (id, text, likes, userID, datetime) values (30, 'Harry', 209, 'pg_RR53SDDOEFGDP93', 1695063443);
insert into post (id, text, likes, userID, datetime) values (31, 'Helen', 334, 'pg_RR53SDDOEFGDP93', 1864187885);
insert into post (id, text, likes, userID, datetime) values (32, 'Russell', 155, 'pg_RR53SDDOEFGDP93', 1667526684);
insert into post (id, text, likes, userID, datetime) values (33, 'Michael', 10, 'pg_RR53SDDOEFGDP93', 1852195165);
insert into post (id, text, likes, userID, datetime) values (34, 'Jose', 451, 'pg_RR53SDDOEFGDP93', 1827749125);
insert into post (id, text, likes, userID, datetime) values (35, 'Cynthia', 66, 'pg_RR53SDDOEFGDP93', 1635374342);
insert into post (id, text, likes, userID, datetime) values (36, 'Raymond', 186, 'pg_RR53SDDOEFGDP93', 1965356200);
insert into post (id, text, likes, userID, datetime) values (37, 'Harold', 355, 'pg_RR53SDDOEFGDP93', 1824070348);
insert into post (id, text, likes, userID, datetime) values (38, 'Gloria', 459, 'pg_RR53SDDOEFGDP93', 1628356388);
insert into post (id, text, likes, userID, datetime) values (39, 'Jane', 7, 'pg_RR53SDDOEFGDP93', 1554878145);
insert into post (id, text, likes, userID, datetime) values (40, 'Virginia', 65, 'pg_RR53SDDOEFGDP93', 1650395542);
insert into post (id, text, likes, userID, datetime) values (41, 'Rachel', 478, 'pg_RR53SDDOEFGDP93', 1791554772);
insert into post (id, text, likes, userID, datetime) values (42, 'Barbara', 475, 'pg_RR53SDDOEFGDP93', 1942415981);
insert into post (id, text, likes, userID, datetime) values (43, 'Victor', 483, 'pg_RR53SDDOEFGDP93', 1837291073);
insert into post (id, text, likes, userID, datetime) values (44, 'Christina', 251, 'pg_RR53SDDOEFGDP93', 1650564446);
insert into post (id, text, likes, userID, datetime) values (45, 'Christina', 245, 'pg_RR53SDDOEFGDP93', 1625550058);
insert into post (id, text, likes, userID, datetime) values (46, 'Maria', 21, 'pg_RR53SDDOEFGDP93', 1766588624);
insert into post (id, text, likes, userID, datetime) values (47, 'Kathryn', 496, 'pg_RR53SDDOEFGDP93', 1567856880);
insert into post (id, text, likes, userID, datetime) values (48, 'Judy', 247, 'pg_RR53SDDOEFGDP93', 1943451916);
insert into post (id, text, likes, userID, datetime) values (49, 'Larry', 337, 'pg_RR53SDDOEFGDP93', 1964885188);
insert into post (id, text, likes, userID, datetime) values (50, 'Debra', 471, 'pg_RR53SDDOEFGDP93', 1544379475);
insert into post (id, text, likes, userID, datetime) values (51, 'John', 215, 'pg_RR53SDDOEFGDP93', 1648481437);
insert into post (id, text, likes, userID, datetime) values (52, 'Debra', 377, 'pg_RR53SDDOEFGDP93', 1714360050);
insert into post (id, text, likes, userID, datetime) values (53, 'Charles', 17, 'pg_RR53SDDOEFGDP93', 1958357171);
insert into post (id, text, likes, userID, datetime) values (54, 'Ashley', 479, 'pg_RR53SDDOEFGDP93', 1860708446);
insert into post (id, text, likes, userID, datetime) values (55, 'Harry', 58, 'pg_RR53SDDOEFGDP93', 1684105612);
insert into post (id, text, likes, userID, datetime) values (56, 'Roger', 195, 'pg_RR53SDDOEFGDP93', 1871077734);
insert into post (id, text, likes, userID, datetime) values (57, 'Alan', 462, 'pg_RR53SDDOEFGDP93', 1510136448);
insert into post (id, text, likes, userID, datetime) values (58, 'Heather', 277, 'pg_RR53SDDOEFGDP93', 1564868235);
insert into post (id, text, likes, userID, datetime) values (59, 'Lawrence', 95, 'pg_RR53SDDOEFGDP93', 1730302920);
insert into post (id, text, likes, userID, datetime) values (60, 'Dorothy', 496, 'pg_RR53SDDOEFGDP93', 1869108489);
insert into post (id, text, likes, userID, datetime) values (61, 'Chris', 76, 'pg_RR53SDDOEFGDP93', 1552088065);
insert into post (id, text, likes, userID, datetime) values (62, 'Henry', 53, 'pg_RR53SDDOEFGDP93', 1936723706);
insert into post (id, text, likes, userID, datetime) values (63, 'Timothy', 51, 'pg_RR53SDDOEFGDP93', 1486927986);
insert into post (id, text, likes, userID, datetime) values (64, 'Amanda', 90, 'pg_RR53SDDOEFGDP93', 1789096846);
insert into post (id, text, likes, userID, datetime) values (65, 'Doris', 142, 'pg_RR53SDDOEFGDP93', 1691730914);
"""