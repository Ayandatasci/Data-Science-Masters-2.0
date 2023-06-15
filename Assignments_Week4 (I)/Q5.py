'''Q5.What is method overriding in python? 
Write a python code to demonstrate method overriding.'''

#Method overriding is a feature in object-oriented programming where a child class provides a different implementation for a method that is already defined in its parent class. 

class animal:
    def sound(self):
        print("Animal makes sounds")

class dog(animal):
    def sound(self):
        print("Dog barks")

class cat(animal):
    def sound(self):
        print("Cats meows")

Bholu=dog()
Tiger=cat()
Bholu.sound()
Tiger.sound()