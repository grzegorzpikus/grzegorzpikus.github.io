class Country:
  def __init__(self, name, capital, population, continent):
    self.__name = name
    self.__capital = capital
    self.__population = population
    self.__continent = continent

my_country = Country('France', 'Paris', 67081000, 'Europe')

print(my_country._Country__name)
print(my_country._Country__capital)
print(my_country._Country__population)
print(my_country._Country__continent)