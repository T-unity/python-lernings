# coding: UTF-8

def high_func(get_data, pass_func):
  for key, value in enumerate(get_data):
    pass_func(value, key)

result = 0
def add_func(value, key):
  global result
  result += value

origin = [98, 21,72, 55, 102]

high_func(origin, add_func)
print(result)


def hello_dolly(data, some_func):
  for key, value in enumerate(data):
    some_func(key, value)

def print_func(key, value):
  print(key, value)

original = ['hello','goodbye','see you','morning','hi','yep',]

hello_dolly(original, print_func)
