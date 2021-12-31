class Person:
  __slots__ = ['firstname', 'lastname', 'age']
  def __init__(self, firstname='some', lastname='one'):
    # firstname = self.firstname
    self.firstname = firstname
    self.lastname = lastname


if __name__ == '__main__':

  taro = Person('山田', '太郎')
  print(taro.firstname, taro.lastname)

  taro.age = 18
  print(taro.age)

  taro.height = 178
  print(taro.height)
