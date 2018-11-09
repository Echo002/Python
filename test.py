import pymysql
import codecs
import csv

def red_mysql_to_csv(filename):
    with codecs.open(filename = filename, mode = 'a+',encoding = 'utf-8')as f:
        write = csv.writer(f,dialect = 'excel')
        db = pymysql.connect("localhost", "root", "root", "zhanghao")
        sql = r"select * from gps1 where  事件 = 4 and 时间<20121101001700 and 状态 > 0 and 速度 =0  and 方位=290  ;"

        cursor = db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        for res in results:
            print(res)
            write.writerow(res)
red_mysql_to_csv('result.csv')
