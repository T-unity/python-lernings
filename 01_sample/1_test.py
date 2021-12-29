# coding: UTF-8
TAX_RATE = 1.1

def get_max_min(*args):
  return max(args), min(args)

max_val, min_val = get_max_min(100,231,0.5, -500, 114514)

print(max_val)
print(min_val)
