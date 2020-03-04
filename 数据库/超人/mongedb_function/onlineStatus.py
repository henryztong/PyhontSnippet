from mongeBase import Mongedbtest
from mongeBase import integration_result

class OnlineStatus(Mongedbtest,integration_result):
	"""	
	# 联系人在网状态，输出状态：
							库无记录
							正常在用
							在网但不可用
							不在网
							停机
							销户
							参数错误或暂不支持该手机号查询
							无短信功能卡
							其他
	"""
	def __init__(self):
		super(OnlineStatus, self).__init__()

	def test2(self):
		# 调试代码
		self.test1()
	def onlineStatus_fix(self,mobile_online_status_info,phone):
		# 修改单独调用聚合查看在网状态
		self.onlineStatus(mobile_online_status_info,phone)

	def integration_onlineStatus_fix(self,mobile,onlineStatus_type):
		# 修改整合结果返回的数据
		self.integration_onlineStatus(mobile,onlineStatus_type)


if __name__ == '__main__':
	a = OnlineStatus()
	# mobile_online_status_info = '正常在用'
	# phone = '15500000237'
	# a.onlineStatus_fix(mobile_online_status_info,phone)
	moblie = '15500000239'
	onlineStatus_type = '正常在用'
	a.integration_onlineStatus_fix(moblie,onlineStatus_type)


