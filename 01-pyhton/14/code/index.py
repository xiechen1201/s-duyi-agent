import math


class MyProperty:

    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        if instance is None:
            return self

        if self.fget is None:
            raise AttributeError("属性不可读取")

        return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("属性不可修改")

        return self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("属性不可删除")

        return self.fdel(instance)

    # 新增：setter 装饰器
    def setter(self, func):
        return type(self)(self.fget, func, self.fdel)

    # 新增：deleter 装饰器
    def deleter(self, func):
        return type(self)(self.fget, self.fset, func)



class Circle:
    def __init__(self, radius):
        self._radius = radius

    @MyProperty
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("半径不能为负数")
        self._radius = value

    @radius.deleter
    def radius(self):
        print("删除半径")
        del self._radius

    @MyProperty
    def area(self):
        return math.pi * self._radius**2

    @MyProperty
    def diameter(self):
        return self._radius * 2
