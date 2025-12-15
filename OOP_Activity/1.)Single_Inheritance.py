class Animal:
    def __init__(self, name):
        self.name = name


class Mouse(Animal):
    def show_role(self):
        print(self.name, "is a mouse.")


animal = Mouse("Jerry")
print("The name of the mouse is", animal.name)
animal.show_role()