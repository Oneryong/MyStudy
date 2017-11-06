#!/usr/bin/env python

"""
一般常用的系统函数方法：
help():查看帮助信息。例如：help(list.append)
print()：打印变量的值到工作台
type()：获取变量类型
max()：获取变量中的最大值
min():获取变量中的最小值
len():求变量长度
in:判断某个值是否在某个变量之中
input()：让用户从命令行输入
id():查看具体的内存地址值
cmp():比较两个变量的值
del():删除某个值
"""

"""
一般变量的定义
python中的变量名称其实都是内存中具体数值的引用。
只是一个标签
"""
a = 10
print(type(a))
print(a)

"""
序列包括：字符串类型，元组()，列表[]
序列的操作：下标，切片
元组和列表的区别是元组内的数据内容不可以修改，列表可以
"""
"""
str字符串
"""
str = "hello world"
print(type(str))
print(str)

"""
tuple元组()
"""
a = ("zhongwanyong", 28, "man")
print(type(a))
print(a)

"""
list列表[]
append
remove
"""
b = ["zhongwanyong", 28, "man"]
print(type(b))
print(b)
b[0] = "guodandan"
b[1] = 27
b[2] = "women"
print(b)
b.append("pulan")
print(b)
b.remove("women")
print(b)
b.remove(b[1])
print(b)

"""
dict字典{}:python中唯一的映射类型,内容都是键值对。
keys():返回字典中所有键的列表
values()：返回字典中所有值的列表
items()
pop()：删除字典中的某个键值对
clear()：清空字典，不是删除
"""
dic = {"name":"zhongwanyong", "age":28, "sex":"man"}
type(dic)
print(dic)
print(dic["name"])
for k in dic.keys():
    print(k)
    print(dic[k])
	
"""添加一个键值对"""
dic["tel"] = "15121018617"
print(dic)
"""修改一个键值对"""
dic["name"] = "guodandan"
print(dic)
"""删除一个键值对"""
del(dic["tel"])
print(dic)
dic.pop("age")
print(dic)
"""清空字典，注意清空并不是删除"""
dic.clear()
print(dic)
"""删除字典"""
del(dic)

"""
流程控制
"""
"""
if else
格式：
if 条件表达式:
    执行语句
elif 条件表达式:
    执行语句
else:
    执行语句
"""
if 2 > 1:
    print("ok")
"""如果出现IndentationError错误，说明缩进有问题"""
"""
python语句块是通过缩进来控制的
python中没有“;”，是通过换行来实现一行结束的。
"""

if 1 < 2:
    print("1 < 2")
elif 2 < 3:
    print("2 < 3")
elif 3 < 4:
    print("3 < 4")
else:
    print("error")

"""
函数定义
格式：
def 函数名():
    函数体
"""
def fun():
    return 1
	
if fun():
    print("ok")
else:
    print("error")
	
"""
逻辑运算符：and,or,not
"""
if 3 > 2 and 3 < 4:
    print("ok")


"""
for循环：迭代序列(字符串，元组，列表)
格式： 
for iterating_val in sequence:
    执行语句
"""
for x in "abcd":
    print(x + " hello world")
	
"""
range(a, b, c):生成一个以a（默认为0）为起始值，以b为结束值(生成的序列中不包括b)，以c（默认为1）为步长的序列。
例如：range(10) = [0,1,2,3,4,5,6,7,8,9]
"""

"""
遍历（迭代）：
1、直接取值遍历
2、通过序列下标遍历
"""
for x in "hello":
    print(x)
	
s = "hello"
for x in range(len(s)):
    print(s[x])
	
l = [1,2,3,"a","b"]
for x in l:
    if x == 2:
	    print("find 2")
    print(x)
	
t = (7,8,9,"x","y")
for x in t:
    print(x)

"""
遍历字典
"""
d = {1:111,2:222,3:333,4:444}
for x in d:
    print(x)
"""这样获取字典的key"""
for x in d:
    print(d[x])
"""这样获取字典的value"""
print(d.items())
"""d.items()获取字典的所有键值对的元组"""
for k,v in d.items():
    print(k)
    print(v)


"""
循环控制：for
1、python的for循环可以有else，在for正常执行后会执行else，
   可以用来检测for循环是否正常执行结束。
2、可以使用break来跳出循环。
3、可以使用continue来跳过本次循环，继续执行下一次循环。
4、可以使用pass起一个占位的作用，就是代码桩。
5、可以使用exit()结束整个程序的执行。
"""
for k,v in d.items():
    print(k)
    print(v)
else:
    print("ending")

import time
for x in range(3):
    print(x)
    time.sleep(1)
else:
    print("ending")

for x in range(1,11):
    print(x)
    if x == 3:
        pass
    if x == 2:
        print("#" * 20)
        continue
    """if x == 5:
        exit()"""
    if x == 6:
        break
else:
    print("ending")

for x in range(1,11):
    print("----->")
    print(x)
else:
    print("ending")

"""
循环控制：while
1、python的while循环是满足一定条件就一直执行的，直到遇到
   break才会推出循环。
2、break一般放在一个条件语句中，每次循环都会去判断条件是否成立。
3、可以使用continue来跳过本次循环，继续执行下一次循环。
4、可以使用exit()结束整个程序的执行。
5、可以有else分支
"""
while True:
    print "hello"
	x = raw_input("please input the step: q for quit")
	if x == "q":
	    break;
	if not x:
	    break;
    if x == "c":
	    continue
	print "one more time"
else:
    print "end..."
	

	
input("Press <enter>")
