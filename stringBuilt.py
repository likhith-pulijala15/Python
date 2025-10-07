#Built-in functions of strings
s = "Hello123 World"

print("len(s):", len(s))                
print("s.upper():", s.upper())           
print("s.lower():", s.lower())           
print("s.title():", s.title())         
print("s.strip():", s.strip())           
print("s.split():", s.split())           
print("s.join(['Hi','Bye']):", " ".join(['Hi', 'Bye']))  
print("s.replace('World','Python'):", s.replace("World", "Python")) 
print("s.startswith('Hello'):", s.startswith("Hello")) 
print("s.endswith('ld'):", s.endswith("ld"))            
print("s.find('123'):", s.find("123"))                  
print("s.isalnum():", s.isalnum())                      
print("s.isalpha():", s.isalpha())                      
print("s.isdigit():", s.isdigit())                     
print("s.isspace():", s.isspace())                    


print()
#isalnum()
def my_isalnum(string):
    if not string:   
        return False
    for ch in string:
        if not (('a' <= ch <= 'z') or ('A' <= ch <= 'Z') or ('0' <= ch <= '9')):
            return False
    return True

print("\nCustom isalnum():")
print(my_isalnum("Hello123"))   
print(my_isalnum("Hello 123"))  
print(my_isalnum(""))          

print()
#find(substring)
def my_find(s, sub):
    n, m = len(s), len(sub)
    if m == 0: 
        return 0
    for i in range(n - m + 1):
        if s[i:i+m] == sub:
            return i
    return -1

print("\nCustom find():")
print(my_find("Hello123 World", "123"))  
print(my_find("Hello123 World", "Python"))  
print(my_find("abcdabcd", "bcd"))        
