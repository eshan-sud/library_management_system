import pymysql
Password_File = open('Library_Password.txt', 'r')
Password = Password_File.read()
Password_File.close()
connection = pymysql.connect(user = 'root', host = 'localhost', password = Password)
cursor = connection.cursor()

try:
    cursor.execute('USE WORLD_LIBRARY;')
    cursor.execute('DROP DATABASE WORLD_LIBRARY;')
except: pass
cursor.execute('CREATE DATABASE WORLD_LIBRARY;')
cursor.execute('USE WORLD_LIBRARY;')

#11111111111111111

try:
    cursor.execute('''
CREATE TABLE BOOKS(
BOOK_ID INT(4) PRIMARY KEY,
BOOK_NAME VARCHAR(20) NOT NULL,
AUTHOR VARCHAR(20) NOT NULL,
TOTAL_COPIES INT(3) NOT NULL,
ISSUED_COPIES INT(3));''')

except: pass

#22222222222222222

try:
    cursor.execute('''
CREATE TABLE MEMBERS(
MEMBER_ID INT(4) PRIMARY KEY,
PASSKEY VARCHAR(10) NOT NULL UNIQUE,
FIRST_NAME VARCHAR(10) NOT NULL,
MIDDLE_NAME VARCHAR(10),
LAST_NAME VARCHAR(10) NOT NULL,
GENDER VARCHAR(10) NOT NULL,
DOB DATE NOT NULL,
ADDRESS VARCHAR(30) NOT NULL,
BOOK_ID1 INT(4),
BOOK_ID2 INT(4),
BOOK_ID3 INT(4),
BOOK_ID4 INT(4));''')

except: pass

#33333333333333333

try:
    cursor.execute('''
CREATE TABLE ISSUE_DETAILS(
MEMBER_ID INT(4) NOT NULL,
BOOK_ID INT(4) NOT NULL,
ISSUED_DATE DATE NOT NULL,
DUE_DATE DATE NOT NULL,
RETURNED_DATE DATE,
RECORD_TYPE CHAR(6));''')
    #cursor.execute('ALTER TABLE ISSUE_DETAILS ADD FOREIGN KEY (BOOK_ID) REFERENCES BOOKS(BOOK_ID);')
    #cursor.execute('ALTER TABLE ISSUE_DETAILS ADD FOREIGN KEY (MEMBER_ID) REFERENCES MEMBERS(MEMBER_ID);')

except: pass

#44444444444444444

try:
    cursor.execute('''
INSERT INTO BOOKS VALUES
(1,'The Lost Tribe','Krish Dhanpriye',4,0),
(2,'How to Sew Buttons','Button Singh',10,1),
(3,'The Lonely Night','Hariram Jaiswaal',8,2),
(4,'Mindys Mittens','Newton',5,3),
(5,'Pizza & Donuts Diet','Aryan Gupta',4,2),
(6,'101 Cat House Plans','Dhriti Gupta',5,3),
(7,'Life for Dummies','Daniyal',6,3),
(8,'Land of Lemurs','Arsh Gupta',6,3),
(9,'Go For It!','Kinshuk',1,0),
(10,'101 Baby Names','Garv Kare Maze',6,3),
(11,'Farming for Nerds','Divyanshu Chalbaaz',4,0),
(12,'They Are Us','Eshita Gulati',2,1),
(13,'Here We Go!','Angus Gus',3,1),
(14,'Spanish for Nurses','Parth Kashap',3,1),
(15,'Tacos Everyday','Beckham Jimenez',5,1),
(16,'One Minute Rule','Ramu Kaka',7,4),
(17,'Apples to Oranges','Freya Harkin',6,3),
(18,'Tiger Mountain','King Inda North',5,3),
(19,'How Cookies Crumble','Dwayne Johnson',6,2),
(20,'Bridge to Yesterday','John Snow',3,3),
(21,'The Lemonade Stand','Ruskin Bond',5,2),
(22,'Hello World','Eshan Sud',10,6),
(23,'Yoga for Moms','Agatha Christie',3,0),
(24,'The Red Balloon','John Kennedy',5,2),
(25,'War of Words','Jack Black',7,2),
(26,'Harry Potter','Joanne Rowling',3,0);''')
    connection.commit()

except: pass

#55555555555555555

try:
    cursor.execute('''
INSERT INTO MEMBERS VALUES 
(1,'DBlto3WxV6','Suraj',NULL,'Palan','MALE','1966-07-21','83, BirenGarh, Jammu',2,10,12,20),
(2,'1dk9eYm8EK','Ram','Gopal','Madan','MALE','1981-09-04','82, Jamshed Nagar, Pondicherry',6,21,22,NULL),
(3,'16N2yKQdqa','Ricky',NULL,'Kata','MALE','1987-10-16','39, Heer Apartments Kolkata',21,4,25,22),
(4,'keKN4rjpmo','Mohit',NULL,'Parmer','MALE','2000-10-18','82, Virar, New Delhi',5,7,10,NULL),
(5,'kYk5r66S7W','Summer',NULL,'Brown','FEMALE','1991-12-02','49 Gleason Quadrant',8,7,14,19),
(6,'GEh9uIh3OD','Harry','Lily','Potter','Male','1980-07-31','4 Privet Drive',23,22,NULL,NULL),
(7,'YO5nS83Pad','Arlo',NULL,'White','MALE','1976-08-05','22 Moen Bend Port Leoraland',7,15,16,NULL),
(8,'jiVUHyEw6q','Charles',NULL,'Thompson','MALE','2003-08-25','784 Arden Norbertoview',16,18,NULL,NULL),
(9,'tG1Qar4Q8W','Alice',NULL,'Williams','FEMALE','2001-06-16','023A Janiya Clementine',10,17,NULL,NULL),
(10,'QDtGRb9u3I','Hannah','Mark','Wilson','FEMALE','2002-04-23','14B Tylerburgh',17,18,NULL,NULL),
(11,'8QToi6muc0','Grace',NULL,'Singh','OTHER','1982-06-08','0391 Boulevard, Sainte',16,NULL,NULL,NULL),
(12,'82mE1nUDj0','Arnav','Henry','Gupta','OTHER','1997-07-19','2627 Bureau 869',25,NULL,NULL,NULL),
(13,'GmOh6fpJSk','Benjamin',NULL,'Simard','MALE','1974-11-18','82035 Avenue',18,17,NULL,NULL),
(14,'Jeai1aEJGL','Alexander',NULL,'MacDonald','MALE','1988-01-25','023A Clementine',NULL,NULL,NULL,NULL),
(15,'028VajuMCn','Layla',NULL,'Bergeron','FEMALE','1983-06-01','791 Pont Marc',16,NULL,NULL,NULL),
(16,'jl4SbNMUdN','Joseph',NULL,'Mitchell','OTHER','1975-03-28','02 West',NULL,NULL,NULL,NULL),
(17,'zjMB0YzssP','Summer',NULL,'Thompson','OTHER','2003-04-18','51C Eden Meander',5,8,13,NULL),
(18,'ptlSs4mEnH','Arvind',NULL,'Baria','OTHER','1972-08-31','22143 Chemin Martine',20,22,NULL,NULL),
(19,'jcs7XbE7Cq','Tom','Marwalow','Riddle','Male','1974-03-14','69 Hartmannport',8,19,NULL,NULL),
(20,'uS2L5SH09k','Kusum',NULL,'Sood','FEMALE','1979-02-13','9 Rousseau',4,3,6,24),
(21,'vK8u08os7Q','Radheshyam',NULL,'Dixit','MALE','1968-04-05','31, Marathahalli Agra',22,NULL,NULL,NULL),
(22,'MFzjp40zUY','Amolika',NULL,'Mannan','FEMALE','1969-07-28','56, Churchgate, Agra',6,22,NULL,NULL),
(23,'4KtvmYVqx7','Bahadur',NULL,'Majumdar','MALE','1969-04-25','93, NarayanGunj, Raipur',3,20,NULL,NULL),
(24,'WqFVyaY6rC','Esha',NULL,'Dewan','FEMALE','1974-03-14','56, Anees Heights Mysore',4,24,NULL,NULL);''')
    connection.commit()
    
except: pass

#666666666666666666

try:
    cursor.execute('''
INSERT INTO ISSUE_DETAILS VALUES
(1,10,'2022-02-10','2022-03-12',NULL,'OPEN'),
(1,12,'2022-02-03','2022-03-5',NULL,'OPEN'),
(1,20,'2022-02-18','2022-03-20',NULL,'OPEN'),
(1,12,'2021-12-10','2022-01-15','2022-01-10','CLOSED'),
(2,6,'2022-01-12','2022-02-11',NULL,'OPEN'),
(2,21,'2021-09-18','2021-10-18',NULL,'OPEN'),
(2,22,'2022-04-10','2022-05-12',NULL,'OPEN'),
(2,8,'2022-01-30','2022-03-01',NULL,'OPEN'),
(3,21,'2021-01-15','2021-02-14',NULL,'OPEN'),
(3,4,'2021-03-09','2021-04-08',NULL,'OPEN'),
(3,25,'2021-04-20','2021-05-20',NULL,'OPEN'),
(3,10,'2020-04-20','2020-05-20','2020-04-29','CLOSED'),
(3,22,'2021-05-19','2021-04-8',NULL,'OPEN'),
(4,5,'2022-01-04','2022-02-03',NULL,'OPEN'),
(4,7,'2022-01-07','2022-02-06',NULL,'OPEN'),
(4,10,'2022-01-16','2022-02-15',NULL,'OPEN'),
(5,8,'2022-01-24','2022-02-23',NULL,'OPEN'),
(5,7,'2022-01-25','2022-02-24',NULL,'OPEN'),
(5,14,'2022-02-17','2022-03-19',NULL,'OPEN'),
(5,19,'2022-02-10','2022-03-12',NULL,'OPEN'),
(6,23,'2022-02-22','2022-03-24',NULL,'OPEN'),
(6,22,'2022-03-01','2022-03-31',NULL,'OPEN'),
(7,7,'2022-02-02','2022-03-04',NULL,'OPEN'),
(7,15,'2022-01-04','2022-02-03',NULL,'OPEN'),
(7,3,'2021-01-01','2021-01-31','2021-01-25','CLOSED'),
(7,16,'2022-02-03','2022-03-5',NULL,'OPEN'),
(8,16,'2022-01-04','2022-02-03',NULL,'OPEN'),
(8,18,'2022-02-02','2022-03-04',NULL,'OPEN'),
(9,10,'2022-03-01','2022-03-31',NULL,'OPEN'),
(15,6,'2021-05-30','2021-06-29','2021-06-27','CLOSED'),
(9,17,'2022-01-27','2022-02-26',NULL,'OPEN'),
(10,17,'2022-03-07','2022-04-06',NULL,'OPEN'),
(10,18,'2022-03-11','2022-04-10',NULL,'OPEN'),
(10,8,'2022-02-03','2022-03-5',NULL,'OPEN'),
(11,16,'2022-01-04','2022-02-03',NULL,'OPEN'),
(12,25,'2022-03-11','2022-04-10',NULL,'OPEN'),
(13,18,'2022-02-03','2022-03-5',NULL,'OPEN'),
(13,17,'2022-03-11','2022-04-10',NULL,'OPEN'),
(15,16,'2022-02-18','2022-03-20',NULL,'OPEN'),
(17,5,'2022-02-18','2022-03-20',NULL,'OPEN'),
(17,8,'2022-01-04','2022-02-03',NULL,'OPEN'),
(17,13,'2022-02-03','2022-03-05',NULL,'OPEN'),
(18,20,'2022-02-04','2022-03-06',NULL,'OPEN'),
(18,22,'2022-02-02','2022-03-04',NULL,'OPEN'),
(19,8,'2022-02-02','2022-03-04',NULL,'OPEN'),
(19,19,'2022-03-07','2022-04-06',NULL,'OPEN'),
(20,4,'2022-02-02','2022-03-04',NULL,'OPEN'),
(20,3,'2022-02-18','2022-03-20',NULL,'OPEN'),
(20,6,'2022-02-02','2022-03-04',NULL,'OPEN'),
(20,24,'2022-03-01','2022-03-31',NULL,'OPEN'),
(21,22,'2022-03-11','2022-04-10',NULL,'OPEN'),
(21,6,'2021-05-30','2021-06-29','2021-06-27','CLOSED'),
(22,6,'2022-02-03','2022-03-5',NULL,'OPEN'),
(22,22,'2022-02-18','2022-03-20',NULL,'OPEN'),
(3,20,'2022-03-07','2022-04-06',NULL,'OPEN'),
(24,4,'2022-02-02','2022-03-04',NULL,'OPEN'),
(24,24,'2022-02-03','2022-03-5',NULL,'OPEN');''')
    connection.commit()

except: pass

print('Database Intialised...')
