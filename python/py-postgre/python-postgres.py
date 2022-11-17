import psycopg2

flag = False

try:
    conn = psycopg2.connect(
        database = "py_pg",
        user = "postgres",
        password = "123456"
    )
    flag = True
    print("Database is connected")
except:
    print("Database is not connected")

if(flag == False):
    pass
else:
    cursor = conn.cursor()

    #FUNCTION SELECTION
    while(True):
        func = input("Enter the function to perform (CREATE/INSERT/UPDATE/DELETE/SELECT/EXIT): ").upper()

        if(func == "CREATE"):

            #IF ALREADY EXIST
            cursor.execute("""DROP TABLE employees;""")

            #CREATE TABLE
            create = """CREATE TABLE employees(employeeNumber SERIAL PRIMARY KEY,firstname VARCHAR(15),lastname VARCHAR(15),email VARCHAR(255),pincode INT,officeCode INT,reportsTo VARCHAR(20),jobTitle VARCHAR(15));"""
            cursor.execute(create)
            conn.commit()
            print("Table employees created")

        elif(func == "INSERT"):

            #INSERT DATA
            n = int(input("Enter number of Employees to input: "))
            for i in range(n):
                firstname = input("Enter your firstname: ")
                lastname = input("Enter your lastname: ")
                email = input("Enter your email: ")
                pincode = int(input("Enter your pincode: "))
                officeCode = int(input("Enter your Office Code: "))
                reportsTo = input("Enter whom are you reporting to: ")
                jobTitle = input("Enter your Job Title: ")
                cursor.execute("""INSERT INTO employees(firstname,lastname,email,pincode,officeCode,reportsTo,jobTitle) VALUES (%s,%s,%s,%s,%s,%s,%s)""",[firstname,lastname,email,pincode,officeCode,reportsTo,jobTitle])
            print("Values inserted")
            conn.commit()
            cursor.execute("""SELECT * FROM employees""")
            print(cursor.fetchall())

        elif(func == "UPDATE"):

            #UPDATE DATA
            print("[1]-SET FIELD(NUMERAL) & WHERE COND(NUMERAL)")
            print("[2]-SET FIELD(STRING) & WHERE COND(STRING)")
            print("[3]-SET FIELD(STRING) & WHERE COND(NUMERAL)")
            print("[4]-SET FIELD(NUMERAL) & WHERE COND(STRING)")
            n_s = int(input("(1/2/3/4): "))
            u_field = input("Enter field to update: ")
            uv_field = input("Enter field value to update: ")
            k_field = input("Enter key field to update: ")
            oper = input("Enter operator to perform (EQUAL/GREATERTHAN/LESSERTHAN/GREATERTHANEQUAL/LESSERTHANEQUAL/NOTEQUAL)").upper()
            val = input("Enter value for key to update: ")

            if(n_s == 1):
                if(oper == "EQUAL"):
                    cursor.execute("UPDATE employees SET " + u_field + " = %s where " + k_field + " = %s ;",[int(uv_field),int(val)])

                elif(oper == "GREATERTHAN"):
                    cursor.execute("UPDATE employees SET " + u_field + " = %s where " + k_field + " > %s ;",[int(uv_field),int(val)])

                elif(oper == "LESSERTHAN"):
                    cursor.execute("UPDATE employees SET " + u_field + " = %s where " + k_field + " < %s ;",[int(uv_field),int(val)])

                elif(oper == "GREATERTHANEQUAL"):
                    cursor.execute("UPDATE employees SET " + u_field + " = %s where " + k_field + " >= %s ;",[int(uv_field),int(val)])

                elif(oper == "LESSERTHANEQUAL"):
                    cursor.execute("UPDATE employees SET " + u_field + " = %s where " + k_field + " <= %s ;",[int(uv_field),int(val)])

                elif(oper == "NOTEQUAL"):
                    cursor.execute("UPDATE employees SET " + u_field + " = %s where " + k_field + " != %s ;",[int(uv_field),int(val)])

            elif(n_s == 2):
                if(oper == "EQUAL"):
                    cursor.execute("UPDATE employees SET " + u_field + "= %s where " + k_field + " = %s ;",[uv_field,val])

                elif(oper == "NOTEQUAL"):
                    cursor.execute("UPDATE employees SET " + u_field + "= %s where " + k_field + " != %s ;",[uv_field,val])

            elif(n_s == 3):
                if(oper == "EQUAL"):
                    cursor.execute("UPDATE employees SET" + u_field + " = %s where " + k_field + " = %s ;",[uv_field,int(val)])

                elif(oper == "GREATERTHAN"):
                    cursor.execute("UPDATE employees SET" + u_field + " = %s where " + k_field + " > %s ;",[uv_field,int(val)])

                elif(oper == "LESSERTHAN"):
                    cursor.execute("UPDATE employees SET" + u_field + " = %s where " + k_field + " < %s ;",[uv_field,int(val)])

                elif(oper == "GREATERTHANEQUAL"):
                    cursor.execute("UPDATE employees SET" + u_field + " = %s where " + k_field + " >= %s ;",[uv_field,int(val)])

                elif(oper == "LESSERTHANEQUAL"):
                    cursor.execute("UPDATE employees SET" + u_field + " = %s where " + k_field + " <= %s ;",[uv_field,int(val)])

                elif(oper == "NOTEQUAL"):
                    cursor.execute("UPDATE employees SET" + u_field + " = %s where " + k_field + " != %s ;",[uv_field,int(val)])

            elif(n_s == 4):
                if(oper == "EQUAL"):
                    cursor.execute("UPDATE employees SET " + u_field + " = %s where " + k_field + " = %s ;",[int(uv_field),val])

                elif(oper == "NOTEQUAL"):
                    cursor.execute("UPDATE employees SET " + u_field + " = %s where " + k_field + " != %s ;",[int(uv_field),val])
            
            conn.commit()
            print("Value Updated")
            cursor.execute("""SELECT * FROM employees""")
            print(cursor.fetchall())


        elif( func == "DELETE"):

            #DELETE DATA
            del_field = input("Enter key field to delete: ")
            oper = input("Enter operator to perform (EQUAL/GREATERTHAN/LESSERTHAN/GREATERTHANEQUAL/LESSERTHANEQUAL/NOTEQUAL): ").upper()
            n_s = input("Is the value for key NUMERAL or STRING: ").upper()
            val = input("Enter value for key to delete: ")

            if(n_s == "NUMERAL"):
                if(oper == "EQUAL"):
                    cursor.execute("DELETE FROM employees where " + del_field + " = %s;",[int(val),])

                elif(oper == "GREATERTHAN"):
                    cursor.execute("DELETE FROM employees where " + del_field + " > %s;",[int(val),])

                elif(oper == "LESSERTHAN"):
                    cursor.execute("DELETE FROM employees where " + del_field + " < %s;",[int(val),])

                elif(oper == "GREATERTHANEQUAL"):
                    cursor.execute("DELETE FROM employees where " + del_field + " >= %s;",[int(val),])

                elif(oper == "LESSERTHANEQUAL"):
                    cursor.execute("DELETE FROM employees where " + del_field + " <= %s;",[int(val),])

                elif(oper == "NOTEQUAL"):
                    cursor.execute("DELETE FROM employees where " + del_field + " != %s;",[int(val),])
            
            elif(n_s == "STRING"):
                if(oper == "EQUAL"):
                    cursor.execute("DELETE FROM employees where " + del_field + " = %s;",[val,])

                elif(oper == "NOTEQUAL"):
                    cursor.execute("DELETE FROM employees where " + del_field + " != %s;",[val,])

            conn.commit()
            print("Value deleted")
            cursor.execute("""SELECT * FROM employees""")
            print(cursor.fetchall())

        elif(func == "SELECT"):
            cursor.execute("""SELECT (%s,%s,%s,%s,%s,%s,%s,%s) FROM employees""",["employeeNumber","firstname","lastname","email","pincode","officeCode","reportsTo","jobTitle"])
            print(cursor.fetchall())
            
        elif(func == "EXIT"):
            break

        else:
            print("Enter valid command!!")

    cursor.close()
    conn.close()