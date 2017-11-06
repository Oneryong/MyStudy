#!/usr/bin/env python
#coding:utf8

import os
import sys
import re

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
#关闭文件对象。
FileObject.close()

#每次读取文件的一行。
#size：指每行每次读取size个字节，直到行的末尾。
String = FileObject.readline([size])

#多行读，返回一个列表。
#size：每次读入size个字符，
#然后继续按size读，而不是每次读入行的size个字符。
List = FileObject.readlines([size])

#读出文件的所用内容，并复制给一个字符串。
#size：读出文件前的size个字符，并输出给字符串，
#此时文件的指针指向size处。
String = FileObject.read([size])

#返回当前行，并将文件指针到下一行。
#是迭代器的一个方法。
FileObject.next()

#写入一个字符串
FileObject.write(string)

#写入一个列表
FileObject.writelines(List)

#文件指针移动的方法。
#选项 = 0时，表示将文件指针指向从文件头部到“偏移量”字节处。
#选项 = 1时，表示将文件指针指向从文件的当前位置，向后移动“偏移量”字节。
#选项 = 2时，表示将文件指针指向从文件尾部向前移动“偏移量”字节。
#偏移量可以为负数，表示按既定方向的反方向。
FileObject.seek(偏移量, 选项)

#提交更新，刷新文件。
FileObject.flush()
"""
fo = open(os.path.join(cur_file_dir(), "testfile.txt"), "r+")
string = fo.readline()
print(string)
fo.close()

fo = open(os.path.join(cur_file_dir(), "testfile.txt"), "r+")
list = fo.readlines()
print(list)
fo.close()

fo = open(os.path.join(cur_file_dir(), "a.txt"), "r+")
alists = fo.readlines()
print(alists)
count = 0
for s in alists:
    li = re.findall("hello", s)
    if len(li) > 0:
        count = count + len(li)
print("Search", count, "hello")
fo.close()

fo = open(os.path.join(cur_file_dir(), "a.txt"), "r+")
alists = fo.readlines()
print(alists)
newlist = []
for s in alists:
    s = s.replace("hello", "csvt")
    newlist.append(s)
fo.write("")
print(newlist)
fo.writelines(newlist)
fo.close()


input("Press <Enter>")
