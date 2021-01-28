# -*- coding: UTF-8 -*-
#导入包
import pymysql
if __name__ == '__main__':

    #创建连接对象
    conn=pymysql.connect(host="127.0.0.1",
                         port=3306,
                         user="root",
                         password="",
                         database="test",
                         charset="utf8")
    #获取游标，目的时执行sql语句
    cursor=conn.cursor()
    #准备sql
    sql="SELECT * from student;"
    #执行sql语句
    cursor.execute(sql)
    #获取查询的结果
    result=cursor.fetchall()
    print(result)
    #关闭游标
    cursor.close()
    #关闭连接
    conn.close()