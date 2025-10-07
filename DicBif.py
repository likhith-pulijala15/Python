#Dictionary Built-in functions

my_dict = {"name":"Likhith","age":21,"branch":"ECE"}

#Accessing
#get() -- Returns value of key
print(my_dict.get("name"))

#keys() -- Returns all keys
print(my_dict.keys())

#values() -- Returns all values
print(my_dict.values())

#items() -- Gives key value pairs as tuple
print(my_dict.items())



#Adding and updating
my_dict.update({"age":22}) #Updates age
print(my_dict)

my_dict.update({"city":"Suryapet"}) #Adds key-value pair
print(my_dict)


#Removing
print(my_dict.pop("age")) #Removes key and returns its value
print(my_dict.popitem()) #Removes and returns the last inserted (key, value) pair.
# my_dict.clear()


#Copy and create
new_dict  = my_dict.copy()
print(new_dict)

#fromkeys() -- Creates a dictionary with given keys, all set to the same value.
keys = ['a','b','c','d']
print(dict.fromkeys(keys,0))

#Check
print("name" in my_dict)
print(len(my_dict))

#setdefault() -- Returns value of key. If not present, inserts key with default.
print(my_dict.setdefault("Skill","Python"))
print(my_dict)




#Internal code for from keys
def fromkeys(iterable, value=None):
    new_dict = {}
    for key in iterable:
        new_dict[key] = value
    return new_dict

ls = ['a','b','c']
print(fromkeys(ls,1))