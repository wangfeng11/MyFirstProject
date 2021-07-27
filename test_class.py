#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
# 类
# class Person:
#     # 类的实例属性
#     name = "tom"
#
#     # 类的方法
#     def get_name(self):
#         return self.name
#
#
# print(Person.name)
# p = Person()
# print(p.name)
# print(p.get_name())
# # 修改类的属性
# Person.name = "xiaoming"
# # 修改实例属性,实例修改后，再修改类的属性，将不会受到影响
# p.name = "lili"
# print(p.name)


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 不属于类的默认变量，独特变量
    def set_att(self, unique):
        self.unique = unique

    def eat(self):
        print(f"name:{self.name}, age:{self.age},gender:{self.gender} 我在吃.")

    def drink(self):
        print(f"name:{self.name}, age:{self.age},gender:{self.gender} 我在喝.")

    def run(self):
        print(f"name:{self.name}, age:{self.age},gender:{self.gender} 我在跑.")


tom = Person("tom", 20, "male")
lili = Person("lili", 18, "female")
print(tom.age)
tom.run()
lili.set_att("beautiful")
print(lili.unique)
print(lili)
