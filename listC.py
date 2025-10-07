
#Create a list of factorials of the first 5 numbers using list comprehensions.
def fact_num(n):
    fact = 1
    for i in range(1,n+1):
        fact*=i
    return fact

lis = [1,2,3,4,5]
factorials = [fact_num(x) for x in lis]
print(factorials)


#Check previous and next numbers of given num is armstrong or not?
num = 153 

for check_num in [num, num - 1, num + 1]:
    digits = len(str(check_num))
    total = 0
    temp = check_num

    while temp:
        total += (temp % 10) ** digits
        temp //= 10

    if total == check_num:
        if check_num == num:
            print(check_num, "is an Armstrong number (entered number)")
        elif check_num == num - 1:
            print(check_num, "is an Armstrong number (previous number)")
        else:
            print(check_num, "is an Armstrong number (next number)")
    else:
        if check_num == num:
            print(check_num, "is not an Armstrong number (entered number)")
        elif check_num == num - 1:
            print(check_num, "is not an Armstrong number (previous number)")
        else:
            print(check_num, "is not an Armstrong number (next number)")