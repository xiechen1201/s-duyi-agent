# 编写一个类装饰器 `to_dict`，自动为类生成 `to_dict` 方法，该方法可以将对象转换为字典


def to_dict(cls):
    def to_dict_method(self):
        return self.__dict__

    cls.to_dict = to_dict_method
    return cls


@to_dict
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(3, 4)
print(p.to_dict())  # 应该输出: {"x":3, "y":4}
