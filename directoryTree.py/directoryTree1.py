from pathlib import Path
import sys
import os
"""python生成文件目录树：方法一使用pathlib库
原地址：https://blog.csdn.net/yaoyefengchen/article/details/80195231
Python有一个标准文件路径处理库 os.path ，从 Python3.4 开始，Python 又加入了一个标准库 pathlib ，该库是跨平台的、面向对象的路径操作库。 

"""
# 第一步：查看基本操作
# p = Path('/Volumes/B/8手机壁纸') #创建路径对象
# print(p.name) # 获取路径地址中的文件名
# print(p.is_file()) # 判断是否是文件
# print(p.is_dir()) # 判断是否是文件夹
# print(p.iterdir()) # 返回一个迭代器，包含p下所有文件夹和文件
# print(Path.cwd()) # 打印当前python运行文件的目录地址

# # 第二步：实现代码逻辑
# tree_str = ''
# def generate_tree(pathname,n=0):
# 	global tree_str
# 	if pathname.is_file():
# 		if pathname.name[0] == '.': # 去掉隐藏文件
# 			pass
# 		else:
# 			# 打印出文件信息
# 			tree_str += '    |' * n + '-' * 4 + pathname.name + '\n'	
# 	elif pathname.is_dir():
# 		# print(pathname.parent) # 获取父路径
# 		# print(pathname.relative_to(pathname.parent)) # 获取相对路径，根据父目录获取当前目录名，没必要这样做，直接用pathname.name便好
# 		# print(type(pathname.relative_to(pathname.parent)))
# 		# print(str(pathname.relative_to(pathname.parent))) # 转换为字符串格式
# 		# 打印出文件夹信息
# 		tree_str += '    |' * n + '-' * 4 + pathname.name + '\\' + '\n'
# 		for cp in pathname.iterdir(): # 递归访问子目录下的所有文件
# 			# print(cp)
# 			generate_tree(cp,n+1) # 递归就是方法自身再次调用该方法

# # 第三步：将打印的数据保存成文件
# def save_file(data,filename='tree.txt'):
# 	with open(filename,'w',encoding='utf-8') as f:
# 		f.write(data)
# if __name__ == '__main__':
# 	#生成指定地址的目录树,将字符串转换为pathlib对象
# 	url = '/Volumes/B/8手机壁纸'
# 	dire = './diretree.txt'
# 	generate_tree(Path(url)) 
# 	print(tree_str)
# 	save_file(tree_str,dire)


# 第四步：封装打包
class DiretoryTree(object):
	"""    
	@ pathname: 目标目录
    @ filename: 要保存成文件的名称
    @ data: 要写入的目录结构
    """
	def __init__(self, pathname='.',filename='tempDire.txt'):
		super(DiretoryTree, self).__init__()
		self.data = ''  # 类中全局变量
		# 如果不自定义路径和文件名则用初始化的值，pathname='.'表示当前路径，filename='tempDire.txt')表示保存到tempDire.txt文件中
		self.pathname = Path(pathname)
		self.filename = filename

	def set_path(self,pathname):
		self.pathname = Path(pathname) # 封装一个方法来自定义设置路径

	def set_filename(self,filename):
		self.filename = filename # 封装一个方法来自定义要保存的文件信息


	def diretree(self,n=0,i=0): # n表示层级，i表示显示到哪一层级
		if self.pathname.name[0] == '.' or self.pathname.name[0] == '_': # 过滤掉隐藏文件
			pass
		else:
			if self.pathname.is_file(): # 判断该文件信息是否是文件
				# 以该格式打印出文件名
				# print('    |'*n + '-'*4 + self.pathname.name)
				self.data += '    |'*n + '-'*4 + self.pathname.name + '\n' 
			elif self.pathname.is_dir(): # 判断文件信息是否是文件夹

				#以该格式打印出文件夹名
				self.data += '    |'*n + '-'*4 + self.pathname.name + '\\------------文件夹---------------\\' +'\n'
				if n<i:		# 判断递归到哪一层		
					for pa in self.pathname.iterdir(): # 获取文件夹下的所有文件信息
						# 调试，查看递归循环逻辑
						# print('dir-')
						# print(self.pathname.name)
						# print(self.count)
						# print(n)
						# print(i)
						# print('----')
						# 将新的文件信息存放到pathname中保存，方便递归时调用判断
						self.pathname = Path(pa) 
						# 对当前文件夹进行递归，就像大盒子里装小盒子，小盒子里再装小盒子
						self.diretree(n+1,i)
		return(self.data)

	def save_file(self):
		# 文件IO的特殊语法，将拼接好的内容写入到指定的文件中
		# 在macOS中python3必须以encoding='utf-8'打开文件再读写
		with open(self.filename,'w',encoding='utf-8') as f: 
			f.write(self.data)


if __name__ == '__main__':
	#生成指定地址的目录树,将字符串转换为pathlib对象
	# url = '/Volumes/B/我的工作文档/superManPro'
	# url = '/Volumes/B/我的工作文档/superManPro/test_wap/wap_entry'
	url = '/Volumes/B/MyWorkspace/superManPro/test_hebaopay/aliyun_hebaopay'
	# dire = './diretree.txt'
	dire = '/Users/henry/Desktop/文档目录结构.md'

	MyTree = DiretoryTree()
	# 注意按照顺序执行方法，因为初始化时设有默认值
	MyTree.set_path(url)
	MyTree.set_filename(dire)
	print(MyTree.diretree(i=2))
	MyTree.save_file()
