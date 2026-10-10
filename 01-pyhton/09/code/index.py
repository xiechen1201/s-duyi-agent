def create_object(cls, *args, **kwargs):
    # 1. 调用 __new__ 创建实例
    obj = cls.__new__(cls, *args, **kwargs)

    # 2. 类型检查：只有 obj 是 cls 的实例（或其子类的实例）时才调用 __init__
    if isinstance(obj, cls):
        obj.__init__(*args, **kwargs)

    # 3. 返回对象
    return obj


# 测试
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayHi(self):
        print(f"my name is {self.name}, I'm {self.age} years old")


p = create_object(Person, "shae", 5)
p.sayHi()
