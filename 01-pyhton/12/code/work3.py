def repeat(n):
    def decorate(func):
        def inner_func(*agrs, **kwargs):
            nonlocal n
            while n != 0:
                func(*agrs, **kwargs)
                n -= 1

        return inner_func

    return decorate


@repeat(3)
def say_hello(s):
    print(s)


say_hello(1)  # 输出: 1 1 1
