#Rotation of a matrix by 90 degrees clockwise
def rotate_90_clockwise(matrix):
    return [list(row) for row in zip(*matrix[::-1])]
m = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(rotate_90_clockwise(m))
#zip() always returns tuples (unless you explicitly convert them into another type, like list or set).


#Hollow Rectangle
n = 4
m = 6
for i in range(n):
    for j in range(m):
        if i==0 or j == 0 or i ==  n-1 or j == m-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


#Hollow Diamond
n = 5
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(2*i+1):
        if j == 0 or j == 2*i:
            print("*", end="")
        else:
            print(" ", end="")
    print()

for i in range(n-2, -1, -1):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(2*i+1):
        if j == 0 or j == 2*i:
            print("*", end="")
        else:
            print(" ", end="")
    print()