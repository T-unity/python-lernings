class Person:
  @classmethod
  def return_name(cls, name):
    return name

if __name__ == '__main__':
  print(Person.return_name('きよし'))

  p = Person()
  print(p.return_name('あべし'))
