# coding: UTF-8
TAX_RATE = 1.1

def total_price(*values):
  res = 1
  for value in values:
    res += value

  return res * TAX_RATE

print(total_price(2000, 1000, 3500, 2200))
