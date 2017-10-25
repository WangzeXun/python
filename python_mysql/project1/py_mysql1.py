import pymysql

conn=pymysql.connect(
    host='127.0.0.1',port=3306,user='root',passwd='940211',
    db='python_mysql',charset='utf8'
    )
curs=conn.cursor()
#print(conn)
#print(curs)

sql = 'select * from user'
curs.execute(sql)

print(curs.rowcount)

r1=curs.fetchone()
print(r1)
r2=curs.fetchmany(3)
print(r2)
r3=curs.fetchall()
print(r3)



curs.close()
conn.close()