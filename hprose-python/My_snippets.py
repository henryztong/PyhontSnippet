s = '1,2,''ww'
# 将文本中读取的字符串转化为列表
result = s.split(',') 
# 将列表转换为字典
list_key = ['applyNo','userMobile','bank_mobile_no','create_time','username','seller_main_id']
list_value = result
baseValidateInput = dict(zip(list_key,list_value))

# 将字符串转化为字典，方便读取值
dic = json.loads(strings)

# 将字典转换为字符串输出
result = json.dumps(select_result) 


class MyClass:
    """一个简单的类实例"""
    i = 12345
    def function():
    	pass
    def f(self):
        return 'hello world'
 
# 实例化类
# x = MyClass()

# 访问类的属性和方法
print("MyClass 类的属性 i 为：", MyClass.i)
print("MyClass 类的方法 f 输出为：", MyClass.function())
















