#!/usr/bin/env python
# encoding: utf-8

import hprose

def main():
	#  表：user_extend_yi， `apply_no` varchar(100) DEFAULT NULL COMMENT '申请流水号',
	#  触发自动审核
	client = hprose.HttpClient('http://audit.test.fenqichaoren.com/Automaticaudit/Bestpay/api')
	print(client.queue_start({"apply_no":"2018081404"}))

if __name__ == '__main__':
	main()


