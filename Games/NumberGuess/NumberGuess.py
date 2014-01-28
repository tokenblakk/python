import random

class Game(object):

    def __init__(self):
        print "Init."
        self.num = random.randint(1,100)
        #choose a number at the beginning of game
        self.counter = 0
        #get ready to count the guesses
        print "Done."
        
    def run(self):
        print
        print "Welcome and Hello!"
        print "We are now in the Psychic Zone"
        print "This is a test of your extrasensory abilities. "
        print
        print "Guess a number from 1-100"
        print
        print "It shouldn't take that long..."
        while 1:
            guess = input("Guess? ")
            self.counter += 1
            if guess == self.num:
                print "You Win!"
                print "It took you " + str(self.counter) + " tries!"
                if self.counter > 5:
                    print "You should work on your ESP"
                elif self.counter <=2 :
                    print "You may just be psychic after all!"
                else:
                    print "Great Job!"
                '''if input("Play Again? (y/n) ") == "n":'''
                break
            if guess > self.num:
                print "A little lower."
            if guess < self.num:
                print "A little higher."
        
    
game = Game()
game.run()
