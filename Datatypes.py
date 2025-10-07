#-------------------------   Basic  ---------------------------#
InstituteName = "10,000 Coder's"            #PascalCase   
class_name = "67r"                          #Snake_case
userName = "Likith"                         #camelCase

a = 15
b = 0.5
c = "Python"
d = True

print(a," Type: ",type(a),"Id: ",id(a))
print(b," Type: ",type(b),"Id: ",id(b))
print(c," Type: ",type(c),"Id: ",id(c))
print(d," Type: ",type(d),"Id: ",id(d))

#-------------------------   Intermediate  ---------------------------#

#List Practice
players = ["Rohit","Virat","Gill","Dhoni"]
players[2] = "Surya"
players.append("Jadeja")
print(players)
print("Length: ",len(players)," 2nd last: ",players[-2])


print()
#Tuple Practice
laptop_info = ("HP","16GB","512GB SSD",2024,True)
print("Tuples, once created cannot be modified")
print("Last two: ",laptop_info[-2:])

print()
#Set Practice
countries = {"India","USA","India","Canada","UK","USA"}
print(countries)
countries.add("Germany")
countries.remove("UK")
print(countries)

print()
#Frozenset Practice
frozen_marks = frozenset([90,85,75,85])
print("Frozensets are Immutable")
print(type(frozen_marks))

#-------------------------   Advanced ---------------------------#

#Dictionaries
car_info = {
    "brand": "Tesla",
    "model": "Model S",
    "price": "1.5Cr",
    "features": ["Autopilot","Electric","Sunroof"]
}

car_info["color"] = "white"
car_info["price"] = "1.7Cr"
car_info["insurance"] ={
    "provider": "HDFC",
    "valid_till": "2026"
}

print(car_info)


print()
#List of dictionaries
books = [
{"title": "Atomic Habits", "author": "James Clear"},
{"title": "Ikigai", "author": "Héctor García"},
{"title": "Zero to One", "author": "Peter Thiel"}
]

books.append({"title": "Deep Work", "author":"Cal Newport"})
print(books)

for book in books:
    if book["author"] == "Peter Thiel":
        print("Title of book by Peter Thiel: ",book["title"])

print()
#Nested Dictionary
laptop = {
    "brand": "Apple",
    "specs": {
        "ram": "16GB", 
        "storage": "1TB SSD",
        "chip": "M2"
    },
    "price": "2L"
}

print("Chip: ",laptop["specs"]["chip"])
print(f"{laptop['brand']} laptop comes with {laptop['specs']['chip']} and costs {laptop["price"]}")
