## Animal is-a object
class Animal(object):
    pass

## Dog is a class of an Animal, Dog is-a animal.
class Dog(Animal):
    def __init__(self, name):
        self.name = name

## Cat is a class of an Animal, Dog is-a animal.
class Cat(Animal):
    def __init__(self, name):
        self.name = name

## Person is a class of an Animal, Person is-a animal, but has-other animal: Cat, Dog.
class Person(Animal):
    def __init__(self, name):
        self.name = name
        self.pet = None

## Employee is an class of a Person, which is a class of Animal. Employee has-other animal: Cat, Dog.
class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

## Fish, Salmon, Halibut, are all independent classes.
class Fish(object):
    pass

class Salmon(object):
    pass

class Halibut(object):
    pass


rover = Dog("Rover")
satan = Cat("Satan")
mary = Person("Mary")
mary.pet = satan
frank = Employee("Frank", 10)
frank.pet = rover
flipper = Fish()
crouse = Salmon()
harry = Halibut()
