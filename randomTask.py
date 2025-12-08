import random

# Dice
def roll(win):
    dice = [1,2,3,4,5,6]
    roll = random.choice(dice)
    if roll == win:
        return f"You Won!, you rolled {roll}"
    else:
        return f"You Lost!, you rolled {roll}"

print(roll(5))

# Shuffle
num = [1,2,3,4,5,6]
numbers = ["first","second","third","fourth","fifth"]
s1 = random.shuffle(num)
random.shuffle(numbers)
print(s1) #returns none
print(numbers)

# OTP
def sendOtp():
    otp = random.randint(4000,9000)
    return f"Otp: {otp}"
print(sendOtp())

# Random: returns float between 0.0 to 1.0
x = random.random()
print(x)

# Range
a = random.randrange(0,10,2)
print(a) #any number from 0,2,4,6,8