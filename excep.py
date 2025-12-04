#1
try:
    x = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero")

#2
try:
    a = int("a")
except ValueError:
    print("Invalid Value")

#3
try:
    a = [1,2,3]
    print(a[3])
except IndexError:
    print("Index out of range")

#4
try:
    b = "1" + 1
except TypeError:
    print("Type Error")
else:
    print(b)

#5
try:
    b = [4,5,6]
    c = b[3]
except IndexError:
    print("Index out of range")
else:
     print(c)

#6
try:
    y = 5 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Execution Completed")

#7
try:
    b = "a" + 1
except TypeError:
    print("Type Error")
else:
    print(b)
finally:
    print("Always runs error or no error")

#8
age = 17
if age < 18:
    raise ValueError("Age must be 18+")
else:
    print(age)

#9
def divide(a,b):
    try:
        return a // b
    except ZeroDivisionError:
        return "Cannot divide by zero"
print(divide(8,0))

#10
try:
    a = int("abc")
except (ValueError, TypeError):
    print("Invalid operation")
