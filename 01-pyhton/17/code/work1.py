from contextlib import contextmanager
import time

class timer:
    def __init__(self, str) -> None:
        self.str = str

    def __enter__(self):
        self.start = time.perf_counter()

    def __exit__(self, exc_type, exc, tb):
        elapsed = time.perf_counter() - self.start
        print(f"{self.str} 耗时: {elapsed:.4f} 秒")

# 使用
with timer("数据处理"):
    time.sleep(1)
    print("处理完成")
# 处理完成
# 数据处理 耗时: 1.0012 秒