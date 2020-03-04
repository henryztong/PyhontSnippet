# 官网：https://github.com/ifduyue/xxtea
# https://pypi.org/project/xxtea-py/1.0.3/

# 注意区分：xxtea-py 与 xxtea
# 字符串转16位key
# bytes和hex字符串之间的相互转换:https://www.cnblogs.com/japhasiac/p/7739846.html

import binascii,os

datastr='13'
#string 类型转换为byte
dataByte=str.encode(datastr)
#byte串 转换为16进制 byte串 ，比如 b'12' 转换为b'3132'
a=binascii.b2a_hex(dataByte)
print(a)
print(type(a))

#16 进制byte串  转换为string串，比如b'3132' 转换为"3132",用来显示
print(a.decode())

#16 进制string  转换为16位byte串，比如'1112' 转换为b"\x11\x12"，用来传输
print(bytes.fromhex("1112"))

print(bytes.fromhex("1112").decode())

print(os.urandom(16))
print(type(os.urandom(16)))
# print(os.urandom(16).decode())





