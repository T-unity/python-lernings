# coding: UTF-8
TAX_RATE = 1.1

def total_price(init, *values):
  res = init
  for value in values:
    res += value

  return res

print(total_price(1000, 1000, 1000))
