"""
类型：python独有的类型，都可以当成‘容器’
list：列表
tuple：元组
set：集合
dict：字典

快速格式化：
ctrl + alt + l : 自动规范格式化
eclipse 模式快捷键： ctrl + shift + F
"""

number = 10
print_ = 10
sources = [1, 2, 3, 4, 5, 6]  # <class 'list'>  允许有重复元素
print(type(sources), sources)

source = (1, 2, 3, 4, 5, 6, 6, 6)
print(type(source), source)  # <class 'tuple'>  允许有崇拜功夫元素

sourse = {1, 3, 5, 7, 9, 1, 3, 5}  # <class 'set'> {1, 3, 5, 7, 9}  不允许有重复元素
print(type(sourse), sourse)

# <class 'dict'> {'zhangsan': 100, 'lisi': 100, 'wangwu': 100}
souces = {'zhangsan': 100, 'lisi': 100, 'wangwu': 100}  # <class 'dict'> key: value
print(type(souces), souces)

A = set('1,2,3')
print(type(A), A)


