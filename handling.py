# try - except - else - finally
try:
    result = 2 / 0 
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(result)
finally:
        print("Execution Complete!")

# Multiple except blocks
try:
    a = 2 + "b"
    b = int("abc")
except ValueError:
    print("Invalid number")
except TypeError:
    print("Wrong datatype")

# Raising Errors
def check(age):
    try: 
        if age < 5:
            raise ValueError("Age should be above 5")
        else:
            return "Valid age"
    except ValueError:
        return "Enter Valid age"
print(check(3))

# Custom exception class
class LowBalanceError(Exception):
      pass

def withdraw(amount,balance):
    if amount > balance:
        raise LowBalanceError("Insufficient Balance")
    else:
        return balance - amount

print(withdraw(1001,1000))
    
# Exception chaining
try:
    int("abc")
except ValueError as e:
    raise TypeError("Invalid type") from e