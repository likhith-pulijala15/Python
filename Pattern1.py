
#Centered Pyramid
n = 5
for i in range(n):
    # print spaces
    for j in range(n - i - 1):
        print(" ", end="")
    # print stars (2*i+1 for odd numbers)
    for j in range(2 * i + 1):
        print("*", end="")
    print()

    
#Diamond
n = 5
for i in range(1, n+1):
    print(' ' * (n - i) + '*' * (2*i - 1))

for i in range(n-1, 0, -1):
    print(' ' * (n - i) + '*' * (2*i - 1))

print()
#Left-Aligned Half Diamond
n = 5
for i in range(1, n+1):
    print('*' * i)
for i in range(n-1, 0, -1):
    print('*' * i)


print()
#Right-Aligned Half Diamond
n = 5
for i in range(1, n+1):
    print(' ' * (n - i) + '*' * i)

for i in range(n-1, 0, -1):
    print(' ' * (n - i) + '*' * i)