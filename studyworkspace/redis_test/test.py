import time
from functools import reduce


PRECISION = {1, 5, 60, 300, 3600, 18000, 86400}


now = time.time()

'''

for prec in PRECISION:
    pnow  = int(now / prec) * prec
    print(pnow)



result = 5 and 4 or 1
print('5 and 4 or 1:::::::' + str(result))


result = 11 // 10

print(result)


def yeild_func(num, num2):
    start = 0
    start += 2
    yield  start



for i in yeild_func(10, 1000):
    print('yeild:' + str(i))


def genter():
    a = 'aaaa'
    b = 'bbbb'
    c = 'cccc'
    for i in range(2):
        yield a
        #print('hhh'+str(i))
        yield b
        #print("aaa" + str(i))
        yield c

# 包含了yield 的 genter() 就是一个生成器
res = genter()
for a, b in enumerate(res):
    print("a:%s"%a)
    print('b:%s'%b)



a = int('063', 10)
print(a)


myname  = str.strip(' ') or 'lee'
print(myname)


none = ''  or None
print(none)

isnone = none != None
print(isnone)


ALL = 'hello'
print(ALL)
ALL =  ALL, ' World'
print(ALL)

tu1 = '1 ', '2 '
tu2= tu1, '3 '
print(tu2)
tu1.__add__(tu1)


dic = {'keys': 'values'}

print(dic['keys'])
#print(dic['key'])
#error because key  'key' does not exits

dic[('lee')] = 'cheng'
# dic key must be invariable   tuple is so it can be dic's key
print(dic[('lee')])

print(dic.get("key"))
print(dic.get("key", 'return Default value when key does not exits'))

if 'keys' in dic:
    print("in~~")


s = '123456789'
s1 = s[::2]
print(s1)



# if not isinstance(x, (int, float))
#  一次性判断多个类型

def multiresult():
    return  'a', 'b'

x,y  = multiresult()
print('x=%s, y=%s'%(x,y))


myinfo = {'name': 'lee', 'age' : '19', 'gender': 'male'}
for k,v in myinfo.items():
    print("key:%s, value:%s"%(k, v))
for key in myinfo.keys():
    print("key:%s, value:%s"%(key, myinfo[key]))
myinfo.update({'name': 'cheng'})
for key in myinfo.keys():
    print("key:%s, value:%s"%(key, myinfo[key]))
    


# isinstance('ABC', Iterable)  是否可迭代

L = [m+n for m in "ABC" for n in "abc"]
print(L)

li = ['a', 'b', 'c']
for a, b in enumerate(li):
    print(a, b)



#l = [(x, y) for x, y in range(1, 100) if x %3 ==0]
#print(l)

'''
def Test01():
    print("执行----------A")
    yield ('A')
    print("执行----------B")
    yield ('B')
    print("执行----------C")
    yield ('C')


# Test01() 既然直接调用没有任何卵用，这行注释
# 既然我们知道这个函数是generator性质的,我们用一个变量存下这个对象
'''
g =  Test01()
v1 = next(g)
v2 = next(g)
v3 = next(g)
print(v1)
print(v2)
print(v3)

G = Test01()
print("*"*100)
for i in Test01():
    print(i)
print("*"*100)

L = list(G)  # 这里，会把Test01函数里没有输出的三个print打印出来，而将'A','B','C'保存到列表中
print('-'*100)
for n in L:
    print(n)

for n in L:
    print(n)


#for n in L:
#    print(n)  # 你



def flib_2(max):
    n, a, b = 1, 0, 1
    while n <= max:
        print(b)
        a, b = b, a + b;  # 我们也可以这样写，简单粗暴（我会时不时的重复这四个字，哈哈）
        n = n + 1
    return 'done'  # 这里，我们结束斐波拉契数列的计算


G = flib_2(9)


def triangles():
    N = [1]
    while True:
        yield N
        N.append(0)
        N = [N[i] + N[i + 1] for i in range(len(N))]



def a():
    for i in range(10):
        yield i

li = a()

while True:
    print(next(li))
'''

#li =  list(range(10))
#print(li[-1])
'''
def addself(x, y):
    return x + y

li = reduce(addself, [1, 2, 3])
print(li)



a =  0 and 2
b  = 1 or 5
c  = 'c' or ''
c1 = None or ''
d = '' and None

print(a)
print(b)
print(c)
print(c1)
print(d)
'''

li = iter(filter(lambda  x: x%2 != 0, range(1 , 11)))

print(next(li))




