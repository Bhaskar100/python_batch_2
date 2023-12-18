
import mysql.connector

try:
    con = mysql.connector.connect(host='localhost',user='root',password='root',database='my_db')
    print('connection successful')
    cursor = con.cursor()
    cursor.execute("select * from emp100")
    results = cursor.fetchall()
    for row in results:
        eid = row[0]
        ename =row[1]
        esal = row[2]
        print("eid = %d,ename=%s,esal=%g"%(eid,ename,esal))
    cursor.close()
    con.close()

except Exception as e:
    print(e)
