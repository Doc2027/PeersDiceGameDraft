## The objective of this game is to see who can score the highest point total
## Each player can roll an infinite amount of times

import random


dice = [1, 2, 3, 4, 5, 6]

user_roll = input(f"Enter any key to roll the dice:\n")

num_rolled = random.choices(dice, k = 3)

print(f"This is what you rolled: {num_rolled} ")

# Checks to see if all the numbers in the roll are equal to each other
def check(num_rolled):
    """
    Calculates whether one valye in a random roll
    is the same throughout the entire list

    Input:
    Your desired list

    Return:
    A boolean showing true if all the values are equal
    or false if the values are different
    """
    return num_rolled.count(num_rolled[0]) == len(num_rolled)


# if check fucntion returns as false (meaning the rolls aren't all the same)
# then gives the user a reroll message
if check(num_rolled) == False:
    print(f"If you want you can reroll for a higher score")

# Make this asking process loop infinitely as long as the player hasn't tupled out
while check(num_rolled) == False:
    reroll = input(f"Do you want to reroll? Choose [yes/no]\n") # Ask the user if they want to reroll
    if reroll == "yes":
        if num_rolled[0] == num_rolled[1]:
            #randomly rolls a single digit for the dice variable and assigns it
            # to a vairable
            replacedvalue = random.choice(dice) 
            # Changes the original value that the player chose to reroll into
            # the new value
            num_rolled[2] = replacedvalue
        elif num_rolled[1] == num_rolled[2]:
            replacedvalue = random.choice(dice)
            num_rolled[0] = replacedvalue
        elif num_rolled[0] == num_rolled[2]:
            replacedvalue = random.choice(dice)
            num_rolled[1] = replacedvalue
        else:
            # If all of the users rolls were different digits, then this gives
            # the user an netirely new roll
            num_rolled = random.choices(dice, k = 3) 
        print(f"This is your new roll: {num_rolled}")
    
    elif reroll != "yes" and reroll != "no": 
        print("Please choose yes or no as an option")
    
    elif reroll == "no":
        print(f"Player 1 scored {sum(num_rolled)} points")
        user2_roll = input(f"Player 2 press any key to roll your dice\n")
        break

# Creates a loop so that this message prints everytime the player tuples out
# Loop is needed so the message can print even if the player rerolls
while check(num_rolled) == True:
    print(f"Sorry you've tupled out! Game Over ;(. Player 2 automatically wins!")
    quit() # Ends the program

### PLAYER 2 SECTION

num_rolled2 = random.choices(dice, k = 3)

print(f"This is your roll: {num_rolled2}")

check(num_rolled2)

if check(num_rolled2) == False:
    print(f"If you want you can reroll for a higher score")

while check(num_rolled2) == False:
    reroll = input(f"Do you want to reroll? Choose [yes/no]\n")
    if reroll == "yes":
        if num_rolled2[0] == num_rolled2[1]:
            replacedvalue = random.choice(dice)
            num_rolled2[2] = replacedvalue
        elif num_rolled2[1] == num_rolled2[2]:
            replacedvalue = random.choice(dice)
            num_rolled2[0] = replacedvalue
        elif num_rolled2[0] == num_rolled2[2]:
            replacedvalue = random.choice(dice)
            num_rolled2[1] = replacedvalue
        else:
            num_rolled2 = random.choices(dice, k = 3)
        print(f"This is your new roll: {num_rolled2}")
    elif reroll != "yes" and reroll != "no":
        print("Please choose yes or no as an option")
    
    elif reroll == "no":
        print(f"Player 2 scored {sum(num_rolled2)} points")
        break

while check(num_rolled2) == True:
    print(f"Sorry you've tupled out! Game Over ;(. Player 1 automatically wins!")
    quit()

if sum(num_rolled) > sum(num_rolled2):
    print(f"Player 1 wins!")
elif sum(num_rolled) < sum(num_rolled2):
    print(f"Player 2 wins!")
elif sum(num_rolled) == sum(num_rolled2):
    print(f"Looks like we have a tie!")
else:
    raise ValueError("There seems to be an issue with calculating the scores")




