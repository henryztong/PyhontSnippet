# https://ishuo.cn/

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError
url1 = 'http://www.pythonscraping.com/pages/page1.html'
url2 = 'http://www.pythonscraping.com/pages/warandpeace.html'

def getTitle(url):
  try:
    html = urlopen(url)
  except HTTPError as e:
    print(e)
    return None
  except URLError as e:
    print(e)
    return None

  try:
    bs = BeautifulSoup(html.read(),'html.parser')
    # print(bs)
    print(type(bs))
    namelist = bs.find_all('span',{'class':'green'})
    # print(namelist)
    print(type(namelist))
    for name in namelist:
      print(name.get_text())
  except AttributeError as e:
    print(e)
    return None
  return namelist
    
  
getTitle(url2)






