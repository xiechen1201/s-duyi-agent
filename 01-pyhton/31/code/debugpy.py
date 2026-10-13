# debugpy

import os
import sys

# 获取当前代码文件所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(current_dir, "demo.py")

code = open(file_path, "r").read()


def my_tracer(frame, event, arg):
    print(f"事件: {event}, 行号: {frame.f_lineno}")
    return my_tracer

# 注入跟踪，每次跟踪都会触发 my_tracer
sys.settrace(my_tracer)
# 运行代码字符串
exec(code)