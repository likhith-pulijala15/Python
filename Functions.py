#---------- Basic Function----------#

def greet():
    print("Hello")
greet()

#---------- Function with parameters ----------#

def greet(name):
    print(f"Hello {name}")
greet("Likith")

#---------- Function with Multiple parameters ----------#

def add(a, b):
    print(a+b)
add(2, 3)

#---------- Function with Default parameters ----------#

def power(base, exponent = 2):
    return base**exponent
print(power(5))
print(power(5, 3))    #overrides default parameter

#---------- Function with Keyword arguments ----------#

def about(name, age):
    print(f"{name} is {age} year's old")
about(name="Likith", age="21")

#---------- Function with Variable positional arguments ----------#

def add(*numbers):         #lets you pass any number of positional arguments to a function.
    print(sum(numbers))
add(2,3)
add(2,3,5)

#---------- Function with Variable Keyword arguments ----------#

def details(**info):
        print(info)
details(name="Likhith", age=21, branch="ECE")

#---------- Nested Function ----------#

def outer():
    print("Outer function")
    def inner():
        print("Inner function")
    inner()
outer()

#---------- Lambda Function ----------#

add = lambda a, b: a+b
print(add(3, 7))