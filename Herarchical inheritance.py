class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start_engine(self):
        print(f"{self.brand} {self.model}'s engine has started")

class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors
    
    def open_trunk(self):
        print("Car trunk has been opened")

class Bike(Vehicle):
    def __init__(self, brand, model, bike_type):
        super().__init__(brand, model)
        self.bike_type = bike_type
    
    def wheelie(self):
        print("The bike is doing a wheelie!")

class Truck(Vehicle):
    def __init__(self, brand, model, load_capacity):
        super().__init__(brand, model)
        self.load_capacity = load_capacity
    
    def load_cargo(self):
        print(f"{self.load_capacity} kg of cargo has been loaded")

# Usage
car = Car("Toyota", "Corolla", 4)
bike = Bike("Yamaha", "R15", "Sports")
truck = Truck("Tata", "407", 5000)

# Common method from parent class
car.start_engine()  # Inherited from Vehicle
bike.start_engine() # Inherited from Vehicle
truck.start_engine() # Inherited from Vehicle

# Unique methods for each child class
car.open_trunk()    # Car's specific method
bike.wheelie()      # Bike's specific method
truck.load_cargo()  # Truck's specific method
