#!/usr/bin/env python
#-*- coding: utf-8 -*-
import calendar
import math
#python 实例练习
#数字求和
# n=int(input("请输入任意一个数字："))
# m=int(input("请再输入任意一个数字："))
# def total(n,m):
#     sum=n+m
#     print('{0} add {1} is equals:{2}'.format(n,m,sum))
#     return sum
# print(total(n,m))

'''
#输入数字排序
def sort(a,b,c):
    if a>b:
        a,b=b,a
    if a>c:
        a,c=c,a
    if b>c:
        b,c=c,b
    print('按照从小到到的顺序进行排序的结果为：{0}, {1}, {2}'.format(a,b,c))

#sort(4,0,6)
#判断输入数据是否能组成三角形
def isTrangle(a,b,c):
    flag=1
    sort(a,b,c)
    if(a+b>c and a+c>b and b+c>a):
        if(a==b==c):
            print("输入数据构成的三角形为等边三角形")
        elif(a==b or a==c or b==c):
            print("输入数据构成的三角形为等腰三角形")
        else:
            print("输入数据构成的三角形为普通三角形")
        flag=1
    else:
        #print("输入数据不能构成三角形，请重新输入数据！")
        flag=0
    return flag

#isTrangle(3,4,5)

#计算三角形的面积
def trangelArea(a,b,c):
    if(isTrangle(a,b,c)==1):
        # 计算半周长
        s = (a + b + c) / 2
        # 计算面积
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('三边边长分别为{0} {1} {2}的三角形的面积为{3:.2f}'.format(a,b,c,area))
    else:
        print("输入数据不能构成三角形，请重新输入数据！")
        a=float(input("请输入三角形第一条边长的数据："))
        b=float(input("请输入三角形第二条边长的数据："))
        c=float(input("请输入三角形第三条边长的数据："))
        trangelArea(a,b,c)


a=float(input("请输入三角形第一条边长的数据："))
b=float(input("请输入三角形第二条边长的数据："))
c=float(input("请输入三角形第三条边长的数据："))
trangelArea(a,b,c)'''

#判断是否为数字，使用到的方法为str的isdigit()方法，返回值为true or false
#判断是否为闰年leap year
# def leapYear(n):
#     if(n%4==0):
#       if(n%100==0):
#         if(n%400==0):
#           print('%d 年是闰年'%n)
#         else:
#           print('%d 年不是闰年'%n)
#       else:
#         print('%d 年不是闰年'%n)
#     else:
#       print('%d 年不是闰年'%n)

# n=int(input("请输入任意一年的年份："))
# leapYear(n)

#直接调用日历库中封装好的方法
'''
if (calendar.isleap(n)==True):
  print('%d 年是闰年'%n)
else:
  print('%d 年不是闰年'%n)

#比较一组数中的最大数值，可直接调用函数max()方法来进行；
#质数的判断：质数又称为素数，指出了能被1和它本身外，不能被其他的自然数整除；
#判断某个数是否为素数
def primeNum(n):
    flag=True
    if(n>1):
      sqrt_num=int(math.sqrt(n))
      # print('sqrt result is',sqrt_num)
      for i in range(2,sqrt_num+1):#加1的目的是因为range方法只会执行到sqrt_num减1的时候；
          # print(i)
          if(n%i==0):
            #print('%d 不是素数'%n)
            flag=False
            break
      else:
          #print('%d 是素数'%n)
          flag=True
    else:
      print("请重新输入数据，数据要大于1！")
    return flag

# primeNum(5)

#判断某个范围内的素数的个数并进行数据输出
def primeNums(n,m):
    print('%d到%d范围内的素数有：'%(n,m))
    for i in range(n,m+1):
      # print('范围内输出的数据为：',i)
      if(primeNum(i)==True):
        print(i)

primeNums(2,10)

# for i in range(2,3):
#   print(i)
#阶乘的实现，math模块中有阶乘方法factorial()，但是还是用代码来实现下。
#整数的阶乘（英语：factorial）是所有小于及等于该数的正整数的积，0的阶乘为1。即：n!=1×2×3×...×n。
def factorial(n):
    factorialnum=1
    if n<0:
        print('非正数没有阶层运算')
    elif n==0:
        print('0的阶乘为1')
    else:
        for i in range(1,n+1):
            factorialnum=factorialnum*i
        print('%d 的阶乘为：'%n,factorialnum)
        print(math.factorial(n))

factorial(5)

#九九乘法表的实现
# def mutiTable():
#     for i in range(1,10):
#         for j in range(1,i+1):
#             print('{0} * {1} = {2}'.format(i,j,i*j)),
#         print('')
# mutiTable()

#斐波那契数列的实现
def fibonacci(n):
    a,b,count=0,1,0
    while count<n:#增加count用来计数，可根据计数器来产生用户所需的数列位数
        print(a),
        a,b=b,a+b
        count+=1
fibonacci(10)'''

#实现求阿姆斯特朗数：阿姆斯特朗数指n位数等于其各位数的位数次幂之和，如:153=3**3+5**3+1**3;
'''
def isArmstrong(num):
    n=len(str(num))#求输入数据的长度，确定位数；
    temp,sum,a=num,0,0
    flag=True
    while temp>0:
        a=temp%10
        # print('a的结果为：',a)
        sum+=a**n
        temp//=10
        # print('temp的结果为：',temp)
    if sum==num:
        # print('%d 是阿姆斯特朗数！'%num)
        flag=True
    else:
        # print('%d 不是阿姆斯特朗数！'%num)
        flag=False
    return flag
# isArmstrong(153)

#输出一定范围内的阿姆斯特朗数
def armstrongNums(n,m):
    count=0
    for i in range(n,m+1):
        if(isArmstrong(i)):
            count+=1
            print(i),
            # print('{0} 到 {1}范围内的阿姆斯特朗数有{2}位，分别是{3}：'.format(n,m,count,i)),

armstrongNums(1,1000)

#使用匿名函数的方法，非常简洁,而且不需要去对数据进行取余取整操作;
#但是需要注意的是其中使用了，eval函数，map函数；
#eval()函数的意义：eval() 函数用来执行一个字符串表达式，并返回表达式的值
#eval()函数中的值若是字符型的数字，则使用该函数，可将x当做纯数字来进行运算；如果不使用该函数，那程序将会报错，TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
#Python 2.x 返回列表。
#Python 3.x 返回迭代器。
def is_armstrong(n):
    s = sum(map(lambda x: eval(x)**len(str(n)), str(n)))
    return s == n

B = []
for i in range(1000):
    if is_armstrong(i):
        B.append(i)

print(B)'''

#计算两个数的最大公约数Greatest Common Divisor；
#最大公约数：多个数的公约数中最大的一个数；
# def f1(a,b):
#     while b!=0:
#         a,b=b,a%b
#         print(a,b)
#     print(a)
# f1(12,16)

# print(12%16)
#最小公倍数：两个或多个整数公有的倍数叫做它们的公倍数，其中除0以外最小的一个公倍数就叫做这几个整数的最小公倍数；
#在最大公约数的基础上，可以使用两数的乘积除以最大公约数，即可求得最小公倍数。
'''
people=list(range(1,31))
print(people)
while len(people)>15:
    i=1
    while i<9:
        people.append(people.pop(0))
        i+=1
    print('{:2d}号下船了'.format(people.pop(0)))'''

#约瑟夫生死小游戏：船上有30人，但是只有15人能继续待在船上，从第一位开始，数到9之后，该序号的人需要下船，然后又继续从1开始循#环，以此类推，直到船上只剩15人为止；
# def Josef():
#     people=list(range(1,31))
#     i=1
#     while len(people)>15:
#         for j in people:
#             if i==9:
#                 print('number {} off the boat'.format(j))
#                 people.remove(j)
#                 # print(people)
#                 i=1
#             else:
#                 i=i+1
#     print(id(people)
#     print(id(people[:]))
#     return people
# print(Josef())


# people=list(range(1,31))
# for i,j in enumerate(people):
#     print(i,j)
# for i,j in enumerate(people[:]):
#     print(i,j)

def yuesefu(nums,step,stay):
    #nums:总人数  step:步长   stay:剩余的人数
    lists = list( range(1,nums+1) )
    #check = 0
    while len(lists) > stay:
        i = 1
        while i<step:
            lists.append(lists.pop(0))#将需要下船的编号始终固定在第一位，lists.pop(0)做铺垫。
            # print(lists)
            i+=1
            #print(i)
        print("{:2d}号要下船了".format(lists.pop(0)))
stays = yuesefu(30,9,15)
