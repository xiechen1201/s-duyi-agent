# 编写一个元类 `SingletonMeta`，使得任何使用该元类的类都自动成为单例模式：


class SingletonMeta(type):
    _instance = {}

    def __call__(cls, *args, **kwds):
        print(cls, *args, **kwds)

        if cls not in SingletonMeta._instance:
            _ins = super().__call__(*args, **kwds)
            SingletonMeta._instance[cls] = _ins
        return SingletonMeta._instance[cls]


class Database(metaclass=SingletonMeta):
    def __init__(self, host):
        self.host = host


db1 = Database("localhost")
db2 = Database("remote")
print(db1 is db2)  # 应该输出 True
print(db1.host)  # 应该输出 localhost
