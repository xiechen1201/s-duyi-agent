class MyMeta(type):
    def __new__(mcs, name, bases, namespace):
        print(f"正在创建类: {name}")
        print(f"父类: {bases}")
        print(f"属性: {list(namespace.keys())}")

        # 必须调用 type.__new__ 来真正创建类
        cls = super().__new__(mcs, name, bases, namespace)
        return cls


# 使用 metaclass 参数指定元类
class Dog(metaclass=MyMeta):
    species = "Canis familiaris"

    def bark(self):
        print("Woof!")

""" 
正在创建类: Dog
父类: ()
属性: ['__module__', '__qualname__', 'species', 'bark']
 """