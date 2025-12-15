class Color:
    def __init__(self, color):
     self.color = color

class Brand (Color):
    def brand(self):
        print(self.color, "is the color of the car")

class Car (Brand):
    def details(self, brand ):
        print(self.color, "is the color of the car and the brand is", brand)

car = Car ("Gray")
car.brand()
car.details("Toyota")