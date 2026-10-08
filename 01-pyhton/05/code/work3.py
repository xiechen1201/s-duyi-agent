# 以下代码用于统计函数调用次数，先读取全局计数器打印日志，再递增计数。但实际运行会报错，请修改使其正确运行：

call_count = 0

def process_data(data):
  result = sum(data)
  # 处理完成后递增计数器
  global call_count
  call_count += 1 
  return result

print(process_data([1, 2, 3]))
print(process_data([4, 5, 6]))
print(f"总共调用了 {call_count} 次")