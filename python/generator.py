# -*- encoding: utf-8 -*-
"""
@File    : generator.py
@Time    : 2020/4/26 10:03
@Author  : zwt
@git   : 
@Software: PyCharm
"""
import os
print(os.getcwd())


def init(func):
    def wrapper(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g)
        return g
    return wrapper


def demo_range(start, stop, step=1):
    print('start')
    while start < stop:
        yield start
        start += step
    print('end')


@init
def eat():
    print('ready to eat')
    while True:
        food = yield
        print('get the food: %s, and start to eat' % food)


def eater():
    print('ready to eat')
    food_list = []
    while True:
        food = yield food_list
        food_list.append(food)
        print(food_list)


class Foo:

    def f1(self):
        print('Foo.f1')

    def f2(self):
        print('Foo.f2')
        self.f1()


class Bar(Foo):
    def f1(self):
        print('Foo.f1')


if __name__ == '__main__':
    # a = demo_range(1, 3)
    # print(a)
    # for i in a:
    #     print(i)
    # print(next(a))
    # g = eat()
    # next(g)
    # a = g.send('hah')
    # print(a)
    # a = eater()
    # next(a)
    # a.send('hah')
    import sys
    # print(sys.modules)
    b = Bar()
    b.f2()
