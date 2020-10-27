<<<<<<< HEAD
# 打印某字符串的所有子序列
# str = 'ABCD'
# i = 0
# def printAll(str, i, res):
#     if i == len(str) - 1:
#         print(res)
#         return
#     printAll(str, i + 1, res + str[i])
#     printAll(str, i + 1, res)

# printAll(str, 0, "")

# def printAllstr(str):
#     for i in range(len(str)):
#         j = i + 1
#         while j < len(str):
#             print(str[i:j])
#             j += 1
# printAllstr(str)

# list = []
# list.append(1)
# list.append(2)
# list.append(3)
# print(list)
# list.pop()
# list.append(4)
# list.pop()
# print(list)

# def stackTurnElement(list):
#     result = list.pop()
#     if list == nu 

import MySQLdb
import pprint

connect = MySQLdb.connect(
    host = 'localhost',
    user = 'root',
    passwd = '282010',
    db = 'demo01',
    charset = 'utf8'
)

cursor = connect.cursor()
cursor.execute('select * from titles;')
row = cursor.fetchall()
print(row)
cursor.close()
connect.commit()
connect.close()
=======
a = [None]*(n+1)
a[0] = 1
>>>>>>> 5838183a8d5be6bd66052a91d4c6dc6c558b02a9
