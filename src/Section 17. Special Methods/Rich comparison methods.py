class Temp():
    """Represents the temperatures in the certain cities."""

    months = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun", 7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}

    def __init__(self, city, temp, month):
        self.city = city
        self.temp = temp
        self.month = month

    def __str__(self):
        return f'The temperature in {Temp.months[self.month]} in {self.city} is {self.temp}°C.'

    def __lt__(self, other):
        if self.month == other.month:
            return self.temp < other.temp
        else:
            print("You compare different months! It's unfair.")

    def __le__(self, other):
        return self.temp <= other.temp

    def __gt__(self, other):
        return self.temp > other.temp

    def __ge__(self, other):
        return self.temp >= other.temp

    def __eq__(self, other):
        return self.temp == other.temp

    def __ne__(self, other):
        return self.temp != other.temp


msq = Temp("Minsk", "18.1", 5)
waw = Temp("Warsaw", "19.5", 5)
lnd = Temp("London", "14.0", 6)

# print(msq)
print(msq != lnd)
print(msq < waw)
print(lnd < waw)