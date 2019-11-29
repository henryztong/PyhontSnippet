import unittest
import json
import os
import datetime
import xmlrunner
from HTMLTestReportCN import *



class test_bestpayBase(unittest.TestCase):


	def setUp(self):
		"""初始化请求参数，每个用例开始时执行，用于测试环境的搭建和销毁"""
		pass

	def tearDown(self):
		# 还原数据，每个用例结束时执行
		pass

	def test_timeCheck(self):	
		# 对返回结果进行校验
		self.assertEqual(response['code'],200,'备注信息')


	def test_timeCheck2(self):	

		self.assertEqual(response['code'],200,'备注信息')



if __name__ == '__main__':
	# 按照ASCII码顺序执行用例
	# a = unittest.main()
	# print(a)
	
	
	# 构造测试集
	test_suite = unittest.TestSuite()
	test_suite.addTest(unittest.makeSuite(test_bestpayBase))

	# 1、生成文本报告
	# write_url = './reports/log.txt'
	# runner = unittest.TextTestRunner()
	# re = runner.run(test_suite)
	# with open(write_url,'w',encoding='utf-8') as f: 
	# 	f.write(str(re))


	# 2、生成html报告的路径
	file_name = os.path.split(__file__)[-1].split(".")[0]
	time = datetime.datetime.now()
	# 生成时间戳
	# now_time = datetime.datetime.strftime(time,'%Y%m%d%H%M%S') # 精确到秒
	now_day = datetime.datetime.strftime(time,'%Y%m%d') # 精确到天
	new_name = 'report_' + file_name + '_' +now_day + '.html'
	# print(new_name)
	path = './%s' % (new_name)
	# print(path)
	fp = open(path,'wb')
	#生成测试报告
	runner2 = HTMLTestRunner(
		stream=fp,
		title='基本准入子模块测试用例报告',
		description='测试情况如下',
		tester='henry'
		)
	#运行测试用例
	runner2.run(test_suite)
	# 关闭文件，否则会无法生成文件
	fp.close()


	# 3、生成xml格式的报告，方便上传到Jenkins
	# runner3 = xmlrunner.XMLTestRunner(output='./reports')
	# runner3.run(test_suite)






	# 测试结果说明：.代表用例执行通过，两个点表示两个用例执行通过。F表示用例执行不通过









