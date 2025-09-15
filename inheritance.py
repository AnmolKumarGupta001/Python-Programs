# Parent Class (Base Class)
class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    def show_info(self):
        print(f"This is a {self.color} {self.brand} vehicle.")

# Child Class (Derived Class)
class Car(Vehicle):   # Car inherits from Vehicle
    def __init__(self, brand, color, model):
        # Parent constructor call using super()
        super().__init__(brand, color)
        self.model = model
    
    def show_car_info(self):
        print(f"Car Details: {self.color} {self.brand} {self.model}")

# ---- Object Creation ----
car1 = Car("Toyota", "Red", "Innova")


# ---- Method calls ----
car1.show_info()        # Parent method
car1.show_car_info()    # Child method

