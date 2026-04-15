from abc import ABCMeta , abstractmethod

class task(metaclass = ABCMeta) :
    def __init__(self,title,deadline,statue):
        self.title = title
        self.__deadline = deadline
        self.statue = statue
    
    def __str__ (self) :
        return f'''task : {self.title}
        deadline : {self.__deadline} 
        statue : {self.statue} '''
    
    def get_deadline(self) :
        return self.__deadline
    
    def self_deadline(self,new_deadline) :
        if self.__deadline == "You missed deadline!" :
            self.__deadline = new_deadline
        return new_deadline
    
    def ubdate_statue(self,new_statue) :
        if self.statue != "done" :
            self.statue = new_statue

    @abstractmethod
    def type_of_task(self) :
        pass


class personaltask(task):
    def __init__(self, title, deadline, statue):
        super().__init__(title, deadline, statue)

    def type_of_task(self) :
        print("this is apersonal task")

class worktask(task):
    def __init__(self, title, deadline, statue):
        super().__init__(title, deadline, statue)

    def type_of_task(self) :
        print("this is a work task")


task1 = personaltask('gym',3,'not done')

print(task1)
task1.ubdate_statue("done")
print(task1)