def generator():
    print("准备 yield 1")
    yield 1
    print("准备 yield 2")
    yield 2
    print("准备 yield 3")
    yield 3
    print("生成器结束")


g = generator()
print("生成器已创建")
print(next(g))
print("---")
print(next(g))
print("---")
g.close()
print("生成器已关闭")
print(next(g))

# 生成器已创建
# 准备 yield 1
# 1
# ---
# 准备 yield 2
# 2
# ---
# 生成器已关闭
# Error