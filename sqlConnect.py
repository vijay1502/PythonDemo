import mysql.connector
cnx = mysql.connector.connect(user='root',password='Ganesh@999',host='localhost',database='stud')
mycursor=cnx.cursor();
# result=mycursor.fetchall();
mycursor.execute("insert into student(rollNo,name) VALUES('235','Krishna')")
mycursor.execute("DELETE FROM student where name='Vijaya'")
mycursor.execute("select * from student")

for i in mycursor:
    print(i)