#CMPT 120L
#Game Project
#Ashley Wohlrab



def title():
        print("\ESCAPE FROM THE DEATH STAR: A STAR WARS GAME"
              "\n========\n")

def playerCust():
        person = input("What is your name?")
        gender = input("What is your gender?")
        print(" ")
        print("Hello", person)
        print("The force is strong with you. Good luck!")
        print(" ")

# show game introduction
#for reference, this game takes place between Episodes 3 and 4
StarWarsMessage="A long time ago in a galaxy far, far away..."
introductionMessage = "You are a rebel spy who has snuck aboard the Death Star in search of intel on Darth Vader's next attack. You are sure that you'll be able to take this information back to the Rebel Alliance and help destroy the Sith, who are rising to power in their creation of the Galactic Empire. As you're sneaking through the corridors of the massive space-station, the alarm sounds. You duck into a dark corner just outside the control room as dozens of storm-troopers run toward the main entrance of the ship. Now is your chance! You take this opportunityto race into the empty control room, and gather the intel you need. The Death Star is under attack, and now that you have what you came for, it's time to find a strategic escape!"

def GameStart():
        title()
        playerCust()
        input(StarWarsMessage)
        input(introductionMessage)
        
#store locales in list
locales=["You are standing in the empty control room. There is an air duct on the south wall, a door on the west wall, and strange looking tool laying on the desk.",
         "Using the tool, you pry the vent from the duct. It's dark inside, but you can just make out the path in front of you. There is another vent straight ahead.",
         "You use the tool to pry open the vent, and find yourself inside a storage closet containing Storm Trooper uniforms and a single exit door on the south wall.",
         "Through the door you find a hallway with Storm Troopers heading West down the hall. There is another corridor in the Eastern direction of the hallway.",
         "You find yourself inside a food storage room. The walls are lined with cans and snacks.",
         "Following the crowd, you find your way to the ship's vehicle hangar. There are Rebels and Storm-troopers fighting closeby, and an empty tie fighter on the east wall."]

