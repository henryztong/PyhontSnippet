from sqlite3 import connect,Row

db_name = 'test.db'
con = connect(db_name)
# con.row_factory = Row
# cur = con.cursor()
##### 1. 行对象（row）简介 -------------------------------------------------------

# cur.execute('select * from star')
# # 获取行对象
# row = cur.fetchone()

# print(type(row))
# print('以列名访问：',row['name'])

# print('以索引访问：',row[1])
# print('以迭代访问：')
# for item in row:
# 	print(item)

# print('len():',len(row))

"""
输出结果：
<class 'sqlite3.Row'>
以列名访问： 小米
以索引访问： 小米
以迭代访问：
1
小米
22
北京
len(): 4
"""
##### 2. 批量数据库操作 -------------------------------------------------------
# - cur.executemany(sql_string,seq) -----------
# 设定批量执行的参数
# rows = [(3,'小王',24,'成都'),(4,'小秋',26,'重庆')]
# cur.executemany('insert into star (id,name,age,address) values(?,?,?,?)',rows)
# con.commit()
# 遍历并查询数据
# cur.execute('select * from star')
# for row in cur:
# 	print(row)
# 	for j in row:
# 		print(j)

# - cur.executescript(sql_string) -----------
cur = con.cursor()

# 创建一个字符串脚本
sql_str = """
create table test(id integer,name text);
insert into test (id,name) values(1,'Lily');
insert into test (id,name) values(2,'WangLei');
insert into test (id,name) values(3,'Haihua')
"""
# 执行sql脚本
# cur.executescript(sql_str)

cur.execute('select * from test')
for row in cur:
	print(row)
	print(type(row))
	for j in row:
		print(j)

con.commit()

con.close()














		
