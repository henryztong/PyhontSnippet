from mongeBase import Mongedbtest
from mongeBase import integration_result

class SpendLevel(Mongedbtest,integration_result):
	""" 修改【月消费档次】数据
	消费档次值
0
(0,5]
[0,50]
(20,50]
(50,100]
(100,200]
(115,+)
(200,+)
库无记录
其他
	"""
	def __init__(self):
		super(SpendLevel, self).__init__()

	def spendLevel_fix(self,x,url):
		self.integration_spendLevel(mobile,spendLevel_type)

	def test2(self):
		# 调试代码
		self.test1()


if __name__ == '__main__':
	# 修改【月消费档次】数据
	mobile = '15500000078'
	spendLevel_type = "(115,+)"	
	case1 = SpendLevel()
	case1.spendLevel_fix(mobile,spendLevel_type)



