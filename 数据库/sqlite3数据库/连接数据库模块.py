import os 
import sqlite3
from sqlite3 import connect

class MySqliteDB(object):
	""" 访问数据库的类 """
	def __init__(self, dbname='address.db'):
		# 构造方法
		super(MySqliteDB, self).__init__()
		self.dbname = dbname
		self.con = None
		self.curs = None

	def getCursor(self):
		# 建立连接
		self.con = sqlite3.connect(self.dbname)
		if self.con:
			self.curs = self.con.cursor() # 返回游标
	
	def closeDB(self):
		if self.curs:
			self.curs.close() # 关闭游标
		if self.con:
			self.con.commit() # 提交事务
			self.con.close()
	
	def __enter__(self):
		# 协议方法，上下文管理器，方便建立连接，释放数据库连接
		self.getCursor()
		return self.curs
	
	def __exit__(self,exc_type,exc_val,exc_tb):
		# 协议方法，上下文管理器，方便建立连接，释放数据库连接
		if exc_val:
			print('Exception has generate:',exc_val)
			print('sqlite3 execute error!')
		self.closeDB()




		