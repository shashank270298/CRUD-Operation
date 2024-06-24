import sqlite3
import traceback

t = int()
conn = None
try:
    conn = sqlite3.connect("F:/PythonPrjct/Databases/Students.db")
    print("Database connected successfully......")
    cur = conn.cursor()
    
    def create():
        cur.execute("Create table t1(Roll_no int, Name text, Surname text, Class int, City text)")
        print("Table created Successfully......")
    
    def insert(n):
        for i in range(n):
            rollN = int(input(f'Enter Roll-Number: '))
            name = input(f'Enter Name: ')
            surname = input(f'Enter Surname: ')
            clas = int(input(f'Enter Class: '))
            cty = input(f'Enter City: ')
            cur.execute("Insert into t1  values(:1, :2, :3, :4, :5)",(rollN, name, surname, clas, cty))
            conn.commit()
            n = cur.rowcount
            print(f'{n} row inserted')
                    
    def read():
        cur.execute("Select * from t1")
        rslt = cur.fetchall()
        for i in rslt:
            Roll_no, Name, Surname, Class, City = i
            print(Roll_no, Name, Surname, Class, City, sep = " ")
        
    def update():
        id = int(input("Enter roll_no to update information: "))
        col = input(f'Enter column to update(N for name, S for surname, C for class, Ct for city): ')
        if col == "N":
            newN = input("Enter new name: ") 
            updt = cur.execute("Update t1 set Name = :1 where Roll_no = :2",(newN, id))
            conn.commit()
            n = cur.rowcount
            print(n," Row updated!!!!!!")
        elif col=="S":
            newS = input("Enter new surname: ")
            updt = cur.execute("Update t1 set Surname= :1 where Roll_no=:2",(newS, id))
            conn.commit()
            n = cur.rowcount
            print(n, "Row updated!!!!!!")
        elif col=="C":
            newC= int(input("Enter new Class: "))
            updt = cur.execute("Update t1 set Class = :1 where Roll_no = :2",(newC, id))
            conn.commit()
            n = cur.rowcount
            print(n, "Row updated!!!!!!")
        elif col=="Ct":
            newCt = input("Enter new City: ")
            updt = cur.execute("Update t1 set City = :1 where Roll_no = :2",(newCt, id))
            conn.commit()
            n = cur.rowcount
            print(n, "Row updated!!!!!!")      
    
    def delete():
        a = input("W for deleting whole table, R for deleting row: ")
        if a == "W":
            cur.execute("Drop table t1")
            conn.commit()
            print("Table deleted successfully!!!!!!")
        elif a == "R":
            n = int(input("Enter Roll_no to delete row: "))
            cur.execute("Delete from t1 where Roll_no = :1",(n,))
            cnt = cur.rowcount
            conn.commit()
            print(f'{cnt} Row deleted!!!!!!')
            
    

    print("This is a CRUD operation program.", "1 for Create table", "2 for Inserting data in table","3 for Reading table data", "4 for Updating table data", "5 for Deleting table data", sep = "\n")
    opt = int(input("Enter: "))

    if   opt == 1:
        print("You opt for creating table......")
        create()
    elif opt == 2:
        print("You opt for inserting record into table......")
        row = int(input("Enter number of rows to be inserted: "))
        insert(row)
    elif opt == 3:
        print("You opt for reading table......")
        read()
    elif opt == 4:
        print("You opt for updating table......")
        update()
    elif opt == 5:
        print("You opt for deleting table......")
        delete()
    
    
except(sqlite3.DatabaseError) as ex:
    print("Error in connection......")
    print("Cause: ", traceback.format_exc())
finally:
    if conn is not None:
        conn.close()
        print("Database disconnected sucessfully......")