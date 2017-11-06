#!/usr/bin/env python
#coding:utf8

from functools import reduce 

"""
python 函数的学习
函数是完成特定功能的一个语句组。
1、函数：
（1）、降低编程的难度
（2）、代码重用
2、函数定义格式：
def 函数名(参数列表):  #可以没有参数
    函数体
"""
"""
代默认参数的函数
函数定义
函数调用
"""
a = 100
def fun():
    if True:
        print("Good")
    print(a)
        
#fun()

def machine(x = 1, y = "巧克力"):  #设置默认参数
    print("正在制造", x, "个", y, "口味的冰激凌！")
    
machine()
machine(5)
machine(y = "奶油")
machine(2, "草莓")

#s1 = input("输入个数：")
#s2 = input("输入口味：")
#machine(s1, s2)

"""
局部变量和全局变量
可以使用global关键字强制把变量声明为全局变量
"""
a = 100  #全局变量
def fun2():
    b = 200  #局部变量
    global c
    c = 300
    print(a)
    print(b)
    print(c)

#fun2()
#print(a)
#print(b)
#print(c)


"""
函数的返回值
使用关键字return
range获得一个连续的数据
"""
def fun3(x, y):
    return x + y

z = fun3(1, 2)
print(z)

def fun4(x, y):
    if x > y:
        return 1
    if x < y:
        return -1
    if x == y:
        return 0
        
#print(fun4(2, 2))

"""
冗余参数处理
"""
def fun5(x):
    print(x)

fun5([1, 2, 3, 4]) #传递列表
fun5((1, 2, 3, 4)) #传递元组
fun5({1:11, 2:22, 3:33}) #传递字典
fun5(range(10))

def fun6(x, y):
    print("%s : %s" % (x, y))
    
fun6(1, 2)

t = ("name", "milo")
"""
在元组或列表中的数据个数
和函数参数个数一样多的时候
可以使用*进行匹配
"""
fun6(*t) 

"""
lambda
匿名函数：
  lambda函数是一种快速定义单行的最小函数，
  是从Lisp借用来的，可以用在任何需要函数的地方。
  
lambda语句中，冒号前是参数，可以有多个，
  用逗号隔开，冒号右边是返回值。
"""
def fun7(x, y):
    return x * y

g = lambda x, y : x * y  #和上面函数是一样的功能

print(fun7(2, 3))
print(g(2, 3))  #和上面是一样的

"""
内置函数reduce，可以将函数作用与一个序列
"""
l = range(1, 6)
def fun8(x, y):
    return x * y

print(reduce(fun8, l))  #返回1*2*3*4*5
    
input("Press <enter>")