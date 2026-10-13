import asyncio


def async_delay(duration: int):
    # 获取事件循环
    loop = asyncio.get_event_loop()
    # 创建 Future
    future = loop.create_future()

    # n 秒后，设置 Future 的值为 None
    loop.call_later(duration, future.set_result, None)

    # 返回 Future
    return future


def async_request(host, prot, path):
    pass


# 协程函数
async def test():
    print("main begins")
    resp1 = await async_request("localhost", 5500, "/index.html")
    print("resp1", resp1[:9])
    await async_delay(1)
    print("delayed")
    resp2 = await async_request("localhost", 5500, "/index.html")
    print("resp2", resp2[:9])
    return "ok"


def main():
    coro = test()

    # 创建事件循环
    loop = asyncio.get_event_loop()
    # 创建 Future 对象
    f = loop.create_future()
    # 运行协程对象
    r = coro.send(None)

    def done_callback(fut):
        try:
            r = coro.send(fut.result())
            r.add_done_callback(done_callback)
        except StopIteration as e:
            f.set_result(e.value)

    # 给 Future 对象绑定回调函数
    r.add_done_callback(done_callback)
    return f


def run():
    # 得到 Future 对象
    fut = main()

    def done_callback(fut):
        loop.stop()
        print(fut.result())

    # 绑定回调函数
    fut.add_done_callback(done_callback)


# 创建事件循环
loop = asyncio.new_event_loop()
# 绑定到线程
asyncio.set_event_loop(loop)

# 推入任务到 ready 队列
loop.call_soon(run)
loop.run_forever()
print("over")
