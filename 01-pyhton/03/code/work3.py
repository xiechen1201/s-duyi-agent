# 字典与遍历综合

d = {"x": 10, "y": 20}
d["z"] = 30
d.update({"x": 15})
print(len(d))
print("x" in d, 20 in d)
print(d.get("w", 0))

keys = []
for k in d:
    keys.append(k)
print(keys)

i = 0
while i < len(keys):
    k = keys[i]
    if d[k] > 15:
        print(k)
    i += 1


""" 

3
True Flase
0

x y z

y
z

 """