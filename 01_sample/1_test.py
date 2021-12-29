# coding: UTF-8
TAX_RATE = 1.1

def create_dict(**kwargs):
  res = dict()
  for key , value in kwargs.items():
    res[key] = value

  return res

d = create_dict(name='its me', age=20, gender=1, address='JP')

print(d)
