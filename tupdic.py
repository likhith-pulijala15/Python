#Common built in functions for tuple, list and string

#len()
len("hello")   
len([1, 2, 3])   
len((4, 5, 6))   

#max()
max("hello")     
max([1, 5, 2]) 
max((7, 3, 9))   

#min()
min("hello")    
min([1, 5, 2])  
min((7, 3, 9))   

#sum()
sum([1, 2, 3])   
sum((4, 5, 6))   

#sorted()
sorted("hello")       
sorted([3, 1, 2])     
sorted((9, 5, 7))     

# any()
any("hello")      
any([0, 0, 5])     
any((0, 0, 0))     

# all()
all("hello")       
all([1, 2, 0])     
all((1, 2, 3))    

# enumerate()
list(enumerate("hi"))     
list(enumerate([10, 20]))  
list(enumerate((7, 8)))    

# reversed()
list(reversed("abc"))    
list(reversed([1, 2, 3])) 
list(reversed((4, 5, 6)))

#zip()
list(zip("abc", [1, 2, 3], (10, 20, 30)))



#Second large and small
ls = [5, 9, 6, 2, 10]
large = small = ls[0]
sec_large = sec_small = None  

for i in range(1, len(ls)):
    if ls[i] > large:
        sec_large = large      
        large = ls[i]
    else:
        if sec_large is None or ls[i] > sec_large:
            sec_large = ls[i]

   
    if ls[i] < small:
        sec_small = small    
        small = ls[i]
    else:
        if sec_small is None or ls[i] < sec_small:
            sec_small = ls[i]

print("Second Largest:", sec_large)
print("Second Smallest:", sec_small)
