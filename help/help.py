
import os
import this
import sys
import mysql.connector # mysql数据
import hprose # RPC协议请求
import hashlib # 加密库
import math # 数学库



# with open('./help.md','w',encoding='utf-8') as f: 
# 			f.write(help(mysql.connector))

# help(mysql.connector)
# help(hashlib)	
# print(type(a))
# print(sys.path)
# print(help(hprose))
# PACKAGE CONTENTS
#     client
#     common
#     httpclient
#     httpserver
#     io
#     server
# print(dir(math))



# 查看所有内建函数
# print(dir(__builtins__))
# 查看帮助信息
# print(help(print))

# def abcd():
# 	# pass
# 	print(123)
# print(help(abcd))


# 导入内置math模块
# import math
# content = dir(math)
# print(content)

from sqlalchemy.orm import sessionmaker
# print(dir(sessionmaker))
# print(sessionmaker)
# print(help(sessionmaker().configure()))
import sqlalchemy
# print(sqlalchemy.__version__) #1.3.1
# 打印模块路径方式一
print(sqlalchemy)
# 方式二
print(sqlalchemy.__file__)

