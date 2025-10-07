
#print numbers from 100 to 0 in reverse which are divisible by 5 
def print_num(m,n):
    for i in range(m,n,-1):
        if i%5==0:
            print(i)
m = 100
n = 0
print_num(m,n)


print()
#check whether given string is a palindrome or  not using a function
str = "madam"
def check_palindrome(str):
    reversed = ""
    for c in str:
        reversed = c + reversed
    if reversed == str:
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")
check_palindrome(str)
  
print()
#wirte a function to print tables in reverse
# # for eg: 3x10=30
#           3x9=27
#           3x8=24

def print_table(num):
    for i in range(10, 0, -1):
        print(f"{num} x {i} = {num * i}")
num = 3
print_table(num)