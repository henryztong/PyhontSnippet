# 使用dynaconf管理配置文件

## 官方示例
https://github.com/rochacbruno/dynaconf/tree/master/example/yaml_example

## 官方文档
https://dynaconf.readthedocs.io/en/latest/guides/usage.html#the-settings-files

## 使用示例：
```python
from dynaconf import settings

print(settings.API_URL)

print("* Switiching to production")
# using [production] env values for context
with settings.using_env("PRODUCTION"):
    print(settings.CUSTOM)
    print(settings.HOST)

print("* Switiching to development")
# back to default [development] env
print(settings.get("CUSTOM"))
print(settings.HOST)

print("* Switiching to production")
# set env to [production]:
settings.setenv("production")
print(settings.HOST)
print(settings.CUSTOM)

print("* Switiching to development")
# back to [development] env again
settings.setenv()
print(settings.HOST)
print(settings.get("INEXISTENT"))  # None


```


