# -*- coding: utf-8 -*-
#请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
import re
def is_valid_email(addr):
    if re.match(r'^(\<?)(\w*\.?\w*)@(\w*).(com)$',addr):
        return True
assert is_valid_email('someone@gmail.com')
assert not is_valid_email('mr-bob@example.com')
#版本二可以提取出带名字的Email地址
def name_of_email(addr):
    re_name=re.compile(r'^<?(((\w*\s+\w*)|\w*>))?>?(\s+)?(\w*)?@(\w*).(\w*)$')
    if re_name.match(addr):
        c=re_name.match(addr).group(1)
        return c
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
# assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
#获取当前日期和时间
from datetime import datetime
now=datetime.now()
print(now)
print(type(now))
#获取指定日期和时间
from datetime import datetime
dt=datetime(2015,4,19,12,20)
print(dt)
#把一个datetime类型转换为timestamp只需要简单调用timestamp()方法
from datetime import datetime
dt=datetime(2015,4,19,12,20)#用指定日期时间创建datetime
dt.timestamp()#把datetime转换为timestamp
t=1429417200.0
print(datetime.fromtimestamp(t))
#str转换为datetime
cday=datetime.strptime('2015-6-1 18:19:59','%Y-%m-%d %H:%M:%S')
print(cday)
#datetime转换为str
now=datetime.now()
print(now.strftime('%a,%b %d %H:%M'))
#创建一个自定义的tuple对象
from collections import namedtuple
Point=namedtuple('Point',['x','y'])
p=Point(1,2)
p.x
#namedtuple('名称'，[属性list]):
Circle=namedtuple('Circle',['x','y','r'])
#deque高效实现插入和删除操作的双向列表，适合用于队列和栈
from collections import deque
q=deque(['a','b','c'])
q.append('x')
q.appendleft('y')
q#deque(['y','a','b','c','x'])
#key不存在时返回一个默认值
from collections import defaultdict
dd=defaultdict(lambda :'N/A')
dd['key1']='abc'
dd['key2']#'N/A'
#保持Key的顺序，用OrderedDict
from collections import OrderedDict
d=dict([('a',1),('b',2),('c',3)])
d#{'a': 1, 'c': 3, 'b': 2}
od=OrderedDict([('a',1),('b',2),('c',3)])
od#key会按照插入顺序排列
#实现一个FIFO（先进先出）的dict
from collections import OrderedDict
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self,capacity):
        super(LastUpdatedOrderedDict,self).__init__()
        self._capacity=capacity
    def __setitem__(self, key, value):
        containsKey=1 if key in self else 0
        if len(self)-containsKey>=self._capacity:
            last=self.popitem(last=False)
            print('remove:',last)
        if containsKey:
            del self[key]
            print('set',(key,value))
        else:
            print('add:',(key,value))
        OrderedDict.__setitem__(self,key,value)
#统计字符出现的个数
from collections import Counter
c=Counter()
for ch in 'programming':
    c[ch]=c[ch]+1
c#Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})
#base64编解码
import base64
base64.b64encode(b'binary\x00string')
base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
#把字符+和/分别变成-和_
base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
#Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等
#请写一个能处理去掉=的base64解码函数：
def safe_base64_decode(s):
    if len(s)%4==0:
        return base64.b64decode(s)#利用递归来增加=
    d=s+b'='
    return safe_base64_decode(d)
import hashlib
md5=hashlib.md5()
#分块多次调用update()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
#根据用户输入的口令，计算出存储在数据库中的MD5口令
import hashlib
str='12345'
def calc_md5(password):
    md5=hashlib.md5()
    md5.update(password)
    print(md5.hexdigest())
print(calc_md5(str))
#根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5
#然后，根据修改后的MD5算法实现用户登录的验证
import hashlib,random
def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()
def register(username,password):
    return db[username]==get_md5(password+username+'salt_param')
class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)
db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
     }
def login(username,password):
    user=db[username]
    return user.password==get_md5(password)




