# 作业一：代码输出结果预测

# 变量定义
a = 10
b = 3.5
c = "Python"
d = True
e = None

# 1. 数据类型与 type 函数
print(type(a)) 
# int
print(type(b))
# float
print(type(c))
# str
print(type(d))
# bool
print(type(e))
# None
print(type(a) == int)
# True

# 2. 变量类型转换
print(int(b))
# 3
print(float(a))
# 10.0
print(str(a) + c)
# 10Python
print(bool(0))
# False
print(bool(""))
# False
print(bool("hello"))
# True

# 3. 算术运算符
print(a + 5)
print(a / 4)
print(a // 4)
print(a % 4)
print(a ** 2)
print(c * 2)

# 4. 字符串格式化（f-string）
name = "Alice"
age = 25
print(f"姓名: {name}, 年龄: {age}")
# 姓名: Alice, 年龄: 25
print(f"明年{age + 1}岁")
# 明年 26 岁
print(f"{a} + {5} = {a + 5}")
# 10 + 5 = 15

# 5. 比较运算符与链式比较
print(a > 5)
print(a == 10)
print(5 < a < 20)
print(c == "python")
print("A" < "a")

# 6. 逻辑运算符
print("6. 逻辑运算符")
print(True and False)
# False
print(True or False)
# True
print(not d)
# False
print(0 and 5)
# 0
print(3 or 5)
# 3
print("" and "hello")
# ""
print("hi" or "hello")
"hi"
print(not None)
# True

# 7. 三元运算符
print("7. 三元运算符")
score = 85
result = "及格" if score >= 60 else "不及格"
print(result)
# 及格
level = "A" if score >= 90 else ("B" if score >= 80 else "C")
print(level)
# B

# 8. 赋值运算符
x = 10
x += 5
print(x)
# 15
x -= 3
print(x)
# 12
x *= 2
print(x)
# 24
x /= 4
print(x)
# 6.0

s = "Hi"
s += " Python"
print(s)
# Hi Python
s *= 2
print(s)
# Hi Python Hi Python