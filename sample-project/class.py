class Animal:
    def __init__(self, name, species):
        self.name = name  
        self.species = species  

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."

class Dog(Animal):        
    tricks = [] 
    def __init__(self, name, breed):
        super().__init__(name, 'Dog')
        self.breed = breed
        self.sound = 'Woof'
    
    def add_trick(self, trick):
        self.tricks.append(trick)
    def speak(self):
        return f"{self.name} says {self.sound}!"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, 'Cat')
        self.color = color
        self.sound = 'Meow'
    
    def speak(self):
        return f"{self.name} says {self.sound}!"

dog1 = Dog('Blacky', 'Lab')
dog1.add_trick('roll over')
dog2 = Dog('Samy', 'Husky')
dog2.add_trick('sit')

cat1 = Cat("Whiskers", "Black")

print(dog1.eat(), dog1.tricks, dog1.speak(),dog1.sleep())
print(dog2.eat(), dog2.tricks, dog2.speak(),dog2.sleep())

print(cat1.eat(), cat1.speak(), cat1.sleep())

