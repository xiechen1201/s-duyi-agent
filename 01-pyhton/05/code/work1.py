# 阅读以下代码，预测每行 `print` 的输出结果，并在注释中写出你的答案。

x = 1

def func_a():
    x = 2
    
    def func_b():
        print(x)      # 2
    
    func_b()
    print(x)          # 2

func_a()
print(x)              # 1