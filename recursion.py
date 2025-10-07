import sys
print(sys.getrecursionlimit())

"""
Recursion:
-- Recursion is a programming technique where a function calls itself (directly or indirectly) in order to solve a problem.
-- Each recursive call works on a smaller sub-problem of the original problem.
-- Every recursive function must have a base case (stopping condition) to prevent infinite calls.
-- The process continues until the base case is reached, after which results are combined (returned) back through the call stack.

Syntax:
def recursive_function(parameters):
    if base_case_condition:
        return result  # base case
    else:
        return recursive_function(modified_parameters)  #recursive call

"""

#Factorial
def factorial(n):
    if n == 0 or n == 1:   # base case
        return 1
    return n * factorial(n-1)  # recursive case
print(factorial(5))  


#Number print
def print_numbers(n):
    if n == 0:  # base case
        return
    print_numbers(n-1)   # recursive call first
    print(n)             # action after
print_numbers(5)



#Fibonacci
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def fibonacci_Seq(n):
    return [fibonacci(i) for i in range(n)]
print(fibonacci_Seq(8))


#sum
def summ(n):
    if n==1:
        return n
    return n+summ(n-1)
n = 10
print(summ(n))


#Palindrome
def palindrome(s,i,j):
    if i>=j:
        return True
    if s[i]!=s[j]:
        return False
    else:
        return palindrome(s,i+1,j-1)
s = "madam"
i=0
j=len(s)-1
print(palindrome(s,i,j))

#for else
