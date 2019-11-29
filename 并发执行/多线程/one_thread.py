import time

def music(loop):
	for i in range(loop):
		print("播放音乐 %s" % time.ctime())
		time.sleep(2)


def movie(loop):
	for i in range(loop):
		print("播放电影 %s" % time.ctime())
		time.sleep(4)


if __name__ == '__main__':
	music(2)
	movie(2)
	print("结束 %s" % time.ctime())
	




