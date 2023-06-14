'''Q4. What are getter and setter in python? 
Create a class and create a getter and a setter method in this class.'''

#In Python, getters and setters are methods used to access (get) and modify (set) the values of class attributes respectively.

class person:
    def __init__(self,name,age):
        self.__name= name
        self.__age= age
    
    def get_age(self):
        print(f"{self.__name}'s age is {self.__age}")
    def set_age(self,new_age):
        if new_age>0:
            print(f"{self.__name}'s age is {new_age}")

obj= person("Ayan",19)
obj.get_age() #prints initial value
obj.set_age(25) #prints new value
