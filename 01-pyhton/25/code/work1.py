import asyncio
from async_delay import async_delay
from typing import Coroutine


def gather(*aws: Coroutine) -> asyncio.Future:

    future = asyncio.Future()
    count = len(aws)
    result = [None] * count
    finished_count = 0

    def on_done(task):
        pass;

    for el in aws:
        asyncio.create_task(el).add_done_callback(on_done)

    return future


async def coro(name: str, duration: int):
    await async_delay(duration)
    return f"{name} 完成"


async def main():
    results = await gather(
        coro("A", 2),
        coro("B", 1),
        coro("C", 3),
    )
    print(results)  # 预期: ['A 完成', 'B 完成', 'C 完成']


asyncio.run(main())
