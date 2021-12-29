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
