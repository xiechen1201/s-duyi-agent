__all__: list[str] = ["PI", "add"]


PI: float = 3.14159


def add(a: int, b: int) -> int:
    return a + b

print(__name__)

# 以下代码只有在 python my_math.py 直接运行时才执行
# 作为模块被导入时不会执行
if __name__ == "__main__":
    print(add(3, 5))  # 8
    print(add(-1, 1))  # 0
