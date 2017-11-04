#!/usr/bin/env python
#coding:utf8

import os
import sys

global path
path = os.getcwd()
#path = os.path.abspath(os.curdir)
#path = os.path.abspath(".")

#获取脚本文件的当前路径
def cur_file_dir():
    #获取脚本路径
    tempPath = sys.path[0]
    """
    判断为脚本文件还是py2exe编译后的文件，
    如果是脚本文件，则返回的是脚本的目录；
    如果是py2exe编译后的文件，则返回的是编译后的文件路径
    """
    if os.path.isdir(tempPath):
        return tempPath
    elif os.path.isfile(tempPath):
        return os.path.dirname(tempPath)
        
#print(cur_file_dir())

#分别获取路径名称，文件目录名称，文件名称
def cur_file_name():
    for root, dir, files in os.walk(os.getcwd()):
        for file in files:
            #print(os.path.join(root, file))
            if ".c" == file[-2:] or ".cpp" == file[-4:] or ".txt" == file[-4:]:
                #print(os.path.join(root, file))
                return os.path.join(root, file)
                
#cur_file_name()

"""
文件读写操作：
1、文件的打开和创建
2、文件读取
3、文件写入
4、内容查找和替换
5、文件删除、复制、重命名
6、目录操作
"""
""" 
案例：
1、目录分析器
2、杀毒软件
3、系统垃圾清理工具
"""

"""
Python文件读写：
函数为open或file。
格式：
file_handler = open(filename, mode)
mode:
r     只读
r+    读写
w     写入，先删除
w+    读写，先删除
a     写入，在文件末尾追加，文件不存在则创建
a+    读写，在文件末尾追加，文件不存在则创建
b     打开二进制文件，和上面模式一起使用 
"""
fo = open(os.path.join(cur_file_dir(), "testfile.txt"), "r+")
fo.read()
fo.write("abc")
fo.close()

"""
文件对象方法：
FileObject.close()
String = FileObject.readline([size])
List = FileObject.readlines([size])
String = FileObject.read([size])

FileObject.next()
FileObject.write(string)
FileObject.writelines(List)
FileObject.seek(偏移量, 选项)
FileObject.flush()
"""

input("Press <Enter>")