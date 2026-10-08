# 作业一：列表与身份运算符综合

nums = [3, 1, 4, 1, 5]
copy = nums[:]
print(nums == copy, nums is copy)
nums[0] = 10

print(nums[0], copy[0])
print(nums == copy, nums is copy)
print(len(nums)) 

i = 0
count = 0
while i < len(nums):
    if nums[i] > 3:
        count += 1
    i += 1
print(count)

""" 

true，false
10，3
false，false
5
4

 """