from sqlite3 import connect

# 定义一个数据库，生成在当前目录中
db_name = 'test.db'

# 创建连接
con = connect(db_name)
# 创建游标
cur = con.cursor()

# 创建表
# cur.execute('create table star (id integer,name text,age integer,address text)')
# # 设定数据
# rows = [(1,'小米',22,'北京'),(2,'小明',23,'天津'),(3,'小王',24,'成都')]


# # 遍历并插入数据
# for item in rows:
# 	cur.execute('insert into star (id,name,age,address) values (?,?,?,?)',item)
# # 提交修改内容
# con.commit()
# # 遍历并查询数据
# cur.execute('select * from star')
# for row in cur:
# 	print(row)


# 修改
# cur.execute('update star set age=? where id=?',(16,3))
# con.commit()
# # 遍历并查询数据
# cur.execute('select * from star')
# for row in cur:
# 	print(row)

# 删除
cur.execute('delete from star where id = ?',(3,))
con.commit()
# 遍历并查询数据
cur.execute('select * from star')
for row in cur:
	print(row)

# 使用完数据库后关闭连接
con.close()







