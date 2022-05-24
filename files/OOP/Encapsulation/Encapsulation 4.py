class Dancer:

  def __init__(self, name, nationality, style):
    self._name = name
    self._nationality = nationality
    self._style = style


  def get_name(self):
    return self._name

  def set_name(self, new_name):
    self._name = new_name

  def get_nationality(self):
    return self._nationality

  def set_nationality(self, new_nationality):
    self._nationality = new_nationality

  def get_style(self):
    return self._style

  def set_style(self, new_style):
    self._style = new_style

  name = property(get_name, set_name)
  nationality = property(get_nationality, set_nationality)
  style = property(get_style, set_style)

my_dancer = Dancer("Savion Glover", "American", "tap")

print(my_dancer.name)
print(my_dancer.nationality)
print(my_dancer.style)
my_dancer.name = 'Anna Pavlova'
my_dancer.nationality = 'Russian'
my_dancer.style = 'ballet'
print(my_dancer.name)
print(my_dancer.nationality)
print(my_dancer.style)