#Activity Week7-1.2: Singleton Design Pattern - Follow up Question
#Is "car_name" variable is the same location in the memory? Debug the code to get the name of the car from end user? See below code:
 
 
 
class RentalManager:
    _instance = None
 
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RentalManager, cls).__new__(cls)
            cls._instance.cars_available = ["Toyota", "Honda", "Ford"]
        return cls._instance
 
    def rent_car(self, car_name):
        print(f"input car_name = {car_name}, id = {id(car_name)}")
        # Check if the variable is the same location in memory
        if car_name in self.cars_available:
            self.cars_available.remove(car_name)
            print(f"{car_name} has been rented.")
        else:
            print(f"{car_name} is not available.")
 
    def show_available_cars(self):
        print("Available cars:", self.cars_available)
 
car_name = input("Enter the name of the car you want to rent: ")
print(f"car_name = {car_name}, id = {id(car_name)}")    
# Check if the variable is the same location in memory  
manager1 = RentalManager()
manager2 = RentalManager()
 
manager1.rent_car(car_name)
manager2.show_available_cars()  # Affects both because it's the same instance
 
print("Are both managers the same object?", manager1 is manager2)

print("ID of manager1:", id(manager1))
print("ID of manager2:", id(manager2))
