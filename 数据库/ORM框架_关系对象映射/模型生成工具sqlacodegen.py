# 生成新的对象对应关系.py

"""
相关文档
https://blog.csdn.net/fungleo/article/details/78865921
https://blog.csdn.net/guoqianqian5812/article/details/78861820

sqlacodegen 这个工具主要将数据库中的表生成sqlalchemy模型
创建命令例子：
sqlacodegen mysql+mysqlconnector://sp_man:Spman@123#admin.com@119.23.145.20/sp_grant --tables credits --outfile ./credits.py
mysql+mysqlconnector://，需要链接的数据库类型
sp_man:Spman@123#admin.com@119.23.145.20，sqlalchemy连接数据库的方式，用户名+密码+端口号
sp_grant数据库名
--tables指定数据表名称，我们给fund基金数据表生成。
--outfile指定输出文件名称。

示例：
sqlacodegen mysql+pymysql://sp_man:Spman@123#admin.com@119.23.145.20:3306/fqcr --tables afterloan_order --outfile AfterloanOrder.py
sqlacodegen mysql+pymysql://sp_man:Spman@123#admin.com@119.23.145.20:3306/fqcr --tables user_extend_yi --outfile ./model/user_extend_yi.py
sqlacodegen sqlite://sp_man:Spman@123#admin.com@119.23.145.20/sp_grant > sp_grant_credits.py
---
执行：
sqlacodegen mysql+mysqlconnector://sp_man:Spman@123#admin.com@119.23.145.20/fqcr --tables user_extend_yi --outfile ./fqcr_user_extend_yi.py
sqlacodegen mysql+mysqlconnector://sp_man:Spman@123#admin.com@119.23.145.20/fqcr --tables order_extend_yi --outfile ./fqcr_order_extend_yi.py


"""
		





