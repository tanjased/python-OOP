class ElectronicDevices:
    def __init__(self, code, year):
        self.code = code
        self.year = year


class Computer(ElectronicDevices):
    def __init__(self, code, year, brand):
        super().__init__(code, year)
        self.brand = brand


class TV(ElectronicDevices):
    def __init__(self, code, year, screen):
        super().__init__(code, year)
        self.screen = screen


class Desktop(Computer):
    def __init__(self, code, year, brand, ram):
        Computer.__init__(self, code, year, brand)
        self.ram = ram


class Laptop(Computer):
    def __init__(self, code, year, brand, diagonal):
        Computer.__init__(self, code, year, brand)
        self.diagonal = diagonal


comp = Desktop('230011', '2020', 'Lenovo', '8 Gb')
laptop = Laptop('230031', '2017', 'Asus', '16.1"')

print(laptop.diagonal)