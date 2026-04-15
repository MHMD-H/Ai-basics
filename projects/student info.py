from abc import ABCMeta,abstractmethod
class student(metaclass=ABCMeta) :
    def __init__(self,name,age,grade,email):
        self.name = name 
        self.age = age
        self.grade = grade
        self.__email = email
    def __str__(self) : 
        return f'''name is {self.name} 
age is : {self.age} 
grade is {self.grade}
email is :{self.__email}'''
    
    def get_email(self):
        return self.__email
    
class StudentManager(student):
    def __init__(self, name, age, grade, email):
        super().__init__(name, age, grade, email)

    