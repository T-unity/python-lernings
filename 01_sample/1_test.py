class Person:
  def __init__(self, firstname, lastname):
    # firstname = self.firstname
    self.firstname = firstname
    self.lastname = lastname


if __name__ == '__main__':

  taro = Person('山田', '太郎')
  print(taro.firstname, taro.lastname)

  Joe = Person('Andy', 'Joe')
  print(f'My name Is {Joe.firstname} {Joe.lastname}')
