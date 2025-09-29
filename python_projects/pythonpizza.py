print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? Type 'S', 'M' or 'L': ")
price = 0
if size == "S":
    price = 15
elif size == "M":
    price = 20
elif size == "L":
    price = 25
else:
    print("Incorrect input: Please enter the pizza size you want: ")

pepperoni = input("Do you want pepperoni on your pizza? 'Y' or 'N': ")
if pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3

extra_cheese = input("Do you want extra cheese? 'Y' or 'N': ")
if extra_cheese == "Y":
    price += 1
else:
    price = price

print(f"Your final bill is : ${price}")

# Notes for today:
# I made my code less efficient by not utilizing nested conditional statements the first time I tried this coding challenge.
# My code still worked, but it was a bit cluttered and was harder to read than this version, particularly in the section calculating the cost w/ or w/o pepperoni.
# I notice that I tend to overcomplicate my code, so I'm glad I can use this as an opportunity to improve on my foundation.
# I'm glad I recognized this issue and that I'm learning how to better handle these scenarios by using nested conditional statements.
# Below is my original code:

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? Type 'S', 'M' or 'L': ")
# price = 0
# if size == "S":
#     price = 15
# elif size == "M":
#     price = 20
# elif size == "L":
#     price = 25
# else:
#     print("Incorrect input: Please enter  pizza size you want: ")

# pepperoni = input("Do you want pepperoni on your pizza? 'Y' or 'N': ")
# if size == "S" and pepperoni == "Y":
#     price += 2
# elif size == "M" and pepperoni == "Y":
#     price += 3
# elif size == "L" and pepperoni == "Y":
#     price += 3
# else:
#     price = price

# extra_cheese = input("Do you want extra cheese? 'Y' or 'N': ")
# if extra_cheese == "Y":
#     price += 1
# else:
#     price = price

# print(f"Your final bill is : ${price}")

