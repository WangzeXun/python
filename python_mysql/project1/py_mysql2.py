import pymysql

conn=pymysql.connect(
    host='127.0.0.1',port=3306,user='root',passwd='940211',
    db='python_mysql',charset='utf8'
    )
curs=conn.cursor()
#print(conn)
#print(curs)

sql_insert = 'insert user (user_id,username) values(10,"name10")'
sql_update = 'update user set username="name91" where user_id=9'
sql_delete = 'delete from user where user_id<3'

try:
    curs.execute(sql_insert)
    print(curs.rowcount)
    curs.execute(sql_update)
    print(curs.rowcount)
    curs.execute(sql_delete)
    print(curs.rowcount)
    
    conn.commit()
except Exception as e:
    print(e)
    conn.rollback()

curs.close()
conn.close()