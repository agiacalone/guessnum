#!/usr/bin/python3

import random
from optparse import OptionParser

## Set up some stuff
counter = 3
funny = 0
randnum = random.randint(1,20)

# Set up the parser args
parser = OptionParser()
parser.set_defaults(cheat=False)
parser.add_option("--i-am-a-stupid-cheater", action="store_true", dest="cheat")
(options, args) = parser.parse_args()

def funnymessage(funny):
    if funny == 3:
        return(print("It's pretty simple. Just choose a number between 1 and 20 (no decimals)."))
    elif funny == 6:
        return(print("Maybe you have a problem with your keyboard..."))
    elif funny == 9:
        return(print("Are you sure you know what a number is?"))
    elif funny == 12:
        return(print("Perhaps you're a bit slow..."))
    elif funny == 15:
        return(print("Are you just mashing keys?"))
    elif funny == 18:
        return(print("Monkeys have had a higher success rate than this..."))
    elif funny == 21:
        return(print("I think you're just toying with me."))
    elif funny == 24:
        return(print("Seriously?? It's starting to get old now."))
    elif funny == 27:
        return(print("Come on, dude. Just pick a number!!"))
    elif funny == 30:
        return(print("Ugh..."))
    elif funny == 33:
        return(print("I can't belive that I came into work today."))
    elif funny == 36:
        return(print("I don't get paid enough to put up with this, y'know."))       
    elif funny == 40:
        print("Okay! Okay! The f-ing number is %i. I give up." % (randnum))
        exit(1)
    else:
        return(print("Please choose a number"))

# Begin with the main
print("I've chosen a number between 1 and 20. What is it? You get", counter, "attempts")

# For the cheaters! (or bug testers like me)
if options.cheat is True: 
    print("*** You want to cheat. I get it. Fine...the number is: %i ***" % (randnum)) # cheater, cheater, pumpkin eater!

while counter > 0:

    while True:
        print("Guess", counter)
        try:
            guess = int(input())
            break
        except ValueError:
            funny += 1
            funnymessage(funny)
        except KeyboardInterrupt:
            print("\nFine. Just leave. See if I care...")
            exit(1)

    if (guess == randnum):
        if counter == 3:
            print("You got it on the first try! Amazing!")
        else:
            print("You got it! Congrats!")
        exit(1)
        
    elif counter >= 2:
        if guess < randnum:
            print(guess, "is too low. Try again")
        else:
            print(guess, "is too high. Try again")

    funny = 0
    counter -= 1

print("Doh! The number was %i" % (randnum))
exit(1)
