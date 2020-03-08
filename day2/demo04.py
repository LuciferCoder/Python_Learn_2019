"""
运算符：
    1、算数运算符
        + - * / % ** //
        数值型： + 进行的是相加运算
        字符串类型： + 表示的是 fr连接符

        数值型：* 表示算数相乘
        字符串： * 表示字符串遍数

        除数为0的时候，会报错误:
            ZeroDivisionError: division by zero
    2、复制运算符
        +=  -=   *= /=  %=
"""

a = 10
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)

s1 = 'abc'
s2 = 'hello'

print(s1 + s2)

# print(10 / 0)  # ZeroDivisionError: division by zero

result = a + b  # 赋值
print(result)

c = 100
d = 5
print(id(b), id(d))  # id()   内置函数：id（变量名） 获取变量地址，返回的是一个整型值

e = 0
e += 6  # e = e + 6 先相加，后赋值，
print(e)
