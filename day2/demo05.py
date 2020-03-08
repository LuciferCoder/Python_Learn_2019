"""
关系运算符：
    == != > < >= <=
    左边  运算符 右边  --> bool True   False
    == ： 比较的是内容， 返回值是True| False
    is：比较的是地址，  可以通过id（变量）获取地址

逻辑运算符：

"""
a1 = 9
a2 = 9

print(a1 < a2)
print(a1 > a2)
print(a1 == a2)  # 恒等于的判断 True
print(a1 != a2)  # False

b1 = 10000
b2 = 10000

print(b1 == b2)  # 比较的是内容
print(b1 is b2)  # 比较的是地址   在交互式中，这个语句是False，因为交互式窗口是逐行编译结束，所以不相等；而在py文件中，是逐行加载，前者被后者复用，所以相等；
print(id(b1), id(b2))

'''
是False的情况有哪些？
    0   ''  None
'''

print(not 3 + 5)

print(5 + False)  # 5  False参与算数运算的时候就变成了0
print(5 + True)  # 6 True参与算数运算的时候就便车给了

print(5 > True)  # True True与算数进行比较运算时，True表示的数字为1

# and or

'''
and: 与 两边同时为真时结果才为真
    T and T = T
    T and F = F
    F and T = F
    F and F = F
    
    验证用户成功：用户名True and passwd True --> 登陆成功
    
or: 或 已有一边为True 或者两边都是是True
        T and T = T
        T and F = T
        F and T = T     
        F and F = F
    验证登录：（用户名and密码） or (手机号and验证码) -->  登陆成功
            
'''

number = input('请输入一个整型数字：')
print(type(number), number)

# 类型转化吧：str-->int
number = int(number)
# print(8 > 5 and 5 != number)
print(8 > 5 and 5 == number)  # print(8 > 5 and 5 == number)
