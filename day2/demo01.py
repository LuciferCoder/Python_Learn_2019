print("hello world !")

# 单行注释
# 打印5个*
print('*****')

'''
多行注释：
    1.变量:int number; String number;
        弱类型：名 = 值   具体的类型取决于值
        判断变量的类型：    type(变量名)
        
    2.变量的额声明:   格式：变量名 = 值
                    变量的起名规则
                    A.字母、数字、下划线
                    B.不能使用数字开头 2abc是错误的  abc3是正确的
                    C.不能使用关键字:
                        'False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del',
                         'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 
                         'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
                         关键字在pycharm中显示为橘黄色
                    D.区分大小写
                    E.见名知意：尽量使用英文
                        驼峰式：showName 第一个单词全部小写，以后每个单词的首字母大写
                            类：每个单词的首字母大写
                        _命名（推荐）：show_name   print_name  borrow_book send_book
                        
    3.变量的类型:
        str ：   符号： 单引号、双引号、三引号、转义字符、与r结合使用
        int：    整形  3 4 6
        float：浮点型   3.1
        bool：布尔型    True    False
        bytes：字节 b'内容'
    
        list：   列表
        tuple：  元组
        set：    集合
        dict：   字典
        
    4.变量与操作符的使用
        算数运算符：  
        复制运算符
        关系运算符
        逻辑运算符
        位运算符
        三目运算符
'''

number = 10
print(number)
print(type(number))
number = '10'
print(number)
print(type(number))
# number = '10'
# number = '10'

# 查看关键字：
import keyword

print(keyword.kwlist)
