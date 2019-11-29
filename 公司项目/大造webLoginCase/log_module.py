# coding=utf-8
import time
import json
import xlsxwriter
# 日志接口，将日志信息保存到txt文档中
class Loginfo(object):

	def __init__(self,path = ''):
		# path调用者可以传一个路径，默认为当前路径
		# 将日志文件以年月日的方式命名
		# mode代表通过直写的方式打开文件，会覆盖重名文件
		fname = path + time.strftime('%Y-%m-%d',time.gmtime())
		self.log = open(path + fname + '.txt',"w")
	def log_init(self,sheetname,*title): 
		pass # 占位方法
	def log_write(self,msg):
		self.log.write(msg)
	def log_close(self):
		self.log.close()
 
class XLLoginfo(object):
	"""docstring for XLLoginfo"""
	def __init__(self, path='',mode=''):
		fname = path + time.strftime('%Y-%m-%d',time.gmtime()) # 以当前日期命名
		self.row = 0  #行数
		self.xl = xlsxwriter.Workbook(path+fname+'.xls') # 创建一个xls文档
		self.style = self.xl.add_format({'bg_color':'red'}) # 设置背景色为红色
	def xl_write(self,*args): # 将数据按行写入表中，向后写入。内置方法，外面不调用
		col = 0  # 列数
		style = ''
		if 'error' in args: # 在检查到Error字符的时候设置
			style = self.style
		for val in args: 
			self.sheet.write_string(self.row,col,val,style)
			col +=1 # 把每行的所有列都写完
		self.row+=1 # 再换行写

		# 给用户使用的方法,暴露在外面的方法,与Loginfo的方法名一致方便调用
	def log_init(self,sheetname,*title): # 创建一个表，并设置表名和第一行属性内容
		self.sheet = self.xl.add_worksheet(sheetname)
		self.sheet.set_column('A:E',30)
		self.xl_write(*title) # 调用写方法
	def log_write(self,*args):
		self.xl_write(*args) # 调用写方法
	def log_close(self):
		self.xl.close()

if __name__ == '__main__':
	# log = Loginfo()
	# log.log_write("123")
	# msg = json.dumps('世界')
	# log.log_write(msg)
	# log.log_close()
	xinfo = XLLoginfo()
	xinfo.log_init('msg','uname','pwd','result','info')
	xinfo.log_write('123','123','error','错误')
	xinfo.log_close()
	# pass



