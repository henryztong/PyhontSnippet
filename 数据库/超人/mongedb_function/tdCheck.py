from mongeBase import Mongedbtest


class TdCheck(Mongedbtest):
	"""同盾分审核,final_score代表分值，idcard代表被查询的身份证号"""
	def __init__(self):
		super(TdCheck, self).__init__()

	def test2(self):
		# 调试代码
		self.test1()
	def tdCheck_fix(self,final_score,idcard):
		self.tdCheck(final_score,idcard)


if __name__ == '__main__':

	# 同盾分审核,final_score代表分值，idcard代表被查询的身份证号
	final_score = 10
	idcard = '110101198203078451'
	a = TdCheck()
	a.tdCheck_fix(final_score,idcard)

