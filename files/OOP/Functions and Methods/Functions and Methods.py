class Person:
    count = 0
    """Represents a generic Person."""

    def __init__(self, first, last, weight, height):
        self.first_name = first
        self.last_name = last
        self.weight_in_lbs = weight
        self.height_in_inches = height
        Person.count = Person.count + 1

    def __str__(self):
      """Returns a string representation of the person."""
      return '{}, {}, {}, {}, {}'.format(self.first_name, self.last_name, self.weight_in_lbs, self.height_in_inches, self.calc_bmi())

    def calc_bmi(self):
        return(self.weight_in_lbs * 703) / self.height_in_inches ** 2

    def print_self(self):
        print(self)

    def cdc(self):
        bmi = self.calc_bmi()
        if bmi < 18.5:
            return '{}\'s weight falls within the underweight range'.format(self.first_name)
        elif bmi < 25:
            return '{}\'s weight falls within the healthy weight range'.format(self.first_name)
        else:
            return '{}\'s weight falls within the overweight range'.format(self.first_name)

    @classmethod
    def print_count(cls):
        return cls.count

    @classmethod
    def print_class(cls):
        return cls('','',0,0).__dict__.keys()



p = Person('Tom', 'Thumb', 150, 62)
p2 = Person('Fred', 'Flint', 225, 57)

print(p.calc_bmi())
print(p2.calc_bmi())
print(Person.count)
print(Person.print_count())
print()
print(p)
print(p2)
print()
print(p.cdc())
print(p2.cdc())

print(Person.print_class())


