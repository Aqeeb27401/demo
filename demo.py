import mysql.connector as c
con=c.connect(host="localhost",user="root",passwd="",database="aqeeb")
Cursor=con.cursor()
while True:
   name=input("Enter name:")
   design=input("Enter designation:")
   salary=int(input("Enter salary:"))
   Cursor.execute("INSERT INTO `emp` (`code`, `name`, `design`, `salary`) VALUES (NULL, '{}', '{}', {});".format(name,design,salary))
   con.commit()
   print("Successfully Entered")
   x=int(input("1-->Continuoue and 2-->Exit")
   if x==2:
        break
