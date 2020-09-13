# -*- coding:utf-8 -*-
"""
作业一：

区分以下类型哪些是容器序列哪些是扁平序列，哪些是可变序列哪些是不可变序列：

list
tuple
str
dict
collections.deque
作业二：
自定义一个 python 函数，实现 map() 函数的功能。

作业三：
实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
"""

'''
容器序列: list, tuple, dict, collections.deque
扁平序列: str
可变序列: list, dict, collections.deque
不可变序列: tuple, str
'''

def map(func, iterables):
    if (not hasattr(iterables, '__iter__')):
        raise(TypeError("'int' object is not iterable"))
    
    for it in iterables:
        yield func(it)


import functools
import time

def timer(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        t_start = time.time()
        ret = func(*args, **kwargs)
        print (time.time() - t_start)
        return ret

    return inner

if __name__ == '__main__':
    def square(x):
        return x**2

    # r = map(square, 5)
    r = map(square, range(5))
    print (list(r))

    new_sleep = timer(time.sleep)
    new_sleep(1)