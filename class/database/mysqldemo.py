import mysql.connector as sql

con = sql.connect(
    host='127.0.0.1',
    user='root',
    password='root',
    port=3306,
    database = 'pythonsql'
)
cursour = con.cursor()
# cursour.execute("create database pythonsql")
# cursour.execute("create table emp(id int primary key , name varchar(50),email varchar(50))")
# cursour.execute("insert into emp values(3,'zeel','ze@gmail.com')")
# cursour.execute("update emp set email='abc@gmail.com' where id = 3")
# cursour.execute("delete from emp where id=3")
# con.commit()

# cursour.execute("select * from emp")

# data = cursour.fetchall()  

# print(data)