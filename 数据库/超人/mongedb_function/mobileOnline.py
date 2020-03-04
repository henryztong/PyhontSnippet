from mongeBase import Mongedbtest
from mongeBase import integration_result

class MobileOnline(Mongedbtest,integration_result):
	"""
	在网时长输出状态：
					查无
					0-3个月
					3-6个月
					6-12个月
					12-24个月
					24个月+
					第三方错误
					其他
	"""
	def __init__(self):
		super(MobileOnline, self).__init__()

	def test2(self):
		# 调试代码
		self.test1()
	def mobileOnline_fix(self,code,desc,phone):
		# 修改单独调聚合的接口查询到的数据
		self.mobileOnline(code,desc,phone)
	def integration_mobileOnline_fix(self,mobile,mobileOnline_type):
		# 修改整合结果返回的数据
		self.integration_mobileOnline(mobile,mobileOnline_type)
	


if __name__ == '__main__':
	a = MobileOnline()
	# code = '03'
	# desc = '(24,+)'
	# phone = '15500000078'
	# a.mobileOnline_fix(code,desc,phone)
	# 要查询的号码
	mobile = '15500000078'
	# 要修改的状态值
	mobileOnline_type = '24个月+'
	a.integration_mobileOnline_fix(mobile,mobileOnline_type)


















