# 参考：https://www.cnblogs.com/foreversun92/p/11228079.html

import requests
import re
import sys


def kanzhun():
  temp_dic = []
  for i in range(1,6):
    # 要爬取网页的链接
    # i代表第几页
    url = 'http://www.kanzhun.com/pla12c13p'+str(i)+'.html?ka=paging'+str(i)
    headers = {
      'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    }
    reponse = requests.get(url,headers=headers,timeout=30)
    data = reponse.content.decode('utf-8')
    # 正则表达式
    res_title = re.findall('<a ka=".*-title" href="/.*?" target="_blank">(.*?)</a>',data)
    # print(res_title)
    temp_dic += res_title
  print(temp_dic)


def anjuke():
  temp_dic = []
  for i in range(1,2):
    # 要爬取网页的链接
    # i代表第几页
    url = 'https://cd.fang.anjuke.com/wuye/p'+str(i)
    print(url)
    headers = {
      'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    }
    reponse = requests.get(url,headers=headers,timeout=30)
    data = reponse.content.decode('utf-8')
    # print(data)
    # 正则表达式
    res_title = re.findall('<a href= ".*?" target="_blank" class="clearfixed tit"><h3 class="lp-title">(.*?)</h3><span class="lp_num">(.*?)</span></a>',data)
    
    print(res_title)
    temp_dic += res_title
  print(temp_dic)

def stop():
  sys.exit()



if __name__ == '__main__':
  anjuke()









