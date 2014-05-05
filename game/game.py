__author__ = 'Tramel Jones'

"""
Text based adventure game utilizing Twilio.
 Part of 5 Things with Raspberry Pi
  Keyboard 1,2,3, for input
   Actions reflect in the story...
"""
import SendMessage
class game(object):

    def intro(self):
        self.readScript("script_1.txt")
    def Act2(self):
        self.readScript("script_2.txt")
    def Act3(self):
        self.readScript("script_3.txt")

    def choice1(self):
        self.readScript("script_1a.txt")
    def choice2(self):
        self.readScript("script_1b.txt")
    def choice3(self):
        self.readScript("script_1c.txt")
    def choice4(self):
        self.readScript("script_2a.txt")
    def choice5(self):
        self.readScript("script_2b.txt")
    def choice6(self):
        self.readScript("script_2c.txt")
    def choice7(self):
        self.readScript("script_2d.txt")
    def choice8(self):
        self.readScript("script_2e.txt")
    def choice9(self):
        self.readScript("script_2f.txt")

    def __init__(self):

       self.choices = {'1': self.choice1,
       '2': self.choice2,
       '3': self.choice3,
       }
       self.choices_2 = {'1': self.choice4,
                         '2': self.choice5,
                          '3': self.choice6
       }
       self.choices_3 = {'1': self.choice7,
                         '2': self.choice8,
                          '3': self.choice9
       }
       
       self.run()


    def readScript(self, script):
        text = open(script, "r")
        print(text.readline())
        while True:
            if (input() == ""):
                line = text.readline()
                if (line != ""):
                    print(line)
                else:
                    break



    #Drink
    def decision1(self):
        while True:
            usr_choice = input("Which choice?\n 1.)\"What the hell...\" (Take Drink)\n 2.) \"Say no to drugs.\"(Don't Take Drink) \n3.) ...")
            if usr_choice in self.choices:
                choice = self.choices[usr_choice]
                choice()
                break
            else:
                pass
    #Smoke
    def decision2(self):
        while True:
            usr_choice = input("Which choice?\n 1.)\"What the hell...\" (Take Puff of Smoke)\n 2.) \"Say no to drugs.\"(Don't Take Hit) \n3.) ...")
            if usr_choice in self.choices:
                choice = self.choices_2[usr_choice]
                choice()
                break
            else:
                pass
    #Break-in
    def decision3(self):

        while True:
            usr_choice = input("Which choice?\n 1.)Climb Window... \n 2.) Try the airduct \n3.) Try the door")
            if usr_choice in self.choices:
                choice = self.choices_3[usr_choice]
                choice()
                if usr_choice == "2":
                    break #Break only if we are at right choice.
            else:
                pass
    #End

    def run(self):
        self._name = input("Enter Your Name:  \n")
        print("Hello, {} welcome to the game.".format(self._name))
        ##Intro
        self.intro()
        ##Decision 1 Drink, Act 1
        self.decision1()
        ##Ask for phone number End of Act 1
        while True:
            self._number = input("Enter Your Phone Number:  (##########)\n")
            if len(self._number) == 10:
                self._num = self._number.strip()
                #Send Text Message
                messenger = SendMessage.SendMessage()
                messenger.setmessage(self._num, "Hello " + self._name + " I will contact you soon.")
                break
            else:
                pass
        ##Act 2, Car Ride
        self.Act2()
        #Smoke
        self.decision2()
        ##Break-in
        self.decision3()
        ##End of Act 2

        messenger.setmessage(self._num, "1876")
        ##Send text #2.

        while True:
            self._code = input("CODE:  ")
            if self._code == "1876":
                break
            else:
                pass
        self.Act3()
        ##Act 3 End
        