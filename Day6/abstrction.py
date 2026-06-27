from abc import ABC

class Animal(ABC):
    def eat(ABC):
        pass
    def sleep(ABC):
        return "Iam Sleeping"
    
class Dog(Animal):
    def sleep(self):
        return "eat method in dog class"
    
c = Dog()
d = Animal()
print(d.sleep())
print(c.sleep())
