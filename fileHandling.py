# File Handling Syntax 
"""
file = open("sample.txt","mode")
we have to close the file using file.close()

using 'with' it automatically closes file even if error occurs
with open("sample.txt", "mode") as f:
    f.write()
"""

# ------------- Write Operations ----------------
with open("sample.txt","w") as f:
    f.write("Hello World\n")
              
    lines = ["Java\n","HTML\n","MySQL\n","JavaScript\n","Django\n"]
    f.writelines(lines)                     

#Write and Read
with open("example.txt", "w+") as f:
    f.write("New file")
    f.seek(0)
    print(f.read())


# ------------- Read Operations ----------------

with open("sample.txt", "r") as f:
    data = f.read()
    print(data)

with open("sample.txt", "r") as f:
    print(f.readline())
    print(f.readline())

with open("sample.txt","r") as f:
    data = f.readlines()
    print(data)

with open("example.txt", "r+") as f:
    print(f.read())      
    f.seek(0)           
    f.write("Hello\n") 

with open("sample.txt") as f:
    for line in f:
        print(line.strip())

 

# ------------- Appending ----------------
with open("sample.txt", "a") as f:
    f.write("This line is added at end")

with open("log.txt", "a+") as f:
    f.write("Added line\n")
    f.seek(0)                           
    print(f.read())


# ------------- Exclusive Creation ----------------
try: 
    with open("sample.txt","x") as f:
        f.write("Created")
except FileExistsError:
    print("File already exists")


# ------------- Binary Mode----------------
with open("photo.jpg", "rb") as f:
    data = f.read()     

with open("photo.jpg", "wb") as f:
    f.write(data)       


# ------------- Text Mode ----------------
with open("file.txt", "rt") as f:
    data = f.read()

with open("file.txt", "wt") as f:
    f.write("text")
