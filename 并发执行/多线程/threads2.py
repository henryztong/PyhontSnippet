from time import sleep,ctime
import threading

def super_player(file_,time):
	for i in range(2):
		print('%s ，时间%s'%(file_,ctime()))
		sleep(time)

lists = {'樱花.mp3':4,'英雄联盟.mp4':1,'含笑有白鹭.mp3':3}

threads = []
files = range(len(lists))

for file_,time in lists.items(): # 创建多个程序
	t = threading.Thread(target=super_player,args=(file_,time))
	threads.append(t) #将线程加入到列表中

if __name__ == '__main__':
	# print(threads)
	for i in files:
		print(threads[i])
		threads[i].start()

	for i in files:
		threads[i].join()