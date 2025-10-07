#To pack the multiple values into a list, tuple, dictionary or set in simple way then we can use comprehensions
#Comprehensions is a combination of operations/expression, iterations and conditions (Optional)


"""
A list comprehension in Python is a concise way to create lists using a single line of code.
It combines loops and conditional logic into a compact syntax.

General Syntax:
[expression for item in iterable if condition]

expression → What to store in the list
item → Current element from the iterable (like a list, string, or range)
iterable → Sequence to loop over
condition (optional) → Filter elements

1.Basic list creation
# Create a list of numbers from 0 to 9
numbers = [x for x in range(10)]
print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

2. Applying an expression
# Squares of numbers
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

3. With condition
# Even numbers only
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

4. Nested loops
# Pairs (like Cartesian product)
pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
print(pairs)  # [(1, 3), (1, 4), (2, 3), (2, 4)]

5. With if-else
# Label even and odd numbers
labels = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
print(labels)  # ['Even', 'Odd', 'Even', 'Odd', 'Even']

"""

# str  = "Welcome"
# op =[x for x in str]
# print(op)

# op =[x+" Hi" for x in str]
# print(op)

# op = [i for i in range(1,11)]
# print(op)

# op = [i**2 for i in range(1,11)]
# print(op)

# op = [i for i in range(1,11) if i%2==0]
# print(op)

# ip = [1,4,7,9,11,13,24,56,108,234,125]
# op = [i*2 for i in ip if i%2==0]
# print(op)


# def factorial(num):
#     fact*=num
#     return fact

# op = [factorial(x) for x in range(1,6)  ]
# print(op)


"""
list comprehension --> list[] or []
tuple comprehension --> tuple()
set comprehensions --> {}
dictionary comprehension --> {}
"""

# op = {"x":x**2 for x in range(1,25)} 
# print(op)

# op = {x:x**2 for x in range(1,25)} 
# print(op)

op = tuple((x,x**2) for x in range(2,6))
print(op)

ip = ['Sravani','Sravan','kumar','kumari','lalitha','lalith','arjun','lakshmi','nandini']
op = tuple((name.lower(), "Female" if name.lower().endswith(("i","a")) else "Male")for name in ip)
print(op)


ip = ['Sravani','Sravan','kumar','kumari','lalitha','lalith','arjun','lakshmi','nandini']
op = []
for name in ip:
    lower_name = name.lower()
    if lower_name.endswith(("i", "a")):
        gender = "female"
    else:
        gender = "male"
    op.append((lower_name, gender))

print(op)



