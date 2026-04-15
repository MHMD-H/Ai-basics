from abc import ABCMeta,abstractmethod

class animal(metaclass = ABCMeta) :
    def __init__(self,name,age,color,food):
        self.name = name
        self.age = age
        self.color = color
        self.food = food
    def print_info(self):
        print(f"this animal is {self.name}\n his.age is {self.age}\nhis color is {self.color}\n he eat {self.food}")
    @abstractmethod   
    def speak(self): #must be inheratince to each child class
        pass

class typee():
    def __init__ (self,kind):
        self.kind = kind
        
    def print_type(self,name):

        print(f"this {self.name} is : {self.kind}")
    
class dog(animal) : 
    def __init__(self,name,age,color,food):
        super().__init__(name,age,color,food)
    def speak(self): #polyphrism
        print("dog hawwwwww")
class cat(animal,typee):
    def __init__(self,name,age,color,food,kind):
        animal.__init__(self,name,age,color,food)
        typee.__init__(self,kind)
    @staticmethod
    def act():#override  method
    
        print("cat loves mew")
    def speak(self):
        print("cat mewww")


animal1  = cat("kitty",3,"white","dry food","pet")
animal1.print_info()
animal1.print_type(animal1.name)
animal1.act()
animal1.speak()
print('-'*60)
animal2 = dog("hulk",7,"black","bones")
animal2.print_info()
animal2.speak()