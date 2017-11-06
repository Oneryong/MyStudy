#!/usr/bin/env python
#coding:utf8

from __future__ import division
 
"""
switch分支结构
1、类似if elif else结构
2、python没有提供switch结构
3、利用字典实现switch功能
4、首先定义一个字典，其次调用字典的get()获取相应的表达式。
5、例子：
    {1:case1, 2:case2}.get(x, lambda *arg, **key:)()
"""

"""
计算器
"""
"""
传统实现方法
"""
def jia(x, y):
    return x + y
    
def jian(x, y):
    return x - y
    
def cheng(x, y):
    return x * y
    
def chu(x, y):
    return x / y
    
def operator1(x, o, y):
    if o == "+":
        return jia(x, y)
    elif o == "-":
        return jian(x, y)
    elif o == "*":
        return cheng(x, y)
    elif o == "/":
        return chu(x, y)
    else:
        pass
        
print(operator1(2, "+", 4))
print(operator1(2, "-", 4))
print(operator1(2, "*", 4))
print(operator1(2, "/", 4))

"""
进阶实现方法
使用lambda和字典
"""
jia = lambda x, y : x + y

jian = lambda x, y : x - y

cheng = lambda x, y : x * y

chu = lambda x, y : x / y

opr = {"+" : jia, "-" : jian, "*" : cheng, "/" : chu}

print(opr["+"](2, 3))
print(opr.get("-")(2, 3))

def operator2(x, o, y):
    #return opr[o](x, y)
    return opr.get(o)(x, y)
    
print(operator2(2, "+", 4))
print(operator2(2, "-", 4))
print(operator2(2, "*", 4))
print(operator2(2, "/", 4))  
      
input("Press <enter>")