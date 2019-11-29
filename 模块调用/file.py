# 该文件演示的是如何解决模块跨目录调用问题
"""
在dir1目录下存在a，b两个模块，包含__init__文件的文件夹就叫python package
分别演示
file.py调用file_a.py,file_b.py
file_a.py，file_b.py调用file.py
file_a.py，file_b.py相互调用

"""

"""
模块地址导入sys.path的两种办法
1、临时添加
import sys, os
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir,os.pardir))
sys.path.append(parent_dir)

import sys
import os
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir,os.pardir))
sys.path.append(parent_dir)


2、永久添加
在MacOS上进行
1. 先查看执行模块的路径sys.path
>import sys,os
>print(sys.path)

2. 在python安装路径'/usr/local/lib/python3.6/site-packages'文件夹下，新建mytest.pth文件

3. 在mytest.pth中写入项目目录绝对地址'/Volumes/B/MyWorkspace/superManPro/test_bestpay/bestPay'

注意:路径中如果有中文则报ascii码错误
pythonPATH路径
'/Users/henry/Library/Python/3.6/lib/python/site-packages', 
python安装路径
'/usr/local/lib/python3.6/site-packages'

"""
# 可直接调用

# from a import file_a
# from b import file_b

# from a.a1 import file_a1

# import sys,os
# print(sys.path)


# sys.path 变量是一个字符串列表，用于确定解释器的模块搜索路径。该变量被初始化为从环境变量 PYTHONPATH 获取的默认路径，或者如果 PYTHONPATH 未设置，则从内置默认路径初始化。你可以使用标准列表操作对其进行修改:
# import sys
# sys.path.append('/ufs/guido/lib/python')
# print(sys.path)

# 获取当前文件父目录地址
# import sys, os
# BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)







