from mongeBase import Mongedbtest


class WkCheck(Mongedbtest):
	"""白骑士审核，finalDecision代表状态，idcard代表被查询的身份证号"""
	def __init__(self):
		super(WkCheck, self).__init__()

	def test2(self):
		# 调试代码
		self.test1()
	def wkCheck_fix(self,finalDecision,idcard):
		self.wkCheck(finalDecision,idcard)


if __name__ == '__main__':
	# 白骑士审核，finalDecision代表状态，idcard代表被查询的身份证号
	finalDecision = 'Accept'
	idcard = '612423197012121023'
	a = WkCheck()
	a.wkCheck_fix(finalDecision,idcard)