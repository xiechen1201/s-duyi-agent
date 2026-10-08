x = 10

def demo():
    print(x)      # 先读
    x = 20        # 再写 → 编译期就判定 x 是局部变量！

demo()  # UnboundLocalError