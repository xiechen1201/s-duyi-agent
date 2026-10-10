"""编写一个 Counter 类：

初始化时指定起始值
每次调用实例，计数器值加 1
支持 reset() 方法重置为初始值
支持 get() 方法获取当前值"""


class Counter:

    count = 1

    def __init__(self, initCount):
        self.count = initCount

    def __call__(self):
         self.count += 1
         return self.count

    def reset(self):
        self.count = 1

    def get(self):
        return self.count


c = Counter(10)
print(c())  # 11
c()  # 12
print(c.get())  # 12
c.reset()
print(c.get())  # 10
