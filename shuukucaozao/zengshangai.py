# -*- coding: UTF-8 -*-
#数据库查询操作
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
    sql="INSERT INTO `test`.`student` (`id`, `name`, `subject`, `score`) VALUES ('218', '测试', 'B', '89');"
    # sql="UPDATE `test`.`student` SET `name`='dd';"
    # 当对数据进行增删改时执行完语句后需要commit

    #执行sql语句
    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        conn.rollback()#回滚sql
    # cursor.execute(sql1)
    finally:
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()


    #获取查询的结果
    # result=cursor.fetchall()
    # for row in result:
    #     print(row)

    #print(result)
