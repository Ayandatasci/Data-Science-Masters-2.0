'''Q1, Create a vehicle class with an init method having instance 
variables as name_of_vehicle, max_speed and average_of_vehicle.'''

class vehicle:
    def __init__(self, name_of_vehicle,max_speed,average_of_vehicle):
        self.name_of_vehicle= name_of_vehicle
        self.max_speed= max_speed
        self.average_of_vehicle= average_of_vehicle

    def get_details(self):
        print(f"The name of vehicle is {self.name_of_vehicle}")
        print(f"The maximum speed of vehicle is {self.max_speed} km/h")
        print(f"The average of vehicle is {self.average_of_vehicle} km/l")

obj= vehicle("Toyota",180,20)
obj.get_details()