class student_info:

    id_N_allowed =[22410290,224101291,224101292]#class atributes
    student_num = 0
    skills = ["arabic",'english',"python",'mathmatics']


    @classmethod
    def show_student_numbers(cls):#class method to use class atributes
        if  cls.student_num == 0:
            print(f"the number of student before join is {cls.student_num}")
        else :
            print(f"the number of student after join is {cls.student_num}")


    def __len__ (self):#magic method
        return len(self.name)
    

    def __init__(self,ID,name,age,National_Num,gender): # (constractor),__init__ to access object attributes , self is the object
        self.name = name  #define the paramter
        self.ID =  ID 
        self.age = age
        student_info.student_num +=1
        self._National_Num= National_Num #_variable --> protected member that we can access in base & child class
        self.__gender = gender ##__variable --> private member that we can access in its class
        self.lst= []

    def add_student(self,student):
        self.lst.append(student)
        return f'new stydent is {student.name}'
    


    def print_info(self):
        if self.ID in student_info.id_N_allowed :
            return f"hi {self.name}\nSorry!you are fired"
        elif self.age >= 18 :
            return f"hello {self.name}\n your age is :  {self.age},\n your ID is : {self.ID} "
        elif self.age <18 :
            print("I'm sorry your not accebtable")


    @staticmethod
    def welcome() :#has no parameter
        print("welcome everybody and thaanks for join us")
    @property # transform method (m()) --> variable (m)
    def get_gender(self) : #get method to access private members
        return self.__gender

    def set_gender(self,new_gender) : #set method to set value for private members
        self.__gender = new_gender
        return self.__gender
    


student_info.show_student_numbers()
student1 = student_info(224101240,"mohamed",19,177897495068,"male") #pass argument to instance method(constructor)
student2 = student_info(224101291,"ali",22,879038876900,"female")
student3 = student_info(224101135,"jee",17,1498705739905,"Male")
#print(student1.ID)
print(student1.add_student(student2))
print(student1.print_info(),"\n\n")
print(student2.print_info(),'\n\n')
print(student3.print_info(),'\n\n')

student_info.show_student_numbers()

student_info.welcome()
print(len(student1))
print(student_info.skills)
print(student1._National_Num)
#print(student1._student_info__gender)#illegalway to access private members
print(student1.get_gender)#male
student1 = student_info(224101240,"mohamed",19,177897495068,"male")
print(student1.get_gender)#male(doesn't change)
print(student1.set_gender("female"))#female