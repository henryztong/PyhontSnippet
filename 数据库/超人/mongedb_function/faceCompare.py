from mongeBase import Mongedbtest


class Face_compare(Mongedbtest):
	"""人脸对比度修改，x代表分数,只能输入数字;url代表身份证正面照片地址"""
	def __init__(self):
		super(Face_compare, self).__init__()

	def face_compare_fix(self,x,url):
		self.face_compare(x,url)

	def test2(self):
		# 调试代码
		self.test1()


if __name__ == '__main__':
	# 人脸对比度修改方法，x代表分数,只能输入数字;url代表身份证正面照片地址
	x = 40
	url = "http://fqcr.oss-cn-shenzhen.aliyuncs.com/201809/201809131525353833.jpg"	
	case1 = Face_compare()
	case1.face_compare_fix(x,url)



