#----------------------- Diamond Pattern -----------------------#
# Single For Loop
n = 5
for i in range(1,n+1):
    print(" "*(n-i),"*"*(2*i-1))                
for i in range(n-1,0,-1):
    print(" "*(n-i),"*"*(2*i-1))

# Even stars
n = 5
for i in range(1,n+1):
    print(" "*(n-i),"* "*i)
for i in range(n-1,0,-1):                       
    print(" "*(n-i),"* "*i)

# Nested For Loops
n = 5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()
for i in range(n-1,-1,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()


#----------------------- Numeric Pyramid -----------------------#
# Ordered Numbers
n = 5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")              
    for j in range(1,i+1):
        print(j,end=" ")
    print()

# Same Numbers
n = 5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")               
    for j in range(i):
        print(i,end=" ")
    print()


#----------------------- Alphabetic Pyramid -----------------------#
n = 5
for i in range(1,n+1):
    for j in range(i):
        print(chr(65+j),end=" ")
    print()


#----------------------- Vowel and Consonant count -----------------------#
s = "music reduces depression"
vowels = "aeiou"
vowel_c = 0
consonant_c = 0

for i in s:
    if i.isalpha():
        if i in vowels:
            vowel_c += 1
        else:
            consonant_c +=1
print("Vowel Count: ",vowel_c)
print("Consonant Count: ",consonant_c)


#----------------------- Remove duplicates and sort them in non decreasing order -----------------------#
"""
i/p: [ 6,8,4,6,8,3,4,9]
o/p: [3,4,6,8,9]
"""

l1 = [6,8,4,6,8,3,4,9]
l2 = list(set(l1))
n = len(l2)

for i in range(n-1):
    for j in range(n-i-1):
        if l2[j] > l2[j+1]:
            l2[j], l2[j+1] = l2[j+1], l2[j]     
print(l2)

#Without using set
l1 = [6,8,4,6,8,3,4,9]
l2 = []

for i in l1:
    if i not in l2:
        l2.append(i)
n = len(l2)

for i in range(n-1):
    for j in range(n-i-1):
        if l2[j] > l2[j+1]:
            l2[j], l2[j+1] = l2[j+1], l2[j]     
print(l2)


#----------------------- WAP to find lcm of two numbers using while loop -----------------------#
a,b = 15,50
g = max(a,b)

while True:
    if g%a==0 and g%b==0:
        lcm = g
        break
    g += 1
print("LCM: ",lcm)


#----------------------- WAP to print list of strings sorted by length in increasing order -----------------------#
ls = ['a','ccc','bb','d','zz']
n = len(ls)
for i in range(n-1):
    for j in range(n-i-1):
        if len(ls[j]) > len(ls[j+1]):
            ls[j],ls[j+1] = ls[j+1],ls[j]
print(ls)

# without duplicate lengths
ls = ['a','ccc','bb','d','zz']
ls.sort(key=len)
unique = []
lengths = set()
for word in ls:
    if len(word) not in lengths:
        unique.append(word)
        lengths.add(len(word))
print(unique)


#----------------------- create a function that takes a list and returns second largest number in a list -----------------------#
ls = [2,6,7,67,87,9]
largest = sec_largest = ls[0]

for i in range(1,len(ls)):
    if ls[i] > largest:
        sec_largest = largest
        largest = ls[i]
    elif ls[i] > sec_largest and ls[i] < largest:
        sec_largest = ls[i]
print(sec_largest)


#----------------------- convert lower case to upper case and vise versa of a string -----------------------# a = 97 to 122 A = 65 to 90
s = "PYThon FuLL STacK Development"
new = ""
for char in s:
    if ord(char) >= 65 and ord(char) <= 90:
        new += chr(ord(char)+32)
    elif ord(char) >= 97 and ord(char) <= 122:
        new += chr(ord(char)-32)
    else:
        new += char
print(new)