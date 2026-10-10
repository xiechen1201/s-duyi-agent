class Descriptor:
    def __get__(self, instance, owner):
        print(f"__get__ called, instance={instance}, owner={owner}")
        return 42

    def __set__(self, instance, value):
        print(f"__set__ called, instance={instance}, value={value}")


class A:
    x = Descriptor()


a = A()
print(a.x)
a.x = 100
a.__dict__["x"] = "instance"
print(a.x)
print(a.__dict__)

# "__get__ called, instance=a, owner=A"
# 42
# "__set__ called, instance=a, value=100"