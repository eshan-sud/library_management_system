import pymysql

def admin():
    '''Performs The Functions Available To Admin'''
    Password = refresh_password()
    passkey = input('Enter Admin Password: ')
    if passkey == Password:
        global logged_as_admin
        logged_as_admin = True
        while True:
            print('''
 _______________________________
|                               |
| Logged In As Admin....        |
|_______________________________|
|                               |
| 1. Display All Books          |
| 2. Add New Book               |
| 3. Update Existing Book       |
| 4. Remove Book                |
| Search Book By :              |
|    5. Book ID                 |
|    6. Book Name               |
|    7. Author                  |
| Order Books By :              |
|    8. Number Of Copies        |
|    9. Number of Issued Copies |
| 10. Search Member Details     |
| 11. Update Member Details     |
| 12. Remove Member Details     |
| 13. Display Issue Details     |
|     Of Book                   |
| 14. Display Issue Details     |
|     Of Member                 |
| 15. Display Issue Details     |
|     Of Open Records           |
| 16. Display Issue Details     |
|     Of Closed Records         |
| 17. Change Admin Password     |
|                               |
| 18. Log Out                   |
|_______________________________|''')
            user = input('Enter One Of The Above Options(1,2,3,...,18): ')
            if user == '1': display_books()
            elif user == '2': add_book()
            elif user == '3': update_book()
            elif user == '4': remove_book()
            elif user == '5':
                parameter = input('\nEnter Book ID: ')
                if parameter.isdigit():
                    search = search_book(str(parameter))
                    if search: display_book(search)
                    else: print('Book Not Found!')
                else: print('Book ID Must Be An Integer!')
            elif user == '6':
                parameter = input('\nEnter Book Name: ')
                search = search_book(parameter)
                if search: display_book(search)
                else: print('Book Not Found!')
            elif user == '7':
                parameter = input(f'\nEnter Author: ')
                search = search_book(parameter)
                if search: display_book(search)
                else: print('Book Not Found!')
            elif user == '8': order_by('TOTAL_COPIES')
            elif user == '9': order_by('ISSUED_COPIES')
            elif user == '10':
                search = search_member()
                if search:display_member(search)
                else: print('Member Not Found!')
            elif user == '11':
                search = search_member()
                if search: update_member_details(search[0])
                else: print('Member Not Found!')
            elif user == '12': remove_member()
            elif user == '13': display_issue_details('book')
            elif user == '14': display_issue_details('member')
            elif user == '15': order_issue_details('OPEN')
            elif user == '16': order_issue_details('CLOSED')
            elif user == '17': change_password('ADMIN')
            elif user == '18': break
            else: print('Invalid Input!')
    else: print('Request Denied!\nIncorrect Password!\nPlease Try Again')

def member():
    '''Performs Functions Available To Member'''
    global logged_as_admin
    logged_as_admin = False
    member_details = search_member()
    if not(member_details): print('Request Denied!\nIncorrect Member ID Or Passkey!') ; return
    check_late_book(member_details)
    while member_details:
        member_id = member_details[0]
        member_details = refresh_member_details(member_id)
        print(f'''
 _________________________
|                         |
| Logged In As Member.... |
|_________________________|
|                         |
| 1. Display All Books    |
| 2. Issue Book           |
| 3. Return Book          |
| 4. Check Issued Books   |
| 5. Change Password      |
|                         |
| 6. Log Out              |
|_________________________|''')
        user = input('\nEnter One Of The Above Options(1,2,3): ')
        if user == '1': display_books()
        elif user == '2': issue_book(member_details)
        elif user == '3': return_book(member_details)
        elif user == '4': check_late_book(member_details)
        elif user == '5': change_password('MEMBER', member_details)
        elif user == '6': break
        else: print('Invalid Input!')
        
def create_member():
    '''Creates A New Mmeber'''
    cursor.execute('SELECT MEMBER_ID FROM MEMBERS ORDER BY MEMBER_ID;')
    member_id = cursor.fetchall()[-1][0] + 1
    print('\nEnter Your Details...')
    passkey = input('Passkey(=10 charactors)(leave blank for a random passkey): ')
    if not(passkey): passkey = generate_password()
    first_name = input('First Name(<=20 charactors): ')
    middle_name = input('Middle Name(<=20charactors)(if any): ')
    if not(middle_name) or middle_name.isspace(): middle_name = 'NULL'
    else: middle_name = "'" + middle_name + "'"
    last_name = input('Last Name: ')
    if not(last_name): print('Last Name Can Not Be Empty!') ; return
    gender = input('Gender(Male, Female, Other): ').upper()
    if gender not in ('MALE', 'FEMALE', 'OTHER'):
        print('Request Denied!\nInvalid Input Was Given!')
        return
    dob = input('Date Of Birth(YYYY-MM-DD): ')
    address = input('Address: ')
    SQL = f"INSERT INTO MEMBERS VALUES({member_id}, '{passkey}', '{first_name}', \
{middle_name}, '{last_name}', '{gender}', '{dob}', '{address}', NULL, NULL, NULL, NULL);"
    try: cursor.execute(SQL) ; connection.commit()
    except: print('Request Denied!\nInvalid Input Was Given!')
    else: print(f'Request Accepted!\n\nPlease Note: Your Member ID Is "{member_id}" And \
Passkey is "{passkey}"')

def search_member():
    '''Searches For A Member Using MEMBER_ID'''
    member_id = input('\nEnter Member ID: ')
    if member_id.isdigit():
        if logged_as_admin: SQL = f"SELECT * FROM MEMBERS WHERE MEMBER_ID = {member_id};"
        else:
            passkey = input('Passkey: ')
            SQL = f"SELECT * FROM MEMBERS WHERE MEMBER_ID = {member_id} AND PASSKEY = '{passkey}';"
        cursor.execute(SQL)
        return cursor.fetchone()
    else: print('Member ID Must Be An Integer!')

def refresh_member_details(member_id):
    ''''Refreshes The Given Member Details'''
    cursor.execute(f'SELECT * FROM MEMBERS WHERE MEMBER_ID = {member_id};')
    return cursor.fetchone()

def refresh_password():
    '''Refreshes The MySQL And Admin Password'''
    Password_File = open('Library_SQL_Password.txt', 'r')
    Password = Password_File.read()
    Password_File.close()
    return Password

def search_book(parameter):
    '''Searches For A Book Using BOOK_ID Or AUTHOR NAME'''
    if parameter.isdigit(): SQL = f"SELECT * FROM BOOKS WHERE BOOK_ID = {parameter};"
    else: SQL = f"SELECT * FROM BOOKS WHERE BOOK_NAME = '{parameter}' OR AUTHOR = '{parameter}'"
    cursor.execute(SQL)
    book_details = cursor.fetchone()
    return book_details

def update_member_details(member_id):
    '''Updates The Details Of An Existing Member'''
    while True:
        member_details = refresh_member_details(member_id)
        print('''
 __________________________
|                          |
| Update Member Details... |
|__________________________|
|                          |
| 1. First Name            |
| 2. Middle Name           |
| 3. Last Name             |
| 4. Address               |
| 5. Check Details         |
|                          |
| 6. Return To Admin Menu  |
|__________________________|''')
        user = input('Enter One Of The Above Options(1,2,3,4,5,6): ')
        old_detail = {'1':'FIRST_NAME', '2':'MIDDLE_NAME', '3':'LAST_NAME', '4':'ADDRESS'}
        if user == '1':
            new_name = input('New First Name(<= 20 charactors): ')
            if new_name.isspace() or not(new_name): print('New Name Can Not Be Empty!') ; break
            new_detail = f"'{new_name}'"
        elif user == '2':
            new_middle_name = input('\nNew Middle Name(<= 20 charactors)(if any): ')
            if not(new_middle_name) or new_middle_name.isspace(): new_detail = 'NULL'
            else: new_detail = f"'{new_middle_name}'"
        elif user == '3':
            new_last_name = input('\nNew Last Name(<= 20 charactors): ')
            if new_last_name.isspace() or not(new_last_name): print('New Last Name Can Not Be Empty!')
            new_detail = f"'{new_last_name}'"
        elif user == '4':
            new_address = {input('\nNew Address: ')}
            if new_address: print('Address Can Not Be Empty!')
            else: new_detail = f"'{new_address}'"
        elif user == '5':
            member_details = search_member()
            if member_details: display_member(member_details)
            else: print('Member Not Found!')
        elif user == '6': break
        else: print('Invalid Input!') ; break
        
        if user in '1234':
            cursor.execute(f"UPDATE MEMBERS SET {old_detail[user]} = {new_detail} \
WHERE MEMBER_ID = {member_details[0]};")
            connection.commit()
            print('Member Details Updated')

def add_book():
    '''Adds A Book To The Database'''
    cursor.execute('SELECT BOOK_ID FROM BOOKS ORDER BY BOOK_ID;')
    book_id = cursor.fetchall()[-1][-1] + 1
    print('\nEnter Book Details...')
    book_name = input('\nBook Name(<= 20 charactors): ')
    author = input('Author Name(<= 20 charactors): ')
    search1 = search_book(book_name)
    search2 = search_book(author)
    if search1 and search2: print('Request Denied!\nBook Already In Database!') ; return
    total_copies = input('Total Copies: ')
    issued_copies = 0
    if total_copies.isdigit():
        cursor.execute(f"INSERT INTO BOOKS VALUES ({book_id}, '{book_name}', '{author}', {total_copies},\
{issued_copies});")
        connection.commit()
        print(f'Book Added To Database\nBook ID Is {book_id}')
    else: print('Total Copies Should Be An Integer!') ; return

def display_books():
    '''Displays All The Books In The Database'''
    cursor.execute('SELECT * FROM BOOKS;')
    list_books = cursor.fetchall()
    for book_num in range(1, len(list_books) + 1):
        print(f'\nBOOK - {book_num}')
        display_book(list_books[book_num - 1])

def display_book(book):
    '''Displays The Details Of A Book'''
    print(f'''
Book ID          :   {book[0]}
Book Name        :   {book[1]}
Author           :   {book[2]}
Total Copies     :   {book[3]}
Issued Copies    :   {book[4]}''')

def display_member(member):
    '''Displays The Details Of A Member'''
    print(f'''
Member ID    :  {member[0]}
Passkey      :  {member[1]}
First Name   :  {member[2]}
Middle Name  :  {member[3]}
Last Name    :  {member[4]}
Gender       :  {member[5]}
DOB          :  {member[6]}
Address      :  {member[7]}
Book ID 1    :  {member[8]}
Book ID 2    :  {member[9]}
Book ID 3    :  {member[10]}
Book ID 4    :  {member[11]}''')

def update_book():
    '''Performs Functions Of Updating Member Details'''
    while True:
        print('''
 _____________________________
|                             |
| Update Menu....             |
|_____________________________|
|                             |
| 1. Book Name                |
| 2. Book Author              |
| 3. Total Copies             |
| 4. Issued Copies            |
|                             |
| 5. Return To The Admin Menu |
|_____________________________|''')
        user = input('\nEnter One Of The Above Options(1,2,3,4,5): ')
        if user == '5': break
        book_id = input('Book ID: ')
        if not(book_id.isdigit()): print('Book ID Must Be An Integer!') ; return
        book_details = search_book(book_id)
        if not(book_details): print('Book Not Found!') ; break
        print('\nBook Details In Database:')
        display_book(book_details)
        book_id, book_name, author, total_copies, issued_copies = book_details
        try:
            if user == '1': book_name = input('\nNew Book Name: ')
            elif user == '2': author = input('\nNew Author: ')
            elif user == '3': total_copies = int(input('\nNew Total Copies: '))
            elif user == '4': issued_copies = int(input('\nNew Issued Copies: '))
        except: print('Input Must Be An Integer!')
        try:
            SQL = f'UPDATE BOOKS SET BOOK_NAME = "{book_name}", AUTHOR = "{author}", \
TOTAL_COPIES = {total_copies}, ISSUED_COPIES = {issued_copies} WHERE BOOK_ID = {book_id};'
            cursor.execute(SQL)
            connection.commit()
            print('Book Details Updated')
        except:
            print('Request Denied!\nInvalid Input Was Given!')

def remove_book():
    '''Deletes An Existing Book From The Database'''
    book_id = input('\nEnter Book ID: ')
    cursor.execute(f'SELECT BOOK_ID1, BOOK_ID2, BOOK_ID3, BOOK_ID4 FROM MEMBERS;')
    issued_book_ids = cursor.fetchall()
    for issued_book_id in issued_book_ids:
        if book_id in issued_book_id:
            print('This Book Has Been Issued!\nPlease Try Again Later!')
            return
    else:
        cursor.execute(f'SELECT * FROM BOOKS WHERE BOOK_ID = {book_id};')
        book_database = cursor.fetchone()
        display_book(book_database)
        confirmation = input('Is This The Book You Were Looking For?(YES,NO): ').lower()
        if confirmation == 'no': print('Book Not Found')
        elif confirmation == 'yes':
            cursor.execute(f'DELETE FROM BOOKS WHERE BOOK_ID = {book_id};')
            cursor.execute(f'DELETE FROM ISSUE_DETAILS WHERE BOOK_ID = {book_id};')
            print('Book Removed From Database!')
            connection.commit()
        else: print('Invalid Input!')

def remove_member():
    '''Deletes An Existing Member From The Database'''
    member_details = search_member()
    member_id = member_details[0]
    cursor.execute(f"SELECT BOOK_ID1, BOOK_ID2, BOOK_ID3, BOOK_ID4 FROM MEMBERS \
WHERE MEMBER_ID = {member_id};")
    issued_books = cursor.fetchone()
    if issued_books != (None, None, None, None):
        print("Book(s) Have Been Issued By The Member!\nPlease Try Again Later!")
        return
    else:
        cursor.execute(f'DELETE FROM MEMBERS WHERE MEMBER_ID = {member_id};')
        cursor.execute(f'DELETE FROM ISSUE_DETAILS WHERE MEMBER_ID = {member_id};')
        print('Member Removed From Database!')
        connection.commit()

def order_by(condition):
    '''Displays Books In The Order Of TOTAL_COPIES Or ISSUED_COPIES'''
    cursor.execute(f'SELECT BOOK_NAME,TOTAL_COPIES,ISSUED_COPIES FROM BOOKS ORDER BY {condition};')
    books = cursor.fetchall()
    print('\nBook_Name        Total Copies  Issued Copies')
    for book in books:
        print(f'{book[0]:20}{book[1]:3}             {book[2]:3}')

def issue_book(member_details):
    '''Issues A Book For A Member'''
    member_id = member_details[0]
    if member_details[-4] and member_details[-3] and member_details[-2] and member_details[-1]:
        print('You Have Reached Your Limit To Issue Books!\nPlease Return Them First!') ; return
    cursor.execute('SELECT * FROM BOOKS;')
    book_name = input('\nBook Name: ')
    book_details = search_book(book_name)
    if not(book_details): print('\nBook Not Found!') ; return
    book_id, book_name, author = book_details[:3]
    confirmation = input(f'\nID: {book_id}\nName: {book_name}\nAuthor: {author}\
\nIs This The Book You Were Looking For(YES/NO): ').lower()
    if confirmation == 'no': print('Book Not Found!') ; return
    if book_details[-2] == book_details[-1] : print('All Copies Of This Book Have Already Been Issued!\
\nPlease Try Again Later!') ; return
    new_issued_copies = book_details[-1] + 1
    cursor.execute(f'UPDATE BOOKS SET ISSUED_COPIES = {new_issued_copies} WHERE BOOK_ID = {book_id};')
    connection.commit()
    for i in range(1,5):
        if member_details[-5:][i] == None:
            try:
                SQL = f'UPDATE MEMBERS SET BOOK_ID{i} = {book_id} WHERE MEMBER_ID = {member_id} \
AND BOOK_ID{i} IS NULL;'
                cursor.execute(SQL)
                connection.commit()
            except: pass
            print(f'{book_name.title()} Has Been Issued By You')
            due_date = open_rec_issue_details(member_id, book_id)
            print(f'\nNOTE : The Due Date For This Book Is {due_date}\n')
            return

def return_book(member_details):
    '''Returns A Book For A Member'''
    book_name = input('\nBook Name: ').title()
    book_details = search_book(book_name)
    if book_details:
        book_id = book_details[0]
        issued_books = member_details[-4:]
        if book_id not in issued_books: print('You Have Not Issued This Book!') ; return
        new_issued_copies = book_details[-1] - 1
        cursor.execute(f'UPDATE BOOKS SET ISSUED_COPIES = {new_issued_copies} WHERE BOOK_ID = {book_id};')
        connection.commit()
        ids = {'BOOK_ID1' : member_details[-4],
               'BOOK_ID2' : member_details[-3],
               'BOOK_ID3' : member_details[-2],
               'BOOK_ID4' : member_details[-1]}
        for k,v in ids.items():
            SQL = f'UPDATE MEMBERS SET {k} = NULL \
WHERE MEMBER_ID = {member_details[0]} AND {k} = {book_id};'
            cursor.execute(SQL)
        connection.commit()
        print(f'Book {book_name} Returned')
        close_rec_issue_details(member_details[0], book_id)
        connection.commit()
        cursor.execute(f'SELECT * FROM MEMBERS WHERE MEMBER_ID = {member_details[0]};')
        member_details = cursor.fetchone()
    else: print('Book Not Found!')

def check_late_book(member_details):
    '''Checks The Due Books For A Member'''
    import datetime
    todays_date = datetime.date.today()
    member_id = member_details[0]
    print('\nBooks Due:\n')
    book_ids = member_details[-4:]
    for book_id in book_ids:
        if book_id == None: continue
        SQL = f'SELECT * FROM ISSUE_DETAILS WHERE BOOK_ID = {book_id} AND MEMBER_ID = {member_id} \
AND RECORD_TYPE = "OPEN";'
        cursor.execute(SQL)
        issue_details = cursor.fetchone()
        if not(issue_details): continue
        due_date = issue_details[3]
        if todays_date <= due_date: print(f'Book ID {book_id} On Date {due_date}\n')
        elif todays_date > due_date:
            print(f'''Book ID {book_id} On Date {due_date}
You Have Missed The Due Date Of This Book
Kindly Return It At Once\n''')
    else: pass

def open_rec_issue_details(member_id, book_id):
    '''Opens A New Issue Detail For The Issued Book In The Database'''
    import datetime
    issue_date = datetime.date.today()
    due_date = issue_date + datetime.timedelta(30)
    SQL = f'INSERT INTO ISSUE_DETAILS (MEMBER_ID, BOOK_ID, ISSUED_DATE, DUE_DATE, RECORD_TYPE)\
VALUES ({member_id}, {book_id}, "{issue_date}", "{due_date}", "OPEN");'
    cursor.execute(SQL)
    connection.commit()
    return due_date

def close_rec_issue_details(member_id, book_id):
    '''Closes The Issue Details For The Returned Book In The Database'''
    import datetime
    returned_date = datetime.date.today()
    SQL = f'UPDATE ISSUE_DETAILS SET RETURNED_DATE = "{returned_date}", RECORD_TYPE = "CLOSED" \
WHERE MEMBER_ID = {member_id} AND BOOK_ID = {book_id};'
    cursor.execute(SQL)
    connection.commit()

def display_issue_details(parameter):
    '''Displays The Issue Details Of The Given Member Or Book'''
    if parameter == 'book':
        book_id = input('Book ID: ')
        details = search_book(book_id)
        if not(details): print('Record Not Found') ; return
        cursor.execute(f'SELECT * FROM ISSUE_DETAILS WHERE BOOK_ID = {details[0]};')
    elif parameter == 'member':
        details = search_member()
        if not(details): print('Record Not Found') ; return
        cursor.execute(f'SELECT * FROM ISSUE_DETAILS WHERE MEMBER_ID = {details[0]};')
    records = cursor.fetchall()
    for record in records:
        print(f'''
Member ID   : {record[0]}
Book ID     : {record[1]}
Issued Date : {record[2]}
Due Date    : {record[3]}
Returned    : {'Returned' if record[4] else 'Not Returned'}''')

def order_issue_details(record_type):
    '''Displays Those Records Whose Books Have Been Returned Or Whose Books Have Not Been Returned'''
    cursor.execute(f'SELECT * FROM ISSUE_DETAILS WHERE RECORD_TYPE = "{record_type}";')
    records = cursor.fetchall()
    for record in records:
        print(f'''
Member ID     : {record[0]}
Book ID       : {record[1]}
Issued Date   : {record[2]}
Due Date      : {record[3]}
Returned Date : {record[4] if record[4] else 'Not Returned'}''')

def generate_password(length_password = 10):
    '''Generates A Random Password'''
    import string
    import random
    set_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for number in range(length_password):
        password += random.choice(set_characters)
    return password

def change_password(parameter, member_details = ()):
    '''Changes Pasword Of ADMIN Or MEMBER'''
    if parameter == 'ADMIN':
        old_pass = input('Enter Old Password: ')
        Pass_File = open('Library_SQL_Password.txt', 'r+')
        Old_Pass_File = Pass_File.read()
        if old_pass != Old_Pass_File: print('Request Denied!\nInvalid Password Given!') ; return
        new_pass = input('Enter New Passord(<=10 charactors)(Leave Blank For A Random Password): ')
        if new_pass.isspace() or not(new_pass): new_pass = generate_password()
        Pass_File.seek(0)
        Pass_File.truncate(0)
        Pass_File.write(new_pass)
        Pass_File.close()
        cursor.execute(f"ALTER USER 'root'@'localhost' IDENTIFIED BY '{new_pass}';")
        cursor.execute('FLUSH PRIVILEGES;')
    elif parameter == 'MEMBER':
        member_id = member_details[0]
        old_pass = input('Enter Old Passkey: ')
        if old_pass != member_details[1]: print('Request Denied!\nIncorrect passkey!') ; return
        new_pass = input('Enter New Passkey(<=10 charactors)(Leave Blank For A Random Password): ')
        if new_pass.isspace() or not(new_pass): new_pass = generate_password()
        cursor.execute(f"UPDATE MEMBERS SET PASSKEY = '{new_pass}' WHERE MEMBER_ID = {member_id};")
        connection.commit()
    print(f"\nRequest Accepted\nNew Password Is '{new_pass}'")
    print(f'Please Restart The System For The Affect To Take Place...')

Password = refresh_password()
connection = pymysql.connect(user = 'root', host = 'localhost', password = Password)
cursor = connection.cursor()
cursor.execute('USE WORLD_LIBRARY;')
