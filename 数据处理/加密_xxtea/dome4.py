import json,xxtea,base64,json
import urllib.parse
import requests
from hebao_import import input_data
from hashlib import sha1

class Encrypt(object):
    """
        
    """
    def get_reqData(self,path):
        # 读取文本中的值作为参数
        data = input_data()
        jsonDict = data.get_data(path)
        # print('字段 %s'%jsonDict)
        # print(type(jsonDict))

        # 排序
        jsonDictKeys = sorted(jsonDict)
        # print('排序 %s'%jsonDictKeys)

        string = ''
        for one in jsonDictKeys:
            # 拼接键与值
            string += one + jsonDict[one]
            # print(string)
            # print(type(string))
            codes = urllib.parse.quote(string)
            # print(codes)
            # print(type(codes))

        # print(codes)
        # print(type(codes))
        # print(codes.encode())
        # print(type(codes.encode()))
        
        # sha1加密
        s1 = sha1()
        s1.update(codes.encode())
        sign = s1.hexdigest()
        print('sha1加密 %s'%sign)

        # 字符串拼接
        sign = json.dumps(jsonDict) + sign
        # print('字符串拼接 %s \n'%sign)

        # xxtea加密
        key = "jT1kdbpWtdxQDDr9uC7/E5Hi4RaoFYg1" # 测试环境
        # key = "VMa1dSCYG5oVuUx/XabB78I+UYBMJ6MJ" # beta环境

        jsonValue = xxtea.encrypt(sign, key)
        jsonValue = base64.b64encode(jsonValue)
        reqData = bytes.decode(jsonValue)
        # print('xxtea加密结果 %s'%reqData)

        return reqData
        

if __name__ == "__main__":
    path = './data/3.1.2.1 授信申请接口.txt'
    key = "jT1kdbpWtdxQDDr9uC7/E5Hi4RaoFYg1"
    a = Encrypt()
    reqData = a.get_reqData(path)
    

    url = 'http://api.test.fenqichaoren.com/cmpay/credit/v1/apply'
    # url = 'http://api.test.fenqichaoren.com/cmpay/quota/v1/block'
    dic = {
    'reqData' : reqData,
    'clientId' :'07032'
    }

    result = requests.post(url,data=dic)
    config = result.text
    print(type(config))
    print(config)
    # print('\n')

    # # 将获取的数据使用分号分割,并将空格去掉
    # # 解密返回值
    # result = config.split('"')
    # k = result[3]

    # print(k)
    # print(type(k))

    # 解密
    # k = 'nmOsEGVreVeZeySrmoXsaKQ5JjHKhKk9IDIoiv0FeKTqxL2bjAVmU6I6yPp4Ktv\/GXalLGOqE+QeYus5K+5z2S327mxIhjXvnPAndTrepCFVCzTBNPeCIdoaH1mBskkc1xmFWkAHAJub5A+MSeU4fG6NvCm2gyLwh\/I2E9kVngWvvPJnqwiI8VgWMKDvcZQcWeJXkczTLkWngq5cxSo\/xK4vlpYf5TnTQFYEqg=='
    # b = base64.b64decode(k)
    # c = xxtea.decrypt(b, key)
    # print(c)

