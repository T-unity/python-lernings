# coding: UTF-8

def log_func(some):
  def inner(*args, **kwargs):
    print('デコレーターを利用しない高階関数')
    print('------------------')
    print(f'Name: {some.__name__}')
    print(f'Args: {args}')
    print(f'keywords: {kwargs}')
    print('------------------')
    return some(*args, **kwargs)
  return inner

def setter(x, y, m='bar', n='piyo'):
  print(f'setter: {x}-{y}/{m}-{n}')

log_setter = log_func(setter)
log_setter(2021,12, m='hello', n='world')
