# задание№1
class Name:
 def __init__(self,name,age):
     self.name = name
     self.age = age

@classmethod
def name(self):
 return self.name - self.profeshion

name1 = Name("саша",12)
print(vars(name1))
# задание№2
class Animal:

    def __init__(self,name,):
        self.name = name
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        return"ффавфф"

class Cat(Animal):
    def make_sound(self):
        return"мяуууу"

class Cow(Animal):
    def make_sound(self):
        return"мууууу"
animals = [Dog("лисичка"),Cat("пушистик"),Cow("мурка")]

for Animal in animals:
    print(Animal.name + ":" + Animal.make_sound())