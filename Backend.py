import MySQLdb
connection=MySQLdb.connect(host="servername", user="username", passwd="password", db="databasename")
cur=connection.cursor()
cur.execute("create table lfy(name varchar(40), author varchar(40))")
cur.execute("insert into lfy values('Foss Bytes','LFY Team')")
cur.execute("insert into lfy values('Connecting MySql','Ankur Aggarwal')")
cur.execute("select * from lfy")
multiplerow=cur.fetchall()
print  “Displaying All the Rows:  “, multiplerow
print  multiplerow[0]
cur.execute("select * from lfy")
row=cur.fetchone()
print  “Displaying the first row: “, row
print "No of rows: ", cur.rowcount
cur.close()
connection.close()