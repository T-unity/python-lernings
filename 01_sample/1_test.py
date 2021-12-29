# coding: UTF-8
TAX_RATE = 1.1

def name(prefix, suffix, *args):
  res = prefix
  res += '・'.join(args)
  return res + suffix

print(name('鈴木', '一郎', 'middle1', 'middle2'))
