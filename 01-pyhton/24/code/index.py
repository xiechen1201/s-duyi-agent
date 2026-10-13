import asyncio

loop = asyncio.new_event_loop()

asyncio.set_event_loop(loop)

current_loop = asyncio.get_event_loop()

# 创建 future
future = current_loop.create_future()

current_loop.run_forever()