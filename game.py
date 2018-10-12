#CMPT 120L
#Project Version .1
#Ashley Wohlrab
# 17 September 2018

def title():
        print("\ESCAPE FROM THE DEATH STAR: A STAR WARS GAME"
              "\n========\n")
title()

#player customization
def playerCust():
        person = input("What is your name?")
        gender = input("What is your gender?")
        print(" ")
        print("Hello", person)
        print("The force is strong with you. Good luck!")
        print(" ")

playerCust()

#store locales in list
locales=[ControlRoom, AirDuct, Closet, Corridor, Hangar, Space]
print("Locales are", locales)
        
# show game introduction
#for reference, this game takes place between Episodes 3 and 4
StarWarsMessage="A long time ago in a galaxy far, far away..."
introductionMessage = "You are a rebel spy who has snuck aboard the Death Star in search of intel on Darth Vader's next attack. You are sure that you'll be able to take this information back to the Rebel Alliance and help destroy the Sith, who are rising to power in their creation of the Galactic Empire. As you're sneaking through the corridors of the massive space-station, the alarm sounds. You duck into a dark corner just outside the control room as dozens of storm-troopers run toward the main entrance of the ship. Now is your chance! You take this opportunity to race into the empty control room, and gather the intel you need. The Death Star is under attack, and now that you have what you came for, it's time to find a strategic escape!"

input(StarWarsMessage)

input(introductionMessage)

scoreMessage = "Your score is "
inputMessage = "\n<Press Enter to Continue...>\n"
score = 0;

# this function shows the current score
def printScore():
	print(scoreMessage + str(score))

# prompt the user
input(inputMessage)

# show the current location
ControlRoom="You are standing in the empty control room. You hear the footsteps of stormtroopers outside the door. There is an air duct on the wall, a back door to the room, and strange looking tool laying on the desk."

input(ControlRoom)

# show the current score
printScore()

# prompt the user
input(inputMessage)

# show the current location
AirDuct="You pick up the tool and walk to the air duct. Using the tool, you pry the vent from the duct. It's dark inside, but you can just make out the path in front of you."

input(AirDuct)

# update the score
score = score + 5
printScore()

# same as above
input(inputMessage)

# same as above
Closet="You take a right turn, and then a left. You come across another vent, leading into what looks like a small, empty room. You use the tool to pry open the vent, then drop down into a storage closet"

input(ClosetMessage)

# same as above
score = score + 5
printScore()

# again...
input(inputMessage)

# again...
Corridor="Inside you find storm-trooper uniforms! You grab a uniform and throw it on, opening the door and blending into the crowd of stormtroopers outside."

input(Corridor)

# again...
score = score + 5
printScore()

# yet again...
input(inputMessage)

# yet again...
Hangar="You take a left turn, then a right and find your way to the ship's vehicle hangar. There are Rebels and Storm-troopers fighting closeby, but you jump into a nearby tie fighter."

input(Hangar)

# yet again...
score = score + 5
printScore()

# one last time...
input(inputMessage)

# show game ending
Space="You turn the key and start the engine, flying away from the vessel. You look out into space and feel hopeful for the future of the galaxy. Game over!"

input(Space)

# show credits
print("\nCopyright (c) 2018 Ashley Wohlrab, Ashley.Wohlrab1@marist.edu")
