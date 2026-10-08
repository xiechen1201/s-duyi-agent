# 关键字参数与字典操作综合
# 阅读以下代码，预测每行 print 的输出结果，并在注释中写出你的答案。

def merge_data(base, **extra):
    result = base.copy() # 浅拷贝
    for key, value in extra.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result

data = {"a": 10, "b": [1, 2]}
merged = merge_data(data, a=5, b=[3], c="hello")
print(merged)

print(len(merged))
print(merged.get("d", "not found"))

""" 

{
  a: 15,
  b: [1, 2, 3]
  c: "hello"
}

3

"not found"

 """