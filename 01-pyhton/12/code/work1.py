import time


def timer(func):
    def inner_func(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        res = time.time() - start
        print(f"{func.__name__} 执行事件 {res} 秒")

    return inner_func


@timer
def slow_function():
    time.sleep(1)
    return "Done"


slow_function()
# 输出：slow_function 执行时间: 1.0012 秒
