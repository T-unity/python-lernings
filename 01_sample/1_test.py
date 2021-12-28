# coding: UTF-8

name = 'T-unity'
print(name)


base = 8
height = 10

area = base * height / 2
print({area})

def get_area(base, height):
  return base * height

area = get_area(5, 10)
print(area)

def only_return_text(content):
  content = content
  print(content)

only_return_text('めしがうまい')
