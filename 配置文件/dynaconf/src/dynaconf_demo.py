from dynaconf import settings
# 官网：https://dynaconf.readthedocs.io/en/latest/
# 示例：https://github.com/rochacbruno/dynaconf/tree/master/example
# 多文件夹操作：https://github.com/rochacbruno/dynaconf/tree/master/example/multiple_folders


# 环境配置实现原理：从What happens is开始
# https://dynaconf.readthedocs.io/en/latest/guides/usage.html#the-settings-files


# 使用讲解
# https://www.cnblogs.com/zhangyafei/p/10265072.html



# 对应配置文件settings.toml

# print all values in the file
# using [default] + [development] + [global] values
# 默认是打印出settings.toml中[development]的信息，可以通过修改环境变量.env文件重新设定默认配置


# print('* All values')
# print(settings.HOST)
# print(settings.PORT)
# print(settings.USERNAME)
# print(settings.PASSWORD)
# print(settings.LEVELS)
# print(settings.TEST_LOADERS)
# print(settings.MONEY)
# print(settings.AGE)
# print(settings.ENABLED)
# print(settings.CUSTOM)

# print('* Switiching to production')
# # using [production] env values for context
# with settings.using_env('PRODUCTION'):
#     print(settings.CUSTOM)
#     print(settings.HOST)

# print('* Switiching to development')
# # back to default [development] env
# print(settings.get('CUSTOM'))
# print(settings.HOST)

# print('* Switiching to production')
# # set env to [production]:
# settings.setenv('production')
# print(settings.HOST)
# print(settings.CUSTOM)

# print('* Switiching to development')
# # back to [development] env again
# settings.setenv()
# print(settings.HOST)
# print(settings.get('INEXISTENT'))  # None

# print(settings.WORKS)