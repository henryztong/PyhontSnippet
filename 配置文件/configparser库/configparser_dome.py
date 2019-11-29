import configparser
# 对应配置文件config.ini
# 官网：https://docs.python.org/zh-cn/3/library/configparser.html

#初始化类
cp = configparser.ConfigParser()
cp.read("config.ini")

#得到所有的section，以列表的形式返回
section = cp.sections()[0]
print(section)

#得到该section的所有option
print(cp.options(section))

#得到该section的所有键值对
print(cp.items(section))

#得到该section中的option的值，返回为string类型
print(cp.get(section, "db"))

#得到该section中的option的值，返回为int类型
print(cp.getint(section, "port"))



