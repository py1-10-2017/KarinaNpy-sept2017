class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print "Animal's health: ", self.health

animal1 = Animal("Gato", 230)

animal1.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self, name, health = 150):
        super(Dog, self).__init__(name, health)

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name, health = 170):
        super(Dragon, self).__init__(name, health)

    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        print "I am a Dragon"
        super(Dragon, self).displayHealth()

dog1 = Dog("Bobik")
dragon1 = Dragon("Inferno")

dragon1.displayHealth()

# animal1.pet() - AttributeError: 'Animal' object has no attribute 'pet'
# animal1.fly() - AttributeError: 'Animal' object has no attribute 'fly'
animal1.displayHealth()
# dog1.fly() # - AttributeError: 'Dog' object has no attribute 'fly'
