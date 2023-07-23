_____________________________________________________________________________________________________________________________________________________________________________

# Library Management System - World Library


Introducing a cutting-edge text-based management system designed exclusively for libraries, empowering them to efficiently maintain and manage their records. Additionally, this innovative platform offers users the convenience of checking out library books and tracking the time limit on their rented books with ease.


Built using Python programming language, MySQL database management language, file handling, pymysql, database management, etc.


## How To Run


1) Download both Python programming language & MySQL from their official website

   Python : [https://www.python.org/downloads/]

   MySQL  : [https://www.mysql.com/downloads/]

2) <ins>Optional</ins> : To create a sample database execute Create_Sample_Database.py before executing Main.py

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
   
4) Download the files Main.py, Operations.py, Library_MySQL_Password.txt & <ins>Optional</ins> : Create_Sample_Database.py

   (Put the same password of your MySQL account and note that this will be your Admin password as well)
   
5) Execute Main.py to begin your program


## Stored Data

_____________________________________________________________________________________________________________________________________________________________________________

Type Of Data : .txt File

Data In File : <MySQL Password (Same as Admin Password)>

_____________________________________________________________________________________________________________________________________________________________________________

Type Of Data : MySQL Database

Database Name : WORLD_LIBRARY

Table-1: BOOKS

![image](https://github.com/eshan-sud/library_management_system/assets/113531303/7d685cf0-568e-46ac-a0f6-91a4b648aa5f)

Table-2: MEMBERS

![image](https://github.com/eshan-sud/library_management_system/assets/113531303/f258a9ac-6fb1-441a-9328-67e9b561595a)

Table-3: ISSUE_DETAILS

![image](https://github.com/eshan-sud/library_management_system/assets/113531303/a8a0a350-fd97-4c91-921f-1e7b58a53f60)

_____________________________________________________________________________________________________________________________________________________________________________

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
_____________________________________________________________________________________________________________________________________________________________________________
