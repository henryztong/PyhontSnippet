import time
import threading

def music(loop):
	for i in range(loop):
		print("播放音乐 %s" % time.ctime())
		time.sleep(2)


def movie(loop):
	for i in range(loop):
		print("播放电影 %s" % time.ctime())
		time.sleep(5)

threads = []

t1 = threading.Thread(target=music,args=(2,))
threads.append(t1)

t2 = threading.Thread(target=movie,args=(2,))
threads.append(t2)


if __name__ == '__main__':
	# music(2)
	# movie(2)
	# print("最后结束 %s" % time.ctime())

	for t in threads:
		t.start()

	for t in threads:
		t.join()

