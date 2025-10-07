

# 1.swapcase( )
def swap_case(text):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            result += chr(ord(char)-32)
        elif 'A' <= char <= 'Z':
            result += chr(ord(char)+32)
        else:
            result += char
    return result

text="PyThOn"
print(swap_case(text))


# 2.strip( ) 
def strip_space(text):
    result = ""
    for i in text:
        if i == " ":
            continue
        else:
            result += i
    return result

text = "    Python  "
print(strip_space(text))


#lstrip( )
def lstrip_space(text):
    result = ""
    skip = True
    for i in text:
        if skip and i == " ":
            continue
        else:
            skip = False
            result += i
    return result

text = "    Python  "
print(lstrip_space(text))


#rstrip( )
def rstrip_space(text):
    result = ""
    skip = True
    for i in reversed(text):
        if skip and i == " ":
            continue
        else:
            skip = False
            result = i + result
    return result

text = "    Python  "
print(rstrip_space(text))


# 3. count( )
def my_count(s, ch):
    c = 0
    for i in s:
        if i == ch:
            c += 1
    return c

text = "banana"
print("Count of 'n':", my_count(text, 'n'))

# 4. replace() function
def my_replace(s, old, new):
    result = ""
    for i in s:
        if i == old:
            result += new
        else:
            result += i
    return result


text = "banana"
print("Replaced", my_replace(text, 'a', 'o'))
