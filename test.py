 # -*- coding: utf-8 -*-
 
#*******字符串排序及统计**************#
# world=input()
# list1 = list(world)
# while '\n' in list1:
	# list1.remove('\n')
# list2=sorted(list1)
# print(list2)
# print('\n')
# list3=list(set(list2))
# print(list3) 
# list4=[]
# list5=[]

# for i in list3:
	# j=list2.count(i)
	# list4.append((i,j))

# def recmp(x,y):
	# if x<y:
		# return 1
	# if x==y:
		# return 0
	# if x>y:
		# return -1

# list4.sort(lambda x,y:recmp(x[1],y[1]))
# list5=list4[:3]
# print(list5)

#***************   test   *********************#
# def dic(name,age,*d,city,**job):
	# print(name,age,*d,city,*job)
# dic('qs',23,city='cq')

# print('\n')


# def not_empty(s):
    # return s.strip('v')
# l=['vjkv','tvkj','tvkv']
# t=list(filter(not_empty,l))
# print(t)

# l=['vjkv','tvkj','tvkv']
# def hh(l):
	# listt=[]
	# for i in l:
		# listt.append(i.strip('v'))
	# return listt
# print(hh(l))
#***************求素数****************#
# num=[]
# i=2
# for i in range(2,10):
   # j=2
   # for j in range(2,i):
   
      # if(i%j==0):
         # break
   # else:
      # num.append(i)
# print(num)
#*************************************#		

#***************返回函数*****************#	

# def top1(args):
	# i=1
	# l=[]
	# def top2():
		# for j in args:
			
			# l.append(i+j)
		# return l
	# return top2
# li=[1,2,3,5,6,2,3]
# r=top1(li)
# print(r())
	
# def count():
	# def f(j):
		# def num():
			# return j*j
		# return num
	# fs=[]
	# for i in range(1,4):
		# fs.append(f(i))
	# return fs
# f1,f2,f3=count()#返回多少个地址就需要多少个变量去接受
# print(f1(),f2(),f3())
# T=[]
# T=count()#用列表去接收
# for i in range(len(T)):
	# print(T[i]())
	
	
#***************装饰器*****************#		
# def now():
	# print('2015-3-25')
# f=now
# print(f.__name__)#两个下划线

	
#***************偏函数*****************#	
# import functools
# int2=functools.partial(int,base=2)	
# num=int2('1010',base=10)
# num1=int('25',8)
# print (num1)

#***************模块导入*****************#
# 'a test model'
# __author__='Mr.qin'
# import sys
# def test11():
	# args=sys.argv
	# if len(args)==1:
		# print('hello world,%s'%args[0])
		
	# elif len(args)==2:
		# print('hello,%s!'%args[1])
	# else:
		# print('hh')
# def test1():
	# print('自动运行')

# test1()
# #其他.py文件调用下面的函数，需要指明调用才行。
# #eg:test.test()11.而test()1,当导入时就直接被调用
# if __name__=='__main__':
	# test11()

def __print_1(name1):
	print('hello %s'%name1)
def __print_2(name1):
	print('Hi, %s'%name1)

def write1():
	name=input('plesae input your name:')
	if len(name)>3:
		__print_2(name)
	else:
		__print_1(name)

if __name__=='__main__':
	 write1()









	