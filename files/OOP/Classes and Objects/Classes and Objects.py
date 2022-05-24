class Person:
    """Represents a generic Person."""
    def __init__(self, first, last, weight, height):
        self.first_name = first
        self.last_name = last
        self.weight_in_lbs = weight
        self.height_in_inches = height

p1 = Person('Tom', 'Smith', 80, 185)
p2 = Person('Fred', 'Smith', 80, 185)
p3 = Person('George', 'Smith', 80, 185)
p4 = Person('Tanya', 'Smith', 80, 185)
p5 = Person('Mary', 'Smith', 80, 185)

list_people = [p1, p2, p3, p4, p5]

for i in list_people:
    print(i.first_name)
