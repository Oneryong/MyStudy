#!/usr/bin/env python
#coding:utf-8

"""
OS模块

目录操作：就是通过python来实现目录的创建，修改，遍历等功能。
目录操作需要调用os模块
import os
os.mkdir('/root/csvt')
"""
"""
常用操作：
1、创建目录
mkdir(path[, mode=0777])
makedirs(name, mode=511) //创建多级目录
2、移除目录
rmdir(path)
removedirs(path)  //删除多级目录
3、列出目录
listdir(path)
4、获取当前目录
getcwd()
5、更改目录
chdir(path)
6、分解目录，分别获取路径名、目录名和文件名
walk(top,topdown=True,onerror=None)
"""

import os

#os.mkdir('./test')
#os.rmdir('./test')
#print(os.listdir(os.getcwd()))


"""
系统垃圾清除小工具
方法：
递归函数 + os.walk()函数
"""

"""
列出所有文件
"""
#分别获取路径名称，文件目录名称，文件名称
def cur_file_name():
    for root, dir, files in os.walk(os.getcwd()):
        for file in files:
            #print(os.path.join(root, file))
            if ".c" == file[-2:] or ".cpp" == file[-4:] or ".txt" == file[-4:]:
                #print(os.path.join(root, file))
                return os.path.join(root, file)
        

print(cur_file_name())



#input("Press <Enter>")
os.system("pause")
