'''Q3. What is multiple inheritance? 
Write a python code to demonstrate multiple inheritance.'''

#Multiple inheritance is a feature in object-oriented programming where a class can inherit attributes and methods from multiple parent classes


class papa:
    def papa_msg(self):
        print("Hi, this is Dad")
class mom:
    def mom_msg(self):
        print("Hi, this is Mom")
class child(papa, mom):
    pass

obj=child() # created object of child()
obj.papa_msg()
obj.mom_msg()