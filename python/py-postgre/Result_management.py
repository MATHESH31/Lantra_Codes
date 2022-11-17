import psycopg2

IS_DB_CONNECTED = False

try:
    conn = psycopg2.connect(  
        database = "result_management",  
        user = "postgres",  
        password = "123456"  
    ) 
    IS_DB_CONNECTED = True
    print("Database is connected")

except:
    print("Database connection failed!!")

if IS_DB_CONNECTED:
    cursor = conn.cursor()  

    def view_result(): 
        # INPUT
        a = 0 
        final_res = []
        roll = input("Enter the roll number of the student: ").upper()   

        #ROLL_NO ERROR
        cursor.execute("""SELECT roll_no from Results WHERE roll_no = %s;""",(roll,))
        r_err = cursor.fetchall()

        if(len(r_err) == 0):
            print("NO RESULT FOUND FOR THIS ROLL NUMBER")
        else:
            # SEM ERROR 
            sem = int(input("Enter the semester: "))
            print("\n") 
            cursor.execute("""SELECT sem from Results WHERE sem = %s;""",(sem,))
            s_err = cursor.fetchall()

            if(len(s_err) == 0):
                print("THIS SEMESTER IS NOT IN DATABASE!!")
            else:
                # JOINING TABLE AND VIEWING THE STUDENT  
                cursor.execute("""SELECT s_name,dept,c_year,c_sem,sem,subject,marks,grade FROM Results INNER JOIN StudentTable on StudentTable.roll_no = Results.roll_no where StudentTable.roll_no = %s and Results.sem = %s;""",(roll,sem)) 
                res = cursor.fetchall()   

                # CONVERTING TUPLES INTO LIST AND PRINTING
                for i in res:  
                    final_res.append(list(i)) 
                    print("Name: ",i[0])
                    print("Department: ",i[1])  
                    print("Current Year: ",i[2])
                    print("Current Semester: ",i[3])
                    print("Semester Needed: ",i[4])
                    print("Subject: ",i[5])
                    print("Marks: ",i[6])
                    print("Grade: ",i[7])
                    print("\n")

                # OVERALL RESULT  
                for i in final_res: 
                    if(i[7] == "U"): 
                        a +=1 

                if(a >= 1): 
                    print("OVERALL RESULT: FAIL") 
                else: 
                    print("OVERALL RESULT: PASS")     

    # FUNCTION RUNNING 
    while(True): 
        inp = input("SHOW RESULTS (YES/EXIT): ").upper()
        print("\n") 
        if(inp == "YES"): 
            view_result() 
        elif(inp == "EXIT"): 
            break 
        else: 
            print("Enter vaild command!!") 

    # CLOSING  
    cursor.close()  
    conn.close()  