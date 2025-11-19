#Hollow Pattern
n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == 1 or j == 1 or i == n or j == n:
            print("*",end=" ")
        else:
            print(" ",end = " ")
    print()


# Factorial using recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))