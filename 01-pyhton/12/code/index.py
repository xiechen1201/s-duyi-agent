def my_decorator(func):
   print("替换为新函数了")

@my_decorator
def say_hello():
    print("Hello!")
