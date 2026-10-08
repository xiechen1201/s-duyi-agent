# 字符串操作与循环综合

s = "hello"
print(s[1:4])
print("el" in s, "x" not in s)
print(s + " world", s * 2)

i = 0
vowels = "aeiou"
count = 0
while i < len(s):
    if s[i] in vowels:
        count += 1
    i += 1
print(count)
print(f"length: {len(s)}")

""" 

ell
True True
hello world，hellohello
2
5

 """