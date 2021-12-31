class Person:
  __slots__ = ['firstname', 'lastname', 'age']
  def __init__(self, firstname='some', lastname='one'):
    # firstname = self.firstname
    self.firstname = firstname
    self.lastname = lastname

  def show_own(self):
    print(f'私の名前は{self.firstname}{self.lastname}です。')


if __name__ == '__main__':

  taro = Person('山田', '太郎')

  taro.show_own()
