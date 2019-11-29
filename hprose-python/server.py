
#!/usr/bin/env python
# encoding: utf-8

import hprose
# print(help(hprose))
def hello(name):
	return 'Hello1111 %s!' % name

def main():
	server = hprose.HttpServer(port = 8181)
	server.addFunction(hello)
	server.start()

if __name__ == '__main__':
	main()