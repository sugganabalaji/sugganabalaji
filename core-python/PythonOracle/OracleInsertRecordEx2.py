#Program for Reading the values from KBD and Insert then as Record in Employee table
# OracleInsertRecordEx2.py
import oracledb as orc # step 1

def recordInsert():
    try:
        connobj = orc.connect("c##scott/tiger@localhost/orcl")
        curobj = connobj.cursor()
        # Read emp values from KBD
        print("--------------------------------------------")
        eno=int(input("Enter Employee Number:"))
        ename = input("Enter Employee Name:")
        empsal = float(input("Enter Employee Salary:"))
        compname = input("Enter Company name:")
        print("--------------------------------------------")

        iq = "insert into employee values (%d,'%s',%f,'%s')" %(eno,ename,empsal,compname)
        # 200 Dennis 3.4 Bell Labs
        # 400 sandeep 2.3 TCS
        #
        curobj.execute("insert into employee values (%d,'%s',%f,'%s')" %(eno,ename,empsal,compname))
        connobj.commit()

        print("{} Record inserted in Table--verify".format(curobj.rowcount))
    except orc.DatabaseError as db:
        print("Problem on Oracle Databse: ", db)

#Main program
recordInsert()