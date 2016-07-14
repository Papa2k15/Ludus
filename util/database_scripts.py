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

likes_table_script = """
    CREATE TABLE "like" (
    `ID`            INTEGER PRIMARY KEY AUTOINCREMENT,
    `postID`        TEXT NOT NULL,
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
    DROP TABLE IF EXISTS "like";
    DROP TABLE IF EXISTS "log";
    DROP TABLE IF EXISTS "forgotpassword";
    """

clear_all_tables_script = """
    DELETE FROM "user";
    DELETE FROM "userprofile";
    DELETE FROM "security";
    DELETE FROM "post";
    DELETE FROM "like";
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
insert into post (ID, text, userID, likes, datetime) values (1, 'metus arcu adipiscing molestie hendrerit at vulputate vitae nisl aenean lectus pellentesque eget nunc donec quis orci eget orci vehicula condimentum curabitur in libero ut massa volutpat convallis morbi odio odio elementum eu interdum eu tincidunt in leo maecenas pulvinar lobortis est phasellus sit amet erat nulla tempus vivamus in felis eu sapien cursus vestibulum proin eu mi nulla ac enim in tempor turpis nec euismod', 'pg_RR53SDDOEFGDP93', 14, 1468044759);
insert into post (ID, text, userID, likes, datetime) values (2, 'nibh in quis justo maecenas rhoncus aliquam lacus morbi quis tortor id nulla ultrices aliquet maecenas leo odio condimentum id luctus nec molestie sed justo pellentesque viverra pede ac diam cras pellentesque volutpat dui maecenas tristique est et tempus semper est quam pharetra magna ac consequat metus sapien ut nunc vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae mauris viverra', 'pg_RR53SDDOEFGDP93', 18, 1468051643);
insert into post (ID, text, userID, likes, datetime) values (3, 'non quam nec dui luctus rutrum nulla tellus in sagittis dui vel nisl duis ac nibh fusce lacus purus aliquet at feugiat non pretium quis lectus suspendisse potenti in eleifend quam a odio in hac habitasse platea dictumst maecenas ut massa quis augue luctus tincidunt nulla mollis molestie lorem quisque ut erat curabitur gravida nisi at nibh in hac habitasse platea dictumst aliquam augue quam sollicitudin vitae consectetuer eget', 'pg_RR53SDDOEFGDP93', 50, 1468066804);
insert into post (ID, text, userID, likes, datetime) values (4, 'in faucibus orci luctus et ultrices posuere cubilia curae donec pharetra magna vestibulum aliquet ultrices erat tortor sollicitudin mi sit amet lobortis sapien sapien non mi integer ac neque duis bibendum morbi non quam nec dui luctus rutrum nulla tellus in sagittis dui vel nisl duis ac nibh fusce lacus purus aliquet at feugiat non pretium quis lectus suspendisse potenti', 'pg_RR53SDDOEFGDP93', 12, 1468067998);
insert into post (ID, text, userID, likes, datetime) values (5, 'laoreet ut rhoncus aliquet pulvinar sed nisl nunc rhoncus dui vel sem sed sagittis nam congue risus semper porta volutpat quam pede lobortis ligula sit amet eleifend pede libero quis orci nullam molestie nibh in lectus pellentesque at nulla suspendisse potenti cras in purus eu magna vulputate luctus cum sociis natoque penatibus et magnis dis parturient montes nascetur ridiculus mus vivamus vestibulum', 'pg_RR53SDDOEFGDP93', 34, 1468050719);
insert into post (ID, text, userID, likes, datetime) values (6, 'eget eleifend luctus ultricies eu nibh quisque id justo sit amet sapien dignissim vestibulum vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae nulla dapibus dolor vel est donec odio justo sollicitudin ut suscipit a feugiat et eros vestibulum ac est lacinia nisi venenatis tristique fusce congue diam id ornare imperdiet sapien urna pretium nisl ut volutpat sapien arcu sed augue aliquam erat', 'pg_RR53SDDOEFGDP93', 24, 1468056738);
insert into post (ID, text, userID, likes, datetime) values (7, 'vestibulum sed magna at nunc commodo placerat praesent blandit nam nulla integer pede justo lacinia eget tincidunt eget tempus vel pede morbi porttitor lorem id ligula suspendisse ornare consequat lectus in est risus auctor sed tristique in tempus sit amet sem fusce consequat nulla nisl nunc nisl duis bibendum felis sed interdum venenatis turpis enim blandit mi in porttitor pede justo eu massa donec dapibus duis at velit eu est', 'pg_RR53SDDOEFGDP93', 17, 1468050966);
insert into post (ID, text, userID, likes, datetime) values (8, 'ut nulla sed accumsan felis ut at dolor quis odio consequat varius integer ac leo pellentesque ultrices mattis odio donec vitae nisi nam ultrices libero non mattis pulvinar nulla pede ullamcorper augue a suscipit nulla elit ac nulla sed vel enim sit amet nunc viverra dapibus nulla suscipit ligula in', 'pg_RR53SDDOEFGDP93', 21, 1468055556);
insert into post (ID, text, userID, likes, datetime) values (9, 'montes nascetur ridiculus mus etiam vel augue vestibulum rutrum rutrum neque aenean auctor gravida sem praesent id massa id nisl venenatis lacinia aenean sit amet justo morbi ut odio cras mi pede malesuada in imperdiet et commodo vulputate justo in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices phasellus id sapien in sapien iaculis congue vivamus metus', 'pg_RR53SDDOEFGDP93', 41, 1468057293);
insert into post (ID, text, userID, likes, datetime) values (10, 'gravida sem praesent id massa id nisl venenatis lacinia aenean sit amet justo morbi ut odio cras mi pede malesuada in imperdiet et commodo vulputate justo in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices phasellus id sapien in sapien iaculis congue vivamus metus arcu adipiscing molestie hendrerit at vulputate vitae nisl aenean lectus pellentesque eget nunc donec quis', 'pg_RR53SDDOEFGDP93', 14, 1468066110);
insert into post (ID, text, userID, likes, datetime) values (11, 'tincidunt eget tempus vel pede morbi porttitor lorem id ligula suspendisse ornare consequat lectus in est risus auctor sed tristique in tempus sit amet sem fusce consequat nulla nisl nunc nisl duis bibendum felis sed interdum venenatis turpis enim blandit mi in porttitor pede justo eu massa donec dapibus duis at velit eu est congue elementum in hac habitasse platea dictumst morbi vestibulum velit id', 'pg_RR53SDDOEFGDP93', 41,  1468058818);
insert into post (ID, text, userID, likes, datetime) values (12, 'quisque porta volutpat erat quisque erat eros viverra eget congue eget semper rutrum nulla nunc purus phasellus in felis donec semper sapien a libero nam dui proin leo odio porttitor id consequat in consequat ut nulla sed accumsan felis ut at dolor quis odio consequat varius integer ac leo pellentesque ultrices', 'pg_RR53SDDOEFGDP93', 16, 1468049627);
insert into post (ID, text, userID, likes, datetime) values (13, 'pellentesque ultrices phasellus id sapien in sapien iaculis congue vivamus metus arcu adipiscing molestie hendrerit at vulputate vitae nisl aenean lectus pellentesque eget nunc donec quis orci eget orci vehicula condimentum curabitur in libero ut massa volutpat convallis morbi odio odio elementum eu interdum eu tincidunt in leo maecenas pulvinar lobortis est phasellus', 'pg_RR53SDDOEFGDP93', 5, 1468069899);
insert into post (ID, text, userID, likes, datetime) values (14, 'feugiat non pretium quis lectus suspendisse potenti in eleifend quam a odio in hac habitasse platea dictumst maecenas ut massa quis augue luctus tincidunt nulla mollis molestie lorem quisque ut erat curabitur gravida nisi at nibh in hac habitasse platea dictumst aliquam augue quam sollicitudin vitae consectetuer eget rutrum at lorem integer tincidunt ante vel ipsum praesent blandit lacinia erat', 'pg_RR53SDDOEFGDP93', 48, 1468044923);
insert into post (ID, text, userID, likes, datetime) values (15, 'lorem vitae mattis nibh ligula nec sem duis aliquam convallis nunc proin at turpis a pede posuere nonummy integer non velit donec diam neque vestibulum eget vulputate ut ultrices vel augue vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae donec pharetra magna vestibulum aliquet ultrices erat tortor sollicitudin mi sit amet lobortis sapien sapien non', 'pg_RR53SDDOEFGDP93', 40, 1468068235);
"""