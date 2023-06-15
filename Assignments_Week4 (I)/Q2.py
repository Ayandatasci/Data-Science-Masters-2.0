'''Q2. Create a child class car from the vehicle class created in Que 1,
which will inherit the vehicle class.Create a method named seating_capacity 
which takes capacity as an argument and returns the name of the vehicle and its seating capacity.'''

class vehicle:
    def __init__(self,name,seats):
        self.name= name
        self.seats= seats
class car(vehicle):
    def seating_capacity(self):
        print(f"The name of the vehicle is {self.name} and its seating capacity is {self.seats}")

obj=car("Sedan",4)
obj.seating_capacity()