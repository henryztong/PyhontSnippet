import multiprocessing

def pro1(pipe):
	pipe.send('hello')
	print('程序1',pipe.recv())

def pro2(pipe):
	print('程序2',pipe.recv())
	pipe.send('hello,too')

if __name__ == '__main__':
	multiprocessing.freeze_support()
	pipe = multiprocessing.Pipe()

	p1 = multiprocessing.Process(target=pro1,args=(pipe[0],))
	p2 = multiprocessing.Process(target=pro2,args=(pipe[1],))
p1.start()
p2.start()
p1.join()
p2.join()