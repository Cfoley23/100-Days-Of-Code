# *args returns a tuple

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(3, 5, 6, 4, 5, 6, 7, 8, 9, 111234, 3, 345, 6543, .1)*2)

# **kwargs returns a

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items()
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(4, add=3, multiply=3)


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")


my_car = Car(make="Nissan", model="Skyline", seats=2, color="Black")
print(my_car.model)
