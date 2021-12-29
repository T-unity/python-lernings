# coding: UTF-8

def high_level_func(get_data, pass_value_func):
  for key, value in enumerate(get_data):
    pass_value_func(value, key)

def entity_func(value, key):
  print(key, 's value is', value, '.')

set_data = [12,55,36,74,342,554,2,432,4]

high_level_func(set_data, entity_func)
