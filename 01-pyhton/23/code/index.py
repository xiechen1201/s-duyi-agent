import asyncio

loop = asyncio.new_event_loop()

asyncio.set_event_loop(loop)

current_loop = asyncio.get_event_loop()

print("当前事件循环", current_loop)

def test_run():
  print("测试运行")
  loop.stop()

loop.call_soon(test_run)

loop.run_forever()