# Palindrome recursion
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

word = input("Enter a string: ")
if is_palindrome(word):
    print("Palindrome")
else:
    print("Not Palindrome")


#Nth fibonnacii
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("Enter N: "))
print(f"The {n}th Fibonacci number is:", fibonacci(n))
