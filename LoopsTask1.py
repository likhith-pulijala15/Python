#Task 1
l1 = ["sravan", "harish", "aravind","akhil"]
l2 = [24, 17, 20, 18]

for i in range(len(l1)):
        if l2[i] >= 18:
            print(l1[i],"is eligible")
        else:
            print(l1[i],"is not eligible")
 

print()
#Task 2
num = 123
sum_digits = 0
while num>0:
    digit = num%10
    sum_digits += digit
    num = num//10
print("Sum of digits: ",sum_digits)

num = "123"
sum_digits = 0
for digit in num:
    sum_digits += int(digit)
print("Sum of digits: ",sum_digits)


print()
#Task 3
num = str(123498)
big = int(num[0])
for digit in num:
    d = int(digit)
    if d>big:
        big = d
print(big)


print()
#Task 4
rs = 100
choc = rs// 1 #100
wraps = choc // 3 #33
total_choc = choc + wraps #133
while wraps >= 3:         
    choc = wraps // 3 
    total_choc += choc
    wraps = (wraps % 3) + choc
print( total_choc)