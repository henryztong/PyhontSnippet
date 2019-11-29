# 导入:
from sqlalchemy import Column, Integer, String, create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Table
import mysql.connector

# 创建对象的基类
Base = declarative_base()

# 创建一个类与user_extend_yi表映射，并自定义user_extend_yi表的列名作为属性
class User_extend_yi(Base):
	# Common subclasses of TypeEngine include String, Integer, and Boolean.类中属性常用定义类型包括String, Integer, and Boolean。
	__tablename__ = 'user_extend_yi' # 类对应的数据库表

	# 属性对应的表中列
	id = Column(Integer, primary_key=True) # 主键不可缺失，如果表中主键id是序号且为int型，则这里要定义为Integer
	apply_no = Column(String(20))
	phone = Column(String(20))
	# bank_mobile_no= Column(String(20))
	# create_time=Column(Integer)
	user_name=Column(String(20))
	# seller_main_id=Column(Integer)
	# id_number=Column(String(20))
	# id_validity_end=Column(String(20))
	# user_main_id=Column(Integer)
	# residence_address=Column(String(20))
	# is_married=Column(Integer)
	# company_name=Column(String(20))
	# company_address=Column(String(20))
	# bank_no=Column(String(20))
	# longitude=Column(String(20))
	# latitude=Column(String(20))
	# education=Column(Integer)
	# industry_type=Column(Integer)
	# salary=Column(Integer)
	# seller_province=Column(String(20))
	# def __repr__(self):
	# 	# 重写__repr__方法中的return值，在session调用中会执行__repr__方法从而打印出结果
	# 	return "<User_extend_yi(apply_no='%s', phone='%s', user_name='%s')>" % (self.apply_no, self.phone, self.user_name)

# 查看类对应的表
print(User_extend_yi.__table__)

# 连接数据库并实例化一个对象,'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://sp_man:Spman@123#admin.com@119.23.145.20/fqcr')

# 创建一个类并自动获取对应表中的列名作为属性
class User_photo_yi(Base):
	__table__ = Table("user_photo_yi", Base.metadata,autoload=True, autoload_with=engine)

# 创建一个类的实例，用于新增和修改数据
ed_user_extend_yi = User_extend_yi(apply_no='77701',phone='5',user_name='henry')

# 创建session用来操作数据库
DBSession = sessionmaker(bind=engine)
session  = DBSession()

# 新增数据
session.add(ed_user_extend_yi)
session.commit() # 增、删、改等数据库事务操作必须提交才保存成功，不然只是在session缓存中修改

print(ed_user_extend_yi.phone) # 查看修改前的值
ed_user_extend_yi.phone = '10' # 对缓存中的某个属性进行修改，只要没有提交就不会改变数据库中的值
print(ed_user_extend_yi.phone) # 查看修改后的值

# print(session.dirty) # 查看缓存中的信息
# print(session.new) # 查看缓存中的信息


# 语法结构，query = select，filter = where
# one()表示查询唯一的结果，没有或多条时报错
a = session.query(User_extend_yi).filter(User_extend_yi.apply_no=='77701').one()

# all() 表示查询所有行
b = session.query(User_extend_yi,User_extend_yi.phone).filter(User_extend_yi.apply_no=='77701').all()

# 不要where语句查询表中所有列所有行
c = session.query(User_extend_yi).all()

# first() 表示返回查询到的第一条数据
a = session.query(User_extend_yi.apply_no).filter(User_extend_yi.apply_no=='77701').first()

# 查询到多行时可以使用遍历的方式获取每个结果
for row in a:
	# print(row)
	print(row.phone)

# 结束关闭session
session.close()















































