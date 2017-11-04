#!/usr/bin/env python
#coding:utf8

"""
python中常见内置函数
1、返回绝对值          abs()
2、返回最大值          max()
3、返回最小值          min()
4、获取长度            len()
5、求两个数的商和模    divmod
6、求指数              pow
7、返回对应的浮点数    round
8、判断某个函数是否可以被调用    callable
9、判断某个对象是不是某个类型    isinstance  type
10、比较两个数值       cmp
11、获取一个范围的序列           range
12、range生成器        xrange

13、类型转换函数,强制类型转换
type, int, long, float, complex
"""

"""
序列处理函数
filter():过滤函数
zip():列表合并
map():并行遍历
reduce():
"""
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l)

def fun1(x):
    if x % 2 == 0:
        return True

print(*filter(fun1, l))

name = ["mil0", "zou", "tom"]
age = [20, 30, 40]
tel = ["133", "156", "189"]

print(*zip(name, age, tel))
print(map(name, age, tel))


input("Press <enter>")