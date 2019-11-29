from time import sleep,ctime
import multiprocessing

def super_player(file_,time):
	for i in range(2):
		print('开始播放:%s；播放时间%s'%(file_,ctime()))
		sleep(time)
lists = {'爱情买卖.mp3':5,'阿凡达.mp3':4,'凤凰传奇':3}
threads = []
files = range(len(lists))

for file_,time in lists.items():
	t = multiprocessing.Process(target=super_player,args=(file_,time))
	threads.append(t)

if __name__ == '__main__':
	for t in files:
		threads[t].start()
	for t in files:
		threads[t].join()
	print('结束时间%s' % ctime())