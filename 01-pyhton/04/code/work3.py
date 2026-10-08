# 多返回值与容器遍历综合
# 阅读以下代码，预测每行 print 的输出结果，并在注释中写出你的答案。

def split_data(data):
    mid = len(data) // 2
    return data[:mid], data[mid:]

nums = [1, 2, 3, 4, 5, 6]
first, second = split_data(nums)
print(first, second)

def find_indices(items, target):
    indices = []
    for i, item in enumerate(items):
        if item == target:
            indices.append(i)
    return indices

scores = [85, 92, 85, 78, 85]
positions = find_indices(scores, 85)
print(positions)

result = second + [len(positions)]
print(result)

""" 
[1, 2, 3] [4, 5, 6]
[0, 2, 4]
[4, 5, 6, 3]
 """