class Laptop:
    def __init__(self, name):
     self.name = name

class Brand:
    def __init__(self, ACER):
        self.ACER = ACER

class Version (Laptop, Brand):
    def __init__(self, name, brand):
        Laptop.__init__(self, name)
        Brand.__init__(self, brand)

    def details(self):
        print("The brand of laptop is", self.name, " and the version is", self.ACER)

lap = Version ("ACER", "Aspire Lite 15")
lap.details()