class Bacteria:
    # Complete the class
    numm = 12

    def __init__(self, shape, size, name, color, singular):
    	self.shape = shape
    	self.size = size
    	self.name = name
    	self.color = color
    	self.singular = singular



# Create 3 instances

bacilli = Bacteria("rod-shaped", "small", "Bacilli", "blue", "bacillus")
cocci = Bacteria("sphere-shaped", "small", "Cocci", "blue", "coccus")
Spirilli = Bacteria("spiral-shaped", "small", "Spirilli", "blue", "spirillum")

# print(Bacteria.numm)


# class BouncyBall:
#     def __init__(self, price, size, brand):
#         self._price = price
#         self._size = size
#         self._brand = brand

#     @property
#     def price(self):
#         return self._price

#     @price.setter
#     def price(self, new_price):
#         if 0 < new_price < 500:
#             self._price = new_price

#     @property
#     def size(self):
#         return self._size

#     @size.setter
#     def size(self, new_size):
#         if isinstance(new_size, str):
#             self._size = new_size    

#     @property
#     def brand(self):
#         return self._brand

#     @brand.setter
#     def brand(self, new_brand):
#         if isinstance(new_brand, str):
#             self._brand = new_brand      

class BouncyBall:
    def __init__(self, price, size, brand):
        self._price = price
        self._size = size
        self._brand = brand

    def get_price(self):
        return self._price

    def set_price(self, new_price):
        if 0 < new_price < 500:
            self._price = new_price

    price = property(get_price, set_price)        

    def get_size(self):
        return self._size

    def set_size(self, new_size):
        if isinstance(new_size, str):
            self._size = new_size   

    size = property(get_size, set_size)   
            
    def get_brand(self):
        return self._brand

    def set_brand(self, new_brand):
        if isinstance(new_brand, str):
            self._brand = new_brand             

    brand = property(get_brand, set_brand)

ball = BouncyBall(370, "M", "Volley")
ball.brand = "Yamaha"
print(ball.brand)       

