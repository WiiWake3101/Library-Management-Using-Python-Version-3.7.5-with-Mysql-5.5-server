import mysql.connector
import datetime
mydb=mysql.connector.connect(user='root',password='3101',host='localhost',database='pps_mini_project')
mycursor=mydb.cursor()

def registermem():
    L=[]
    print("="*140)
    print("Registration for New Members".center(140))
    name=input("Enter Name:\t")
    L.append(name)
    phone=input("Enter Phone No:\t")
    L.append(phone)
    email_id=input("Enter Email-Id:\t")
    memeber_since= datetime.date.today()
    L.append(memeber_since) 
    cust=(L)
    sql="insert into customer_info(name,phone,email_id,member_since)values(%s,%s,%s,%s)"
    mycursor.execute(sql,cust)
    mydb.commit()
    print("Registered successfully !!".center(140))
    print("="*140)

def memview():
    print("="*140)
    print("Member's registred Info".center(140))
    print("\nDo you want to see all members?? - press 1")
    print("\nDo you want to see specific members?? - press 2")
    ch=int(input("\nEnter 1 or 2 :\t"))
    if ch==1:
        sql="select * from customer_info"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        print("="*140)
        print("All Member Information".center(140))
        for x in rows:
            print("Members No:",x[0])
            print("Name:",x[1])
            print("Phone Number:",x[2])
            print("Email-Id:",x[3])
            print("Member Since:",x[4])
            print("\n")
        print("="*140)
    elif ch==2:
        l=[]
        mem_id=int(input("Enter Member's No to fetch the details about it :\t"))
        l.append(mem_id)
        view=(l)
        sql="select * from customer_info where member_no=%s"
        mycursor.execute(sql,view)
        rows=mycursor.fetchone()
        if(rows!=None):
            print("="*140)
            print("Member No:",rows[0])
            print("Name:",rows[1])
            print("Phone Number:",rows[2])
            print("Email-Id:",rows[3])
            print("Member Since:",rows[4])
            print("="*140)
        else:
            print("="*140)
            print("No Member Found!!".center(140))
            print("="*140)
    else:
        print("Table viewation was cancelled")


def updatememberinfo():
     print("="*140)
     print("Updation Section".center(140))
     print("\nDo you want to see Member's Data available??")
     ch=int(input("\nEnter 1 for yes :\t"))
     if ch==1:
         sql="select * from customer_info"
         mycursor.execute(sql)
         rows=mycursor.fetchall()
         print("\nShowing Members info......")
         print("\n")
         for x in rows:
            print("Members No:",x[0])
            print("Name:",x[1])
            print("Phone Number:",x[2])
            print("Email-Id:",x[3])
            print("Member Since:",x[4])
            print("\n")
         print("="*140)
         print("\nDo you want to Update Member's info??")
         ch1=int(input("\nEnter 1 for yes :\t"))
         if ch1==1:
                  print("="*140)
                  print("Updation Menu".center(140))
                  print("\nenter 1 : To Update Member's Name")
                  print("\nenter 2 : To Update Member's Phone No")
                  print("\nenter 3 : To Update Member's Email-Id")
                  ch2=int(input("\nenter your choice:\t"))
                  if ch2==1:
                    L=[]
                    print("*"*140)
                    print("Name Updation".center(140))
                    name=input("\nEnter New Name to be updated:\t")
                    L.append(name)
                    memid=int(input("\nEnter the Member No from the above table display:\t"))
                    L.append(memid)
                    sql="update customer_info set Name=%s where Member_no=%s"
                    updation=(L)
                    mycursor.execute(sql,updation)
                    mydb.commit()
                    print("Updation Done!!".center(140))
                  elif ch2==2:
                    L=[]
                    print("*"*140)
                    print("Phone Number Updation".center(140))
                    phone_new=input("\nEnter New phone no to be updated\t")
                    L.append(phone_new)
                    memid=int(input("\nEnter the Member No from the above table display:\t"))
                    L.append(memid)
                    sql="update customer_info set phone=%s where Member_no=%s"
                    updation=(L)
                    mycursor.execute(sql,updation)
                    mydb.commit()
                    print("Updation Done!!".center(140))
                  elif ch2==3:
                      L=[]
                      print("*"*140)
                      print("Email-Id Updation".center(140))
                      email_id_new=input("\nEnter New Email Id for Updation:\t")
                      L.append(email_id_new)
                      memid=int(input("\nEnter the Member No from the above table display:\t"))
                      L.append(memid)
                      sql="update customer_info set email_id=%s where Member_no=%s"
                      updation=(L)
                      mycursor.execute(sql,updation)
                      mydb.commit()
                      print("Updation Done!!".center(140))
                  else:
                      print("\nSorry for the Conivence we have only four choices :) ")
                      print("\nplease enter your the correct choice from the updation!!\t")

def deletememinfo():
    print("="*140)
    print("Deletion of Member info".center(140))
    print("\nDo you want to see available??- press 1")
    print("\nDo you want to Exit this menu - press 0")
    ch=int(input("\nEnter 1 or 0 :\t"))
    if ch==1:
         sql="select * from customer_info"
         mycursor.execute(sql)
         rows=mycursor.fetchall()
         for x in rows:
            print("Members No:",x[0])
            print("Name:",x[1])
            print("Phone Number:",x[2])
            print("Email-Id:",x[3])
            print("Member Since:",x[4])
            print("\n")   
         print("="*140)    
         print("\nDo you want to Delete specific Member data??")
         ch1=int(input("\nEnter 1 for yes :\t"))
         if ch1==1:
              L=[]
              custid=int(input("\nenter your ID from the above table display:\t"))
              L.append(custid)
              sql="delete from customer_info where Member_No=%s"
              updation=(L)
              mycursor.execute(sql,updation)
              mydb.commit()
              print("Deletion Done!!".center(140))
              print("="*140)
    else:
        print("Exit is done".center(140))
        
def registernewbook():
    L=[]
    print("="*140)
    print("Registration of new book".center(140))
    name=input("Enter the Name of the book:\t")
    L.append(name)
    bookname=input("Enter Author name:\t")
    L.append(bookname)
    status="Available"
    L.append(status)
    number=int(input("Enter No of books came in:\t"))
    L.append(number)        
    register=(L)
    sql="insert into books(title,author,status,no_of_books)values(%s,%s,%s,%s)"
    mycursor.execute(sql,register)
    mydb.commit()
    print("Registered successfully !!".center(140))
    print("="*140)

def bookview():
    print("="*140)
    print("Book Info".center(140))
    print("\nDo you want to see all available books information?? - press 1")
    print("\nDo you want to see specific books?? - press 2")
    print("\nDo you want to Exit this menu - press 0")
    ch=int(input("\nEnter 1 or 2 or 0:\t"))
    if ch==1:
        sql="select * from books"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        print("="*140)
        print("All Available Books".center(140))
        for x in rows:
            print("Book Id:",x[0])
            print("Book Name:",x[1])
            print("Book Author:",x[2])
            print("No.of Books:",x[4])
            print("\n")
        print("="*140)
    elif ch==2:
        l=[]
        title=input("Enter Bookname to fetch the details about it :\t")
        l.append(title)
        view=(l)
        sql="select * from books where title=%s"
        mycursor.execute(sql,view)
        rows=mycursor.fetchone()
        if(rows==None):
            print("="*140)
            print("No Book found".center(140))
            print("="*140)
        else:
            print("="*140)
            print("Book Id:",rows[0])
            print("Book Name:",rows[1])
            print("Book Author:",rows[2])
            print("No.of Books:",rows[4])
            print("="*140)

    else:
        print("Table viewation was cancelled")
def issuebook():
    l=[]
    print("="*140)
    print("Issuing book".center(140))
    bid=int(input("Enter the Book ID:\t"))
    l.append(bid)
    sql="select title,status,no_of_books from books where bid=%s"
    mycursor.execute(sql,l)
    number=mycursor.fetchone()
    if(number==None):
        print("="*140)
        print("No Book is found".center(140))
        print("="*140)
    else:
        title=str(number[0])
        print("Book title:",title)
        status=str(number[1])
        print("Book Availability:",status)
        number1=int(number[2])
        if(number1>1):
            L=[]
            L.append(bid)
            issue=L
            L1=[]
            L2=[]
            L1.append(bid)
            L1.append(title)
            memid=int(input("Enter member id:\t"))
            L1.append(memid)
            L2.append(memid)
            sql="select Member_no from issued_books where Member_no=%s"
            mycursor.execute(sql,L2)
            rows=mycursor.fetchone()
            if(rows==None):
                sql="Select Member_no from customer_info where Member_no=%s"
                mycursor.execute(sql,L2)
                rows1=mycursor.fetchone()
                if(rows1!=None):
                    issue_date=datetime.date.today()
                    L1.append(issue_date)
                    return_date= issue_date + datetime.timedelta(days=14)
                    L1.append(return_date)
                    issued1=L1
                    sql="insert into issued_books(bid,title,member_no,issue_date,return_date)values(%s,%s,%s,%s,%s)"
                    mycursor.execute(sql,issued1)
                    mydb.commit()
                    sql="update books set no_of_books=no_of_books-1 where bid=%s"
                    mycursor.execute(sql,issue)
                    mydb.commit()
                    print("Issued the book Sucessfully".center(140))
                    print("="*140)
                else:
                    print("="*140)
                    print("No Member is found...So cannot Issue the book")
                    print("="*140)
                
            elif(int(rows[0])!=memid):
                sql="Select Member_no from customer_info where Member_no=%s"
                mycursor.execute(sql,L2)
                rows1=mycursor.fetchone()
                if(rows1!=None):
                    issue_date=datetime.date.today()
                    L1.append(issue_date)
                    return_date= issue_date + datetime.timedelta(days=14)
                    L1.append(return_date)
                    issued1=L1
                    sql="insert into issued_books(bid,title,member_no,issue_date,return_date)values(%s,%s,%s,%s,%s)"
                    mycursor.execute(sql,issued1)
                    mydb.commit()
                    sql="update books set no_of_books=no_of_books-1 where bid=%s"
                    mycursor.execute(sql,issue)
                    mydb.commit()
                    print("Issued the book Sucessfully".center(140))
                    print("="*140)
                else:
                    print("="*140)
                    print("No Member is found...So cannot Issue the book")
                    print("="*140)
            else:
                print("Only One Book is allowed per Member".center(140))
        elif(number1==1):
            L=[]
            status="Empty"
            L.append(status)
            L.append(bid)
            issue=L
            L1=[]
            L2=[]
            L1.append(bid)
            L1.append(title)
            memid=int(input("Enter member id:\t"))
            L1.append(memid)
            L2.append(memid)
            sql="select Member_no from issued_books where Member_no=%s"
            mycursor.execute(sql,L2)
            rows=mycursor.fetchone()
            if(rows==None):
                sql="Select Member_no from customer_info where Member_no=%s"
                mycursor.execute(sql,L2)
                rows1=mycursor.fetchone()
                if(rows1!=None):
                    issue_date=datetime.date.today()
                    L1.append(issue_date)
                    return_date= issue_date + datetime.timedelta(days=14)
                    L1.append(return_date)
                    issued1=L1
                    sql="insert into issued_books(bid,title,member_no,issue_date,return_date)values(%s,%s,%s,%s,%s)"
                    mycursor.execute(sql,issued1)
                    mydb.commit()
                    sql="update books set no_of_books=0,status=%s where bid=%s"
                    mycursor.execute(sql,issue)
                    mydb.commit()
                    print("Issued the book Sucessfully".center(140))
                    print("="*140)
                else:
                    print("="*140)
                    print("No Member is found...So cannot Issue the book")
                    print("="*140)

            elif(int(rows[0])!=memid):
                sql="Select Member_no from customer_info where Member_no=%s"
                mycursor.execute(sql,L2)
                rows1=mycursor.fetchone()
                if(rows1!=None):
                    issue_date=datetime.date.today()
                    L1.append(issue_date)
                    return_date= issue_date + datetime.timedelta(days=14)
                    L1.append(return_date)
                    issued1=L1
                    sql="insert into issued_books(bid,title,member_no,issue_date,return_date)values(%s,%s,%s,%s,%s)"
                    mycursor.execute(sql,issued1)
                    mydb.commit()
                    sql="update books set no_of_books=0,status=%s where bid=%s"
                    mycursor.execute(sql,issue)
                    mydb.commit()
                    print("Issued the book Sucessfully".center(140))
                    print("="*140)
                else:
                    print("="*140)
                    print("No Member is found...So cannot Issue the book")
                    print("="*140)
            else:
                sql="Select Member_no from customer_info where Member_no=%s"
                mycursor.execute(sql,L2)
                rows1=mycursor.fetchone()
                if(rows1!=None):
                    L=[]
                    status="Avialable"
                    L.append(status)
                    L.append(bid)
                    sql="update books set no_of_books=no_of_books+1,status=%s where bid=%s"
                    mycursor.execute(sql,L)
                    mydb.commit()
                    sql="update books set no_of_books=0,status=%s where bid=%s"
                    mycursor.execute(sql,issue)
                    mydb.commit()
                    print("Only One Book is allowed per Member".center(140))
                else:
                    print("No Member is found...So cannot Issue the book")
        else:
            print("No books in hand right now....See later".center(140))


def return_issued():
    print("="*140)
    print("Return of issued Book".center(140))
    l=[]
    mem_id=int(input("Enter Member's No:\t"))
    l.append(mem_id)
    view=(l)
    sql="select * from issued_books where member_no=%s"
    mycursor.execute(sql,view)
    rows=mycursor.fetchone()
    if(rows!=None):
        print("Issued Book Details".center(140))
        print("Book Id:",rows[0])
        print("Book Name:",rows[1])
        print("Member No:",rows[2])
        print("Issued Date:",rows[3])
        print("Return Date:",rows[4])
        print("="*140)
        ch=input("Enter 1 to confrim Return:\t")
        if(ch=='1'):
            return_date=str(rows[4])
            today_date=str(datetime.date.today())
            if(return_date==today_date or return_date>today_date):
                L=[]
                bid=int(rows[0])
                L.append(bid)
                sql="select no_of_books from books where bid=%s"
                mycursor.execute(sql,L)
                number=mycursor.fetchone()
                int_number=int(number[0])
                if(int_number==0):
                    L=[]
                    bid=int(rows[0])
                    status="Available"
                    L.append(status)
                    L.append(bid)
                    sql="update books set no_of_books=1,status=%s where bid=%s"
                    mycursor.execute(sql,L)
                    mydb.commit()
                    l1=[]
                    l1.append(mem_id)
                    l1.append(bid)
                    sql1="delete from issued_books where Member_no=%s and bid=%s"
                    mycursor.execute(sql1,l1)
                    mydb.commit()
                    print("Return within Time No Additional fee".center(140))
                elif(int_number>=1):
                    L=[]
                    bid=int(rows[0])
                    L.append(bid)
                    sql="update books set no_of_books=no_of_books+1 where bid=%s"
                    mycursor.execute(sql,L)
                    mydb.commit()
                    l1=[]
                    l1.append(mem_id)
                    l1.append(bid)
                    sql1="delete from issued_books where Member_no=%s and bid=%s"
                    mycursor.execute(sql1,l1)
                    mydb.commit()
                    print("Return within Time No Additional fee".center(140))
            else:
                L=[]
                bid=int(rows[0])
                L.append(bid)
                sql="select no_of_books from books where bid=%s"
                mycursor.execute(sql,L)
                number=mycursor.fetchone()
                int_number=int(number[0])
                if(int_number==0):
                    L=[]
                    bid=int(rows[0])
                    status="Available"
                    L.append(status)
                    L.append(bid)
                    sql="update books set no_of_books=1,status=%s where bid=%s"
                    mycursor.execute(sql,L)
                    mydb.commit()
                    l1=[]
                    l1.append(mem_id)
                    l1.append(bid)
                    sql1="delete from issued_books where Member_no=%s and bid=%s"
                    mycursor.execute(sql1,l1)
                    mydb.commit()
                    print("Return of the book is late!!".center(140))
                elif(int_number>=1):
                    L=[]
                    bid=int(rows[0])
                    L.append(bid)
                    sql="update books set no_of_books=1 where bid=%s"
                    mycursor.execute(sql,L)
                    mydb.commit()
                    l1=[]
                    l1.append(mem_id)
                    l1.append(bid)
                    sql1="delete from issued_books where Member_no=%s and bid=%s"
                    mycursor.execute(sql1,l1)
                    mydb.commit()
                    print("Return of the book is late!!".center(140))
        else:
            print("Return process is cancelled")
    else:
        print("="*140)
        print("No Return for the given Member No".center(140))
        print("="*140)

def Menuset():
    while True:
        print("*"*140)
        print("Welcome to Library Management!!\n".center(140))
        print("enter 1 : To Register New Members".center(140))
        print("enter 2 : To View Existing Members".center(140))
        print("enter 3 : To Update Members Infomation".center(140))
        print("enter 4 : To Delete Customer's Data".center(140))
        print("enter 5 : To Add New Book Details".center(140))
        print("enter 6 : To View Available Books in The Library".center(140))
        print("enter 7 : Issuing the book ".center(140))
        print("enter 8 : Return of The Issued Book".center(140))
        print("enter 9 : Exit".center(140))
        print("*"*140)
        userinput= input("enter your choice:\t")
        if(userinput=='1'):
            registermem()
        elif(userinput=='2'):
            memview()
        elif(userinput=='3'):
            updatememberinfo()
        elif(userinput=='4'):
            deletememinfo()
        elif(userinput=='5'):
            registernewbook()
        elif(userinput=='6'):
            bookview()
        elif(userinput=='7'):
            issuebook()
        elif(userinput=='8'):
            return_issued()
        elif(userinput=='9'):
            print("="*140)
            print("Session over".center(140))
            print("="*140)
            break
            quit()
        elif(userinput==''):
            print("Left a blank....Enter the correct Choice!! :D")
            Menuset()
        else:
            print("\nLeft a space/Maybe Wrong Option Enter Correct Choice !! :D")
Menuset()
