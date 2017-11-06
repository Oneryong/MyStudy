#!/usr/bin/env python
#coding:utf8

"""
模块（module）：
1、模块是Python组织代码的基本方式。
2、Python的脚本都是用扩展名为py的文本文件保存的，
   一个脚本可以单独运行，也可以导入另一个脚本中运行。
   当脚本被导入运行时，我们称其为模块。
3、模块名和脚本的文件名相同。
"""
"""
格式：
1、from xxx import xxx  #这样导入模块后直接使用函数，不用带模块名称了。
2、import xxx  #这样导入模块后不能直接使用函数，需要用模块名称做前缀点操作。
3、from xxx import *
4、import xxx as xxx  #给模块起个别名
"""

print(__name__)  #随着调用者不同，内置属性name值不同。

if __name__ == "__main__":  #这样可以当这个文件被当作模块用的时候不执行函数
   print(3)
   
"""
包：
Python的模块可以按目录组织为包
创建一个包的步骤：
1、建立一个名字为包名字的文件夹
2、在该文件夹下创建一个__init__.py文件(可以为空)
3、根据需要在该文件夹下存放脚本文件、已编译扩展及子包。
4、import pack.m1, pack.m2, pack.m3
"""