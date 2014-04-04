__author__ = 'Tramel Jones'

"""
Text based adventure game utilizing Twilio.
 Part of 5 Things with Raspberry Pi
  Keyboard 1,2,3, for input
   Actions reflect in the story...
"""

import twilio


def choice1():
    print(1)
def choice2():
    print(2)
def choice3():
    print(3)
def choice4():
    print(4)
choices = {'1': choice1,
       '2': choice2,
       '3': choice3,
       '4': choice4,
       }

def intro():
    intro = open("script_1.txt", "r")
    print(intro.readline())
    while True:
        if (input() == ""):
            line = intro.readline()
            if (line != ""):
                print(line)
            else:
                break

def decision1():
    while True:
        usr_choice = input("Which choice? 1.) 2.) 3.)")
        if usr_choice in choices:
            choice = choices[usr_choice]
            choice()
            break
        else:
            pass





_name = input("Enter Your Name:  ")
print("Hello, {} welcome to the game.".format(_name))
##Intro
intro()
##Decision 1
decision1()
##Decision 2
