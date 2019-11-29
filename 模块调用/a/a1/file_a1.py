# 该文件演示的是如何解决模块跨目录调用问题
"""
在dir1目录下存在a，b两个模块，包含__init__文件的文件夹就叫python package
分别演示
file.py调用file_a.py,file_b.py
file_a.py，file_b.py调用file.py
file_a.py，file_b.py相互调用

"""
		
import sys
import os
current_dir = os.path.dirname(__file__) # 获取当前文件路径
print(current_dir)
print(os.pardir) # 相当于'..'
print(os.path.join(current_dir,'../..')) # 上上级目录名,即上级目录的上级目录
parent_dir = os.path.abspath(os.path.join(current_dir,'../..')) # 获取上上级目录路径
print(parent_dir)
sys.path.append(parent_dir) # 将路径添加到pythonPATH中
print(sys.path)

import file
from b import file_b
