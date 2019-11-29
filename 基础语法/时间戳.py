import datetime
import time
import xmlrpc

# # 格式化时间戳
# print(help(datetime))
# newtime = datetime.datetime.now()
# print(time)
# print(type(time))
# nowtime = datetime.datetime.strftime(newtime,'%Y%m%d%H%M%S')# 精确到秒
# nowday = datetime.datetime.strftime(time,'%Y%m%d')# 精确到天
# newtime = str(time).split('.')[0]
# print(newtime)
# print(nowtime)


# a = '2019-02-21 08:26:19.314522'
# print(help(time))
print(time.time())
# print(int(time.time()))
print(time.ctime())
# print(time.localtime())
print(time.strftime("%Y%m%d%H%M%S"))

# 时间化格式+时间戳
s = str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
s += str(int(time.time()))
print(s)




d = datetime.timedelta(days=2)
print(d)


timeStamp = time.strftime("%Y%m%d%H%M%S")
print(timeStamp)
timeStamp = int(time.time())
print(timeStamp)





