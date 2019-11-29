# 原文：https://blog.csdn.net/First_name0101/article/details/80586665
# 先举个栗子：

a=5  #整型

isinstance(a,int)

True     #输出


再举个栗子：

a=5.0  #浮点型

isinstance(a,int)

False   #输出


其实在这里已经可以看出isinstance方法的作用，即判断括号前的变量a是不是符合

括号后我们自身所定义的变量类型，第一个例子中，a为整型，符合isinstance里的

条件——即“int”型。

在第二个栗子当中，由于a=5.0，显然为浮点型，不满足int的条件，故输出为False.
————————————————
版权声明：本文为CSDN博主「lucas_s」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/First_name0101/article/details/80586665





#介绍一下isinstance 这个内置函数
#  isinstance(实例化对象,类)作用: 判断实例化对象是不是该类实例化的,是返回True,不是返回False
#example
 
#定义积基类
class Base:
    pass
 
 
class Test1(Base):
    pass
 
 
#实例化Base
b = Base()
 
 
#这个应该返回False 因为Test1是继承Base产生的新的类(Test1最为一个新的类,,所以b的实例不能包含在内)
print isinstance(b,Test1)    #这个很重重要
#下面返回True
print isinstance(b,Base)
 
 
t = Test1()
#返回True Test1实例化继承Base (Test1<Base)
print isinstance(t,Base)    #这个很重重要
#返回True
print isinstance(t,Test1)
原文链接：https://blog.csdn.net/liuxingyu_21/article/details/30457487