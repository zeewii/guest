#coding=utf-8
#pymysql使用的例子
from pymysql import cursors,connect

conn = connect(host='127.0.0.1',
               user='root',
               password='zeng',
               db='guest',
               charset='utf8mb4',
               cursorclass=cursors.DictCursor)

try:
    with conn.cursor() as cursor:
        sql = 'INSERT INTO sign_guest (realname, phone, email, sign, event_id, create_time) VALUES ("tom", "13000010", "tom@mail.com", 0, 1, NOW());'
        cursor.execute(sql)
    conn.commit()

    with conn.cursor() as cursor:
        sql = "SELECT realname,phone,email,sign FROM sign_guest WHERE phone='13000010';"
        cursor.execute(sql)
        result = cursor.fetchone()
        print result

finally:
    conn.close()