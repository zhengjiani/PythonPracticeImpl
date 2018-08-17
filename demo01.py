#!/usr/bin/env python3
#-*- coding: utf-8 -*-
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
#打印Apple
print(L[0][0])
#打印Python
print(L[1][1])
#打印Lisa
print(L[2][2])
#条件判断
age=3
if age>=18:
    print('adult')
elif age>=6:
    print('teenager')
else:
    print('kid')
#str转换成整数
s=input('birth: ')
birth=int(s)
if birth<2000:
    print('00前')
else:
    print('00后')
#练习
height=1.75
weight=80.5
bmi=weight/pow(height,2)
if bmi<18.5:
    print('过轻')
elif 18.5<=bmi<25:
    print('正常')
elif 25<=bmi<28:
    print('过重')
elif 28<=bmi<32:
    print('肥胖')
elif 32<bmi:
    print('严重肥胖')
#循环
names=['Michael','Bob','Tracy']
for name in names:
    print(name)
#1到10整数之和
sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum=sum+x
print(sum)
for x in range(101):
    sum=sum+x
print(sum)
#100以内所有奇数之和
sum=0
n=99
while n>0:
    sum=sum+n
    n=n-2
print(sum)
L=['Bart','Lisa','Adam']
for name in L:
    print(name)
#dict实现
d={'Michael':95,'Bob':75,'Tracy':85}
print(d['Michael'])
d.pop('Tracy')
s=set([1,1,2,2,3,3])
s#{1,2,3}
s.add(4)
s.remove(4)
#交集和并集
s1=set([1,2,3])
s2=set([2,3,4])
s1&s2#{2,3}
s1|s2
{1,2,3,4}
d={(1,2,3)}
print(d[0])
d={(1,[2,3])}
print(d[2])
n1=255
n2=1000
print(hex(n1))
#定义函数
def my_abs(x):
    if x>=0:
        return x
    else:
        return -x
print(my_abs(-99))
#定义空函数
def nop():
    pass
#添加参数检查
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x
# 一元二次方程解法
import math
def quadratic(a,b,c):
    t=pow(b,2)-4*a*c
    if t>=0:
        x1=(-b+math.sqrt(t))/(2*a)
        x2=(-b-math.sqrt(t))/(2*a)
        return (x1,x2)
    elif t<0:
        return
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
#默认参数
def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
print(power(5))#25
#定义可变参数
def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum
print(calc(1,2))
nums=[1,2,3]
calc(*nums)
#关键字参数
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
#命名关键字参数（限制关键字参数的名字 ）
def person(name,age,*,city,job):
    print(name,age,city,job)
person('Jack',24,city='Beijing',job='Engineer')
def product(*y):
    mut=1
    for n in y:
        mut=mut*n
    return mut
# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
#阶乘
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
#尾递归优化
def fact(n):
    return fact_iter(n,1)
def fact_iter(num,product):
    if num==1:
        return product
    return fact_iter(num-1,num*product)
#汉诺塔
def move(n,a,b,c):
    if n==1:
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        print(a,'-->',c)
        move(n-1,b,a,c)
move(3,'A','B','C')
def trim(s):
    if len(s)==0:
        return s
    elif s[0]==' ':
        return (trim(s[1:]))
    elif s[-1]==' ':
        return (trim(s[:-1]))
    return s

#测试
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
#for循环中同时迭代索引和元素本身
for i,value in enumerate(['A','B','C']):
    print(i,value)
def findMinAndMax(L):
    if L==[]:
        return (None,None)
    else:
        max=L[0]
        min=L[0]
        for x in L:
            if max<x:
                max=x
            if min>x:
                min=x
        return (min,max)
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
[x*x for x in range(1,11)]
#筛选出仅偶数的平方
[x*x for x in range(1,11) if x%2==0]
#使用两层循环生成全排列
[m+n for m in 'ABC' for n in 'XYZ']
d={'x':'A','y':'B','z':'C'}
for k,v in d.items():
    print(k,'=',v)
#使用两个变量来生成list
[k+'='+v for k,v in d.items()]
#把list中所有的字符串变成小写
L=['Hello','World','IBM','Apple']
[s.lower() for s in L]
L1=['Hello','World',18,'Apple',None]
L2=[s.lower() for s in L1 if isinstance(s,str)]
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
#测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
#生成器
g=(x*x for x in range(10))
print(next(g))
for n in g:
    print(n)
#Fibonacci数列
def fib(max):
    n,a,b =0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done'
#改成生成器
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'
#杨辉三角
def triangles():
    L=[1]
    while True:
        yield L
        L.append(0)
        L=[L[i-1]+L[i] for i in range(len(L))]
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
#函数式编程
def add(x,y,f):
    return f(x)+f(y)
print(add(-5,6,abs))
#把str转换成int函数
from functools import reduce
DIGITS={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def char2num(s):
    return DIGITS[s]
def str2int(s):
    return reduce(lambda x,y:x*10+y,map(char2num,s))
def normalize(name):
    return name[0].upper()+name[1:].lower()
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
from functools import reduce
def prod(L):
    return reduce(lambda x,y:x*y,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
from functools import reduce
def str2float(s):
    s=s.split('.')
    def f1(x,y):
        return x*10+y
    def f2(x,y):
        return x/10+y
    def str2num(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    return reduce(f1,map(str2num,s[0]))+reduce(f2,list(map(str2num,s[1]))[:-1])/10
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
#求素数
def _add_iter():
    n=1
    while True:
        n=n+2
        yield n
def _not_divisible(n):
    return lambda x:x%n>0
def primes():
    yield 2
    it=_add_iter()#初始序列
    while True:
        n=next(it)#返回序列的第一个数
        yield n
        it=filter(_not_divisible(n),it)#构造新序列
#打印1000以内的素数
for n in primes():
    if n<1000:
        print(n)
    else:
        break
#回数
def is_palindrome(n):
    nn=str(n)
    return nn==nn[::-1]#反转字符串
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99,
                                                      101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
        print('测试成功!')
else:
        print('测试失败!')
#排序函数
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0].lower()
L2=sorted(L,key=by_name)
print(L2)
def by_score(t):
    return t[1]
L2 = sorted(L, key=by_score)
print(L2)

