# 字节与字符串的转换.py
#bytes object
byte = b"byte example"
# str object
str1 = "str example"

# str to bytes 字符串转字节
a1 = bytes(str1, encoding="utf8")
print(a1)
# bytes to str  字节转字符串
a2 = str(byte, encoding="utf-8")
print(a2)

# an alternative method
# str to bytes  字符串转为字节
b1 = str.encode(str1)
print(b1)
# bytes to str  字节转为字符串
b2 = bytes.decode(byte)
print(b2)