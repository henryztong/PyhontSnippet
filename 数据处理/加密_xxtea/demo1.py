# 官网：https://github.com/ifduyue/xxtea
# https://pypi.org/project/xxtea-py/1.0.3/

# 注意区分：xxtea-py 与 xxtea
import xxtea,base64
text = "123456"
key = "1234"
print(help(xxtea))
# print(xxtea.VERSION)
encrypt_data = xxtea.encrypt(text, key)
print(type(encrypt_data))
a = base64.b64encode(encrypt_data)
b = bytes.decode(a)
print(b)
print(type(b))

decrypt_data = xxtea.decrypt_utf8(encrypt_data, key)
print(text == decrypt_data);