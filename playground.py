# Advanced arguments in Python (args and kwargs)
# Normally I use positional/keyword arguments like this:

def my_function(a, b, c):
    print(a)
    print(b)
    print(c)


# Positional Arguments are sensitive to the position

my_function(1, 2, 3)

# Keyword arguments are like this:

my_function(c=2, b=1, a=4)


# This can be tedious always adding values like above. Python has a method to create default arguments.
# I can simply assign values to the parameters in the function declaration:
def my_function(a=1, b=2, c=3):
    print(a, b, c)


my_function()


# So no inputs have to be used

# Unlimited arguments. If I have a function that should take a lot of arguments I can use the asteriks * to tell python
# that I want to use a lot of arguments. The function can take as many args as I want

def add(*args):
    return sum(args)


print(add(1, 2, 3, 4, 5, 10, 5, 55))


# This was the infinite positional arguments. There is also an infinite keyword operator called **kwargs

def calculate(n, **kwargs):
    print(kwargs)
    # This allows me to loop through the kwargs and find the argument I want
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


# This actually produces a dictionary with the keyword as key and the assigned value as value

calculate(2, add=3, multiply=5)


# So I can use this to create arguments that are optional. Taking a class as example

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        # Instead of [] to access the value of key, I can use get method. This is useful, because if the key doesn't
        # exist it returns none and doesn't crash.
        self.model = kwargs.get("model")
        self.colour = kwargs.get("colour")
        self.seats = kwargs.get("seats")


# If I now initialize the class I can add the attributes if I want.

car = Car(make="Nissan", seats=5)
print(car.model)
print(car.make)
print(car.seats)
