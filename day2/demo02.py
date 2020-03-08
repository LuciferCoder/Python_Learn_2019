"""
变量的类型：
    str ：   符号： 单引号、双引号、三引号、转义字符、与r结合使用
    int：    整形  3 4 6
    float：浮点型   3.1
    bool：布尔型    True    False
    bytes：字节 b'内容'

    list：   列表
    tuple：  元组
    set：    集合
    dict：   字典

"""
# 三引号能够保留格式
name = '孙杨'
name1 = '傅园慧'

messgae = """1.孙杨获得游泳冠军
2.傅园慧第一场出局
"""

print(type(name), type(name1), type(messgae))

print(name)
print(name1)
print(messgae)


'''
预定义的转义字符
\n  换行
\t  制表格
\r  
\'
\"
\\
\

结合：r''  raw：生的，原始的，未分析的；
保留字符串的原有格式
'''
s1 = r'hello \n world'

print(s1)

age = 21    # <class 'int'> 21
print(type(age), age)

f = 6123.456    # <class 'float'>
print(type(f), f)

flag = True
flag1 = False

# <class 'bool'> 值：True、False
print(type(flag), flag)
print(type(flag1), flag1)
