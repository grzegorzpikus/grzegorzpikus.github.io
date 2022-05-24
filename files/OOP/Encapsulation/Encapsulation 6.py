# 2. Getters and Setters with Methods

class Phone:
    def __init__(self, model, storage, megapixels):
        self._model = model
        self._storage = storage
        self._megapixels = megapixels

    def get_model(self):
        return self._model

    def set_model(self, new_model):
        self._model = new_model

    #exercise: Write getters and setters for all of the instance variables in
    # the Phone class

    def get_storage(self):
        return self._storage

    def set_storage(self, new_storage):
        self._storage = new_storage

    def get_megapixels(self):
        return self._megapixels

    def set_megapixels(self, new_megapixels):
        self._megapixels = new_megapixels

# 3. Getters with the Property Decorator

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

# 4. Setters with the Property Decorator

    @name.setter
    def name(self, new_name):
        if type(new_name) != str:
            raise TypeError("Names must be expressed as a string")
        self._name = new_name

    @age.setter
    def age(self, new_age):
        if new_age < 0:
            raise ValueError("age must be a positive number")
        self._age = new_age


class Person2:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        self._age = new_age

    name = property(get_name, set_name)
    age = property(get_age, set_age)


c2 = Person("Dalvin", 66)
print(c2.name)
print(c2.age)
c2.name = "Duna"
c2.age = 99
print(c2.name)
print(c2.age)




c = Person("Calvin", "6")
print(c.name)
print(c.age)
c.age = 17
c.name = "False"
print(c.name)
print(c.age)



my_phone = Phone("iPhone", 256, 12)
print(my_phone.get_model())
my_phone.set_model("Galaxy S20")
print(my_phone.get_model())