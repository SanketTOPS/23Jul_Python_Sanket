import sqlite3

try:
    dbcon=sqlite3.connect('mydb.db')
    print("Database connected!")
except Exception as e:
    print(e)

 # Table Create

tbl_create="create table studinfo(id int primary key,name text,sub text)"
try:
    dbcon.execute(tbl_create)
    print("Table created!")
except Exception as e:
    print(e)

# Insert Records
"""insert_data="insert into studinfo values(1,'sanket','python'),(2,'mitesh','java'),(3,'ashok','java'),(4,'paresh','android'),(5,'harsh','ios')"
try:
    dbcon.execute(insert_data)
    dbcon.commit()
    print("Record inserted!")
except Exception as e:
    print(e)"""

# Update Record
"""update_data="update studinfo set sub='php' where id=3"
try:
    dbcon.execute(update_data)
    dbcon.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""

# Delete Record
"""delete_data="delete from studinfo where name='sanket'"
try:
    dbcon.execute(delete_data)
    dbcon.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""

cur=dbcon.cursor()

# Select Records
select_data="select * from studinfo"
try:
    cur.execute(select_data)
    data=cur.fetchall()
    #data=cur.fetchmany(2)
    #data=cur.fetchone()
    #print(data)

    for i in data:
        print(i[2])
except Exception as e:
    print(e)