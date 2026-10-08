# 阅读以下代码，预测每行 print 的输出结果，并在注释中写出你的答案。

def add_items(base, items=None, *tags):
    if items is None:
        items = []
    items.append(base)
    for tag in tags:
        items.append(tag)
    return items

result1 = add_items(10)
print(result1)

result2 = add_items(20, [1, 2], 30, 40)
print(result2)

print(result1)

""" 
[10]
[1, 2, 20, 30, 40]
[10]
 """