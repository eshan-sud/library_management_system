____________________________________________________________________________________________________________________________________________________________________________

# Library Management System - World Library


Introducing a cutting-edge Command Line Interface(CLI)-based management system designed exclusively for libraries, empowering them to efficiently maintain and manage their records.
Additionally, this innovative platform offers users the convenience of checking out library books and tracking the time limit on their rented books with ease.


Built using Python programming language, MySQL database management language, file handling, pymysql, database management.


## How To Run


- Download both Python programming language & MySQL from their official website

  - Python : [https://www.python.org/downloads/]

  - MySQL  : [https://www.mysql.com/downloads/]

- <ins>Optional</ins> : To create a sample database execute Create_Sample_Database.py before executing Main.py

   Or

   Execute the following commands in the MySQL client:

         CREATE DATABASE WORLD_LIBRARY;

         USE WORLD_LIBRARY;
   
         CREATE TABLE BOOKS(
         BOOK_ID INT(4) PRIMARY KEY,
         BOOK_NAME VARCHAR(20) NOT NULL,
         AUTHOR VARCHAR(20) NOT NULL,
         TOTAL_COPIES INT(3) NOT NULL,
         ISSUED_COPIES INT(3));

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
         BOOK_ID4 INT(4));
      
         CREATE TABLE ISSUE_DETAILS(
         MEMBER_ID INT(4) NOT NULL,
         BOOK_ID INT(4) NOT NULL,
         ISSUED_DATE DATE NOT NULL,
         DUE_DATE DATE NOT NULL,
         RETURNED_DATE DATE,
         RECORD_TYPE CHAR(6));
   
- Download the files Main.py, Operations.py, Library_MySQL_Password.txt & <ins>Optional</ins> : Create_Sample_Database.py

  - (Put the same password of your MySQL account and note that this will be your Admin password as well)
   
- Execute Main.py to begin your program

____________________________________________________________________________________________________________________________________________________________________________

## Admin Operations:

Operations under the control of the Admin

i. Display All Books      

ii. Add New Book           

iii. Update Existing Book

iv. Remove Book      

v. Search Book By: Book ID

vi. Search Book By: Book Name

vii. Search Book By: Author

viii. Order Books By: Number of Total Copies

ix. Order Books By: Number of Issued Copies

x. Search Member Details

xi. Change Member Details

xii. Remove Member Details

xiii. Display Issue Details of Book

xiv. Display Issue Details Member

xv. Display Issue Details of Open Records

xvi. Display Issue Details of Closed Records

xvii. Change Admin Password

xviii. Log Out

## Member Operations:

Operations under the control of the Members

i. Display All Books

ii. Issue Book

iii. Return Book

iv. Check Issued Books

v. Change Password

Vi. Log Out
____________________________________________________________________________________________________________________________________________________________________________
