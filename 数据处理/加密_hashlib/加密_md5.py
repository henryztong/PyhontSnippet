# -*- coding:utf-8 -*-
import requests
import hashlib
# 使用MD5加密方法
def main():
    payload = {
      'apiVersion':'K10',
      # 'apiUrl':'cancelgoodsnotify',
      'apiUrl':'get_p2p_user',
      'reqTime':'1524447895',
    }
    payload['key'] = my_md5(my_md5(payload['apiUrl']) + my_md5(payload['reqTime']))
    print(payload['key'])

def my_md5(str):
    hl = hashlib.md5()
    hl.update(str.encode())
    return hl.hexdigest()

if __name__ == '__main__':
    main()

    # 62cf8d889f5a398be5c274a12386fd69
    # 62cf8d889f5a398be5c274a12386fd69