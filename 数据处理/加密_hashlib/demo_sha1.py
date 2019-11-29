# hashlib.py


from hashlib import sha1

pwd = '123'
s1 = sha1()

s1.update(pwd.encode())
mima = s1.hexdigest() # 16位密码，40位字符串
print(mima)


