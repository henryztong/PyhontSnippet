def isDistingct(self,appidlist)
'''
去重检测
: param appidlist
: return:
'''
# 内部自检是否有去重
initlen = len(appidlist)
afterlen = len(list(set(appidlist)))
if initlen == afterlen:
	self.lg.info(u'客户端app展示无重复')
else:
	self.lg.info(u'客户端app展示有重复')
self.assertEqual(initlen,afterlen)
# 与redis 进行内容比较
self.redisc = RedisConnect()
self.redisc.redisConnect()
imei = self.headers['id']
redisapplist = self.redisc.getRedisApps(imei)
set_tmp = set(appidlist) & set(redisapplist)
list_tmp = list(set_tmp)
self.assertEqual(list_tmp,[])







