#!/usr/bin/python  
# -*- coding:utf8 -*-   
import os  

class DiretoryTree(object):
    """
python生成文件目录树：方法二只使用os
该方法有待优化

    """
    def __init__(self, path='.',filename='tempDire.txt'):
        super(DiretoryTree, self).__init__()
        self.data = ''  # 类中全局变量
        # 如果不自定义路径和文件名则用初始化的值，pathname='.'表示当前路径，filename='tempDire.txt')表示保存到tempDire.txt文件中
        # self.pathname = path
        self.filename = filename
        self.allFileNum = 0  # 文件计数器

    # def set_path(self,path):
    #     self.pathname = path # 封装一个方法来自定义设置路径

    def set_filename(self,filename):
        self.filename = filename # 封装一个方法来自定义要保存的文件信息

    def diretree(self,n=1,i=1,path='.'):  

        # 创建一个空列表用来保存所有文件夹
        dirList = []  
        # 创建一个空列表用来保存所有文件  
        fileList = []  
        # 返回path指定的文件夹包含的文件或文件夹的名字的列表 ，不包含本路径的文件名
        files = os.listdir(path)  

        # 将文件夹和文件进行分类
        for f in files:  
            # 调试打印
            # print(f)
            # print(type(f[0]))
            if(os.path.isdir(path + '/' + f)):  
                # 添加文件夹
                dirList.append(f)  
            if(os.path.isfile(path + '/' + f)):  
                # 添加文件  
                fileList.append(f)  
        # 打印树形目录逻辑
        # if n <= i: #  判断递归到哪一层   
        for dl in dirList:  # 遍历当前路径下的所有文件夹
            if dl[0] == '.': # 过滤隐藏文件
                pass
            else:
                self.data += '    |' * n + '-' * 4 + dl + '\\' + '\n'
                # print('    |' * n + '-' * 4, dl)   
                # 打印目录下的所有文件夹和文件，目录级别+1  
                self.diretree((n + 1),i,path + '/' + dl)  
        for fl in fileList:  # 遍历当前路径下的所有文件
            if fl[0] == '.' or fl[-1]!='d':  # 过滤隐藏文件
                pass
            else:
                self.data += '    |'* n +'-' * 4 + fl + '\n'
                # 打印文件  
                # print('    |' * n +'-'*4 , fl)  
                # 随便计算一下有多少个文件  
                self.allFileNum += 1  

        return(self.data)

    def save_file(self):
        # 文件IO的特殊语法，将拼接好的内容写入到指定的文件中
        with open(self.filename,'w',encoding='utf-8') as f: 
            f.write(self.data)

if __name__ == '__main__':  
    # url = '/Volumes/B/MyWorkspace/superManPro/test_AutoCheck2'
    url = '/Volumes/B/MyWorkspace/Seafile/测试小组资料/测试用例'
    # url = '/Volumes/B/我的工作文档/superManPro'
    dire = './diretree.txt'
    # dire = '/Volumes/B/MyWorkspace/superManPro/test_AutoCheck2/ProStructure.md'
    print('-' * 5,os.path.basename(url))
    MyTree = DiretoryTree()
    MyTree.set_filename(dire)
    # MyTree.set_path(url)
    print(MyTree.diretree(i=1,path=url) )
    print('总文件数 =',MyTree.allFileNum)
    MyTree.save_file()


