import pymysql
conn=None
try :
    conn = pymysql.connect(host='127.0.0.1',user='root',password='123456',database='equipment_mg',port=3306)
except pymysql.err.OperationalError as op_err:
    print(op_err)
else:
    print(conn.ping(False))
finally:
    if conn:
        conn.close()