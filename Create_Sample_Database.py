import pymysql
Password_File = open('Library_MySQL_Password.txt', 'r')
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

print('Database Intialised...')
