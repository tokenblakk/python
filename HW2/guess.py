__author__ = 'Tramel Jones'
"""
Guessing game
"""

import random
smaller = input("Enter the smaller number:")
larger = input("Enter the larger number:")
myNumber = random.randint(int(smaller),int(larger))
count = 0
while count <6:
    count+= 1
    userNumber =int(input("Enter your guess:"))
    if userNumber < myNumber:
        print ("Too small")
    elif userNumber >myNumber:
        print ("Too large")
    else:
        print ("You've got it in",count,"tries!")
        break
if count >= 6:
    print("You're a big loser, I see you've been gaining weight.\nMaybe you should hit the gym because you're not cut out for brainwork.")