import xxtea,base64
text = "123456"
key = "123456"
# print(help(xxtea))
encrypt_data = xxtea.encrypt(text, key)
print(type(encrypt_data))
a = base64.b64encode(encrypt_data)
b = bytes.decode(a)
print(b)
print(type(b))

decrypt_data = xxtea.decrypt_utf8(encrypt_data, key)
# print(text == decrypt_data);