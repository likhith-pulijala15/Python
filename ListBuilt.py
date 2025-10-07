# Different built-in functions on lists
numbers = [0, 1, 2, 3, 4, 5]
words = ["apple", "banana", "cherry", ""]

print("any(numbers):", any(numbers))       
print("all(numbers):", all(numbers))       
print("len(numbers):", len(numbers))       
print("max(numbers):", max(numbers))       
print("min(numbers):", min(numbers))       
print("sum(numbers):", sum(numbers))       
print("sorted(words):", sorted(words))     
print("list(reversed(numbers)):", list(reversed(numbers)))  
print("enumerate(words):", list(enumerate(words)))          
print("zip(numbers, words):", list(zip(numbers, words)))   


print()
#Clear()
def clear(lst):
    lst[:] = []  
    return lst
my_list = [1, 2, 3]
clear(my_list)
print(my_list)  


print()
#sort(key==len)
def sort_by_key(lst, key):
   
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if key(lst[i]) > key(lst[j]):
                lst[i], lst[j] = lst[j], lst[i]
    return lst

words = ["banana", "kiwi", "apple", "cherry"]
print(sort_by_key(words, key=len)) 
