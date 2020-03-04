# 读取xls表操作
import json
import datetime
import xlrd
import codecs
import re


class XLUserinfo(object):
  """读取Excel表操作"""
  def __init__(self,path = ''):
    self.xl = xlrd.open_workbook(path) #打开excel文件，并将其赋给一个对象xl

  def floattostr(self,val): 
    # 浮点型数据转换为字符串
    if isinstance(val,float): 
      val = str(int(val))
    return val

  def get_sheet_info(self): 
  # 得到某张表中的所有数据
    listkey = ['key','value']
    infolist = []
    txt_url = './2016-6成都工程项目信息号码.txt'
    with open(txt_url,'w+',encoding='utf-8') as config:
      if config.read():
        pass
    config =open(txt_url,'a+',encoding="utf-8")# a+表示在文本结尾继续写入内容
    for row in range(1,self.sheet.nrows): # 根据行数进行遍历,从第二行开始
      info = [ self.floattostr(val) for val in self.sheet.row_values(row)] 
      # 获取某一行数据，返回的是列表类型。并对里面的数字类型数据进行解析
      # info = self.sheet.row_values(row) # 获取的数值类型是浮点型的，需要转化为字符串
      # tmp = zip(listkey,info) # 将列表的2个值打包为元组对象
      # infolist.append(dict(tmp)) # 将元组数据转换为字典并添加到新列表中
      # print(info)
      templist = []     

      for i in range(0,5):  # 只取两列，第一列和第二列
        # print(info[i])
        # print(type(info[i]))
        pattern2 = re.compile('(联系人: [\u4e00-\u9fa5 ]*)|(电话: [0-9]* [0-9]* [0-9]*)')
        k = pattern2.finditer(info[i])
        for x in k:
          print(x.group())
          infolist.append(x.group())
          # print(x.group().split(': '))

          config.write(x.group()+'\n')
    config.close()

    return infolist

  def get_sheetinfo_by_name(self,name): #通过名字获取表
    self.sheet = self.xl.sheet_by_name(name)  # 修改了xl.sheet方法使其根据表名获取表
    return self.get_sheet_info() #获取表中数据，并返回获取的数据

  def get_sheetinfo_by_index(self,index): #通过索引获取表
    self.sheet = self.xl.sheet_by_index(index)
    return self.get_sheet_info()


if __name__ == '__main__':
  parameter = r'./2020qyy.xls'
  parameter2 = r'./2016-6成都工程项目信息.xls'
  r = XLUserinfo(parameter)
  a = r.get_sheetinfo_by_index(0)
  print(a)













