import os
import sys

""" 获取当前文件夹地址 文件名"""


print(__file__)
print(sys.argv[0])
print(os.path.dirname(__file__))
# print(os.path.split(__file__))
print(os.path.split(__file__)[-1])
print(os.path.split(__file__)[-1].split(".")[0])
print(os.getcwd())

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.abspath(__file__))