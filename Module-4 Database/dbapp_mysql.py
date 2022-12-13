import pymysql

try:
    dbcon=pymysql.connect(host='localhost',user='root',password='',database='tpdb')
    print("Database connected!")
except Exception as e:
    print(e)


cur=dbcon.cursor()

# Table Create
tbl_create="create table studinfo(id int primary key,name text,sub text)"

try:
    cur.execute(tbl_create)
    print("Table created!")
except Exception as e:
    print(e)

# Insert Records
insert_data="insert into studinfo values(1,'sanket','python'),(2,'mitesh','java'),(3,'ashok','java'),(4,'paresh','android'),(5,'harsh','ios')"
try:
    cur.execute(insert_data)
    dbcon.commit()
    print("Record inserted!")
except Exception as e:
    print(e)
