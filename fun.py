"""
A function in programming is a block code that does a particular task.
In using function, the first you do is to define the function, the you call the function, also known as invocation
"""
# function definition
def greet():
    print("Good day all")

# function call
greet()
greet()
greet()

# Function return keyword
def greet():
    return "Good day everyone"

print(greet())

# pass keyword
def greet():
    pass

print("hello world")

"""
Function parameter and argument
The parameters are variables used to define a function while the arguments are the values assigned to the 
parameters at the point of function call
"""
# function with a parameter
def square(info):
    return info**2
print(square(4)) # info is the parameter while 4 is the argument
print(square(5))
print(square(9))
name = "Patrick"
age  = 20
def details(a):
    return a+" I a python student"
print(details(name))
print(details("John"))
# area function 0.5*base*height
def angle(b,h):
    area = 0.5*b*h
    return area

print(angle(6,8))

def rectangle(l,w):
    pass

# Default Parameter Values
def location(a,city="Kubwa",address = "5 Nepa Road",country = "Nigeria"):
    return "I live at "+address+" "+ city+ ", "+country+ " My name is "+ a
print(location("Gwarinpa"))
print(location(name))

def addr():
    location = "Lagos"
    zone = "Lekki Epe expressway"
    return zone + ", " +location
print(addr())

def circle(r):
    pai = 3.14

def loc(city="Jos",address="Mbadiwe Ave",country="Nija"): 
    return city,address,country
print(loc("Maitama","Aguiyi Ironsi Ave","Nigeria"))




