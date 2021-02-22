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

a = [7, 3, 6, 8, 2, 3, 7, 2, 6, 3, 6]
b = a
c = b
b = c
 
def remove_elem(data, target):
	new_data = data[:]
	for item in data:
		if item == target:
			new_data.remove(target)
	return new_data
 
def get_product(data):
	new_data = data[:]
	total = 1
	for i in range(len(data)):
		total *= new_data.pop()
	return total
 
remove_elem(c, 3)
print(get_product(b))
print(a)  
     

