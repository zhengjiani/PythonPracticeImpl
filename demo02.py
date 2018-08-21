# -*- coding: utf-8 -*-
#利用闭包返回一个计数器函数，每次调用它返回递增整数
# def createCounter():
#     def f():
#         n=0
#         while True:
#             n=n+1
#             yield n
#     fs=f()
#     def counter():
#         return next(fs)
#     return counter
# # 测试:
# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')
#使用匿名函数改造代码
# def is_odd(n):
#     return n % 2 == 1
#
# L = list(filter(is_odd, range(1, 20)))
#print(L)
# L=list(filter(lambda n:n%2==1,range(1,20)))
# print(L)
#请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
# import time,functools
# def metric(fn):
#     @functools.wraps(fn)
#     def wrapper(*args,**kw):
#         print('%s executed in %s ms' % (fn.__name__,10.24))
#         return fn(*args,**kw)
#     return wrapper
#
#
# # 测试
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y;
#
# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z;
#
# f =fast(11, 22)
# print(f)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')
#请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志
import functools
# def log(f):
#      def wrapper(*args, **kw):
#           print('begin call:%s' % f.__name__)
#           func= f(*args, **kw)
#           print('end call:%s' % f.__name__)
#           return func
#      return wrapper
# #测试
# @log
# def fast(x, y):
#     print(x + y)
# f=fast(11,22)
#再思考一下能否写出一个@log的decorator，使它既支持：
# @log
# def f():
#     pass
# 又支持：
# @log('execute')
# def f():
#     pass
#请把下面的Student对象的gender字段对外隐藏起来，
# 用get_gender()和set_gender()代替，并检查参数有效性
# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.__gender=gender
#         def get_gender(self):
#             return self.__gender
#         def set_gender(self,gender):
#             if gender=='male'or gender=='female':
#                 self.__gender=gender
#             else:
#                 raise TypeError('输入性别错误')
#有错误：AttributeError: 'Student' object has no attribute 'get_gender'
# # 测试:
# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')
#为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加
# class Student(object):
#     count = 0
#     def __init__(self, name):
#         self.name = name
#         Student.count +=1
# # 测试:
# if Student.count != 0:
#     print('测试失败!')
# else:
#     bart = Student('Bart')
#     if Student.count != 1:
#         print('测试失败!')
#     else:
#         lisa = Student('Bart')
#         if Student.count != 2:
#             print('测试失败!')
#         else:
#             print('Students:', Student.count)
#             print('测试通过!')
#请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
# class Screen(object):
#     @property
#     def width(self):
#         return self._width
#     @width.setter
#     def width(self,value):
#         self._width=value
#     @property
#     def height(self):
#         return self._height
#
#     @height.setter
#     def height(self, value):
#         self._height = value
#     @property
#     def resolution(self):
#         return self._width*self._height
# # 测试:
# s = Screen()
# s.width = 1024
# s.height = 768
# print('resolution =', s.resolution)
# if s.resolution == 786432:
#     print('测试通过!')
# else:
#     print('测试失败!')
#把Student的gender属性改造为枚举类型，可以避免使用字符串
# from enum import Enum,unique
# @unique
# class Gender(Enum):
#     Male=0
#     Female=1
# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#
# # 测试:
# bart = Student('Bart', Gender.Male)
# if bart.gender == Gender.Male:
#     print('测试通过!')
# else:
#     print('测试失败!')
#异常处理
# try:
#     print('try...')
#     r=10/0
#     print('result:',r)
# except ZeroDivisionError as e:
#     print('except:',e)
# finally:
#     print('finally...')
# print('END')
#运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复
# from functools import reduce
#
# def str2num(s):
#     return float(s)#这里原来是int
#
# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     return reduce(lambda acc, x: acc + x, ns)
#
# def main():
#     r = calc('100 + 200 + 345')
#     print('100 + 200 + 345 =', r)
#     r = calc('99 + 88 + 7.6')
#     print('99 + 88 + 7.6 =', r)
#
# main()
# import unittest
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def get_grade(self):
#        if  60<=self.score<80 :
#             return 'B'
#        if  self.score >= 80:
#             return 'A'
#        if  0<=self.score<60:
#             return 'C'
#        else:
#             raise ValueError
#
#
# class TestStudent(unittest.TestCase):
#     def test_80_to_100(self):
#         s1 = Student('Bart', 80)
#         s2 = Student('Lisa', 100)
#         self.assertEqual(s1.get_grade(), 'A')
#         self.assertEqual(s2.get_grade(), 'A')
#
#     def test_60_to_80(self):
#         s1 = Student('Bart', 60)
#         s2 = Student('Lisa', 79)
#         self.assertEqual(s1.get_grade(), 'B')
#         self.assertEqual(s2.get_grade(), 'B')
#
#     def test_0_to_60(self):
#         s1 = Student('Bart', 0)
#         s2 = Student('Lisa', 59)
#         self.assertEqual(s1.get_grade(), 'C')
#         self.assertEqual(s2.get_grade(), 'C')
#
#     def test_invalid(self):
#         s1 = Student('Bart', -1)
#         s2 = Student('Lisa', 101)
#         with self.assertRaises(ValueError):
#             s1.get_grade()
#         with self.assertRaises(ValueError):
#             s2.get_grade()
#
# if __name__ == '__main__':
#     unittest.main()
#请将本地一个文本文件读为一个str并打印出来
# fpath=r'C:\Windows\system.ini'
# with open(fpath,'r') as f:
#     s=f.read()
#     print(s)
#写入str
# from io import StringIO, BytesIO
#
# f=StringIO()
# f.write('hello')
# f.write(' ')
# f.write('world')
# print(f.getvalue())
# #读取str
# f=StringIO('Hello!\nHi\nGoodbye!')
# while True:
#     s=f.readline()
#     if s=='':
#         break
#     print(s.strip())
# #BytesIO()
# f=BytesIO()
# f.write('中文'.encode('utf-8'))
# print(f.getvalue())
# #os模块功能
# import os
# os.name#操作系统类型
# os.uname()#操作系统详细信息
# #获取某个环境变量的值
# os.environ.get('PATH')
# #查看当前目录的绝对路径
# os.path.abspath('.')
# #在某个目录下创建一个新的目录，首先把新目录的完整路径表示出来
# os.path.join('/Users/michael','testdir')
# #然后创建一个目录
# os.mkdir('/Users/michael/testdir')
# #删掉一个目录
# os.mkdir('Users/michael/testdir')
# #合成目录
# os.path.join()
# #拆分目录
# os.path.spilt('/Users/michael/testdir/file.txt')
# ('/Users/michael/testdir', 'file.txt')
#利用os模块编写一个能实现dir -l输出的程序。
# import os
# import time
# import re#正则表达式模块
# dirpath=r''
#
#
# def numOfFiles(path,num=1):
#     try:
#         for x in os.listdir(path):
#             dir=os.path.join(path.x)
#             if os.path.isdir(dir):
#                 num +=1
#                 num=numOfFiles(dir,num)
#     except BaseException as e:
#         pass
#     finally:
#         return num
#
#
#
# def listFile(path):
#     print('权限\t文件数\t用户名\t群组名\t大小\t月份\t日期\t时间\t文件名')
#     for x in os.listdir(path):
#         dir=os.path.join(path,x)
#         st=os.stat(dir)
#         print(oct(st.st_mode)[-3:],end='\t')
#         print(numOfFiles(dir),end='\t')
#         print(st.st_uid,end='\t')
#         print(st.st_gid,end='\t')
#         print(st.st_size,end='\t')
#         lc_time=time.localtime(st.st_mtime)
#         print(time.strftime('%b',lc_time),end='\t')
#         print(lc_time.tm_mday,end='\t')
#         print(time.strftime('%H:%M',lc_time),end='\t')
#         print(x)
#
#         listFile(dirpath)
# #编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
# import os
# keyword=input('Input keyword:')
# up='.'
# result=[]
# def check(up,keyword):
#     all=os.listdir(up)
#     for x in all:
#         try:
#             abs_x=os.path.join(up,x)
#             if os.path.isdir(abs_x):
#                 up=os.path.join(up,x)
#                 check(up,keyword)
#                 up=os.path.split(up)[0]
#             if os.path.isfile(abs_x):
#                 if keyword in x:
#                     result.append(abs_x)
#         except:
#             continue
# check(up,keyword)
# print('\n===========Find %d files==========\n' % len(result))
# num=0
# for r in result:
#     num += 1
#     print('%d %s'%(num,r))
# os.system("pause")
#python对象转换为JSON
import json
d=dict(name='Bob',age=20,score=88)
json.dumps(d)
#json的字符串反序列化
json_str='{"age":20,"score":88,"name":Bob}'
json.loads(json_str)





