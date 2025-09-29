player = input("What is your name? ")

# Beginning of game
print("Welcome to Treasure Island, " + player + "!")
print("Your mission is to find the treasure.")
choice1 = input("Do you want to go left or right (Type 'L' or 'R' ")

# First choice
if choice1 == "L":
    print("You came to a lake and started swimming, but you got tired after a while.")
    choice2 = input("Keeping swimming or wait?: (Type 'S' or 'W' ")
elif choice1 == "R":
    print("You fell into a hole! Game over!")
else:
    print("You fell into a hole! Game over!")

# Second choice
if choice2 == "W":
    print("You regained your energy and swam until you reached the shore.")
    choice3 = input("You stumbled upon a large temple! Do you want to enter the red, yellow, or blue door? (Type 'R', 'Y', or 'B')" )
elif choice2 == "S":
    print("You were attacked by a trout! Game over!")
else:
    print("You were attacked by a trout! Game over!")

# Third choice
if choice3 == 'Y':
    print("You found the treasure, " + player + "! You win!!")
elif choice3 == 'R':
    print("The door locked behind you and the room burst into flames! Game over!")
elif choice3 == 'B':
    print("A family of beasts was waiting for you on the other side! Game over!")
else:
    print("Game over!")


