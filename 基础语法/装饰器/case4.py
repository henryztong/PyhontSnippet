wrapper 函数指定关键字函数：

def wrapper(*args, **kwargs):
        # args是一个数组，解决参数个数；kwargs一个字典，解决默认参数值
        logging.warn("%s is running" % func.__name__)
        return func(*args, **kwargs)
return wrapper