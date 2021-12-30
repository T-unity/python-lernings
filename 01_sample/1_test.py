# coding: UTF-8

def log_func(some):
  def inner(*args, **kwargs):
    print('デコレーターを利用した高階関数')
    print('------------------')
    print(f'Name: {some.__name__}')
    print(f'Args: {args}')
    print(f'keywords: {kwargs}')
    print('------------------')
    return some(*args, **kwargs)
  return inner

@log_func
def setter_func(x, y, m='bar', n='piyo'):
  print(f'setter: {x}-{y}/{m}-{n}')

setter_func(2021,12, m='hello', n='world')

# log_setter = log_func(setter_func)
# log_setter(2021,12, m='hello', n='world')
