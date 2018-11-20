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
         "Going through the North door, you find yourself back in the hallway you came from.",
         "By going through the West door, you arrive in a small armory. Surrounding you are numerous weapons and shields.",
         "Using the tool, you pry the vent from the duct. It's dark inside, but you can just make out the path in front of you. There is another vent straight ahead.",
         "You use the tool to pry open the vent, and find yourself inside a storage closet containing Storm Trooper uniforms and a single exit door on the south wall.",
         "Through the door you find a hallway with Storm Troopers heading East down the hall. There is another corridor in the Eastern direction of the hallway.",
         "You find yourself inside a food storage room. The walls are lined with cans and snacks.",
         "Following the crowd, you find your way to the ship's vehicle hangar. There are Rebels and Storm-troopers fighting closeby, and an empty tie fighter on the east wall."]

locNames=["Control Room", "North Hallway", "Armory", "Air Duct", "Uniform Closet", "South Hallway", "Food Closet", "Hangar"] 

hasBeen=[False, False, False, False, False, False, False, False]

#global loc
#loc = locNames[0]

#Score and Input messages
scoreMessage = "Your score is "
inputMessage = "\n<What do you want to do next?>\n"

def userInput():
        givenInput = input(inputMessage).lower()
        return givenInput

#score=0
#global count
#count = -1

def printScore(playerLocation):
        #global score
        if hasBeen[playerLocation] == False:
                player["Player Score"]=player["Player Score"]+5
                hasBeen[playerLocation] = True
        print(scoreMessage + str(player["Player Score"]))


def printLocation():
        if locales[0]:
                location = "Control Room"
        elif locales[1]:
                location = "North Hallway"
        elif locales[2]:
                location = "Armory"
        elif locales[3]:
                location = "Air Duct"
        elif locales[4]:
                location = "Uniform Closet"
        elif locales[5]:
                location = "South Hallway"
        elif locales[6]:
                location = "Food Closet"
        elif locales[7]:
                location = "Hangar"
        print("Current Location: " + str(player["Player Location"]) + ".")


def printCount():
        #global count
        player["Moves Made"] = player["Moves Made"] + 1
        print("Moves made: " + str(player["Moves Made"]))

def printMap():
        print("        ---------------------------")
        print("        |      North Hallway      |")
        print("        ---------------------------")
        print("             |             |       ")
        print("     --------|Control Room |       ")
        print("    | Armory |             |       ")
        print("     -----------------------       ")
        print("             | Air Duct |            ")
        print("             ----------------      ")
        print("             |Uniform Closet|      ")
        print(" -------------------------------------")
        print(" |Food Closet| North Hallway | Hangar |")
        print(" --------------------------------------")
        
             

def playerUpdate(playerLocation):
        printLocation()
        printScore(playerLocation)
        printCount()
        

North=""
East=""
West=""
South=""


#Create function for each locale

def ControlRoom():
        global North
        North = "North Hallway"
        global East
        East = ""
        global West
        West = "Armory"
        global South
        South = "Air Duct"
        global loc
        player["Player Location"] = locNames[0]
        playerUpdate(0)
        print(locales[0])

def NorthHallway():
        global North
        North = ""
        global East
        East = ""
        global West
        West = ""
        global South
        South = "Control Room"
        global loc
        player["Player Location"] = locNames[1]
        playerUpdate(1)
        print(locales[1])

def Armory():
        global North
        North = ""
        global East
        East = "Control Room"
        global West
        West = ""
        global South
        South = ""
        global loc
        player["Player Location"] = locNames[2]
        playerUpdate(2)
        print(locales[2])


def AirDuct():
        global North
        North = "Control Room"
        global East
        East = ""
        global West
        West = ""
        global South
        South = "Uniform Closet"
        global loc
        player["Player Location"] = locNames[3]
        playerUpdate(3)
        print(locales[3])

def UniformCloset():
        global North
        North = "Air Duct"
        global East
        East = ""
        global West
        West = ""
        global South
        South = "South Hallway"
        global loc
        player["Player Location"] = locNames[4]
        playerUpdate(4)
        print(locales[4])

def SouthHallway():
        global North
        North = "Uniform Closet"
        global East
        East = "Hangar"
        global West
        West = "Food Closet"
        global South
        South = ""
        global loc
        player["Player Location"] = locNames[5]
        playerUpdate(5)
        print(locales[5])

def FoodCloset():
        global North
        North = ""
        global East
        East = "South Hallway"
        global West
        West = ""
        global South
        South = ""
        global loc
        player["Player Location"] = locNames[6]
        playerUpdate(6)
        print(locales[6])

def Hangar():
        global North
        North = ""
        global East
        East = ""
        global West
        West = "South Hallway"
        global South
        South = ""
        global loc
        player["Player Location"] = locNames[7]
        playerUpdate(7)
        print(locales[7])


def playGame():
        Game = True
        ControlRoom()
        while Game:
                input = userInput()
                if input == "north":
                        if North == "North Hallway":
                                NorthHallway()
                        elif North == "Control Room":
                                ControlRoom()
                        elif North == "Air Duct":
                                AirDuct()
                        elif North == "Uniform Closet":
                                UniformCloset()
                        
                        else:
                                print("You cannot go north here.")
                elif input == "east":
                        if East == "Control Room":
                                ControlRoom()
                        elif East == "South Hallway":
                                SouthHallway()
                        elif East == "Hangar":
                                Hangar()
                       
                        else:
                                print("You cannot go east here.")
                elif input == "west":
                        if West == "Armory":
                                Armory()
                        elif West == "South Hallway":
                                SouthHallway()
                        elif West == "Food Closet":
                                FoodCloset()
                       
                        else:
                                print("You cannot go west here.")
                elif input == "south":
                        if South == "Control Room":
                                ControlRoom()
                        elif South == "Air Duct":
                                AirDuct()
                        elif South == "Uniform Closet":
                                UniformCloset()
                        elif South == "South Hallway":
                                SouthHallway()
                        else:
                                print("You cannot go south here.")
                elif input == "help":
                        print("The valid commands are: north, south, east, west, help, map, and quit.")
                elif input == "quit":
                        break
                elif input == "map":
                        printMap()
                else:
                              print("The command you have entered is invalid.")
                              continue
                if player["Moves Made"] == 15:
                        print("You have been caught! Game Over!")
                        break
                else:
                        continue

#In current state of game, player must quit when reaching "hangar" for dialogue to flow.

player = {
        "Player Name": "person",
        "Player Gender": "gender",
        "Player Score": 0,
        "Player Location": locNames[0],
        "Moves Made": -1
        }

#end the game and show credits
def EndGame():
        print("Getting into the tie fighter, you turn the key and start the engine. Flying away from the vessel, you look out into space and feel hopeful for the future of the galaxy. Game over!")
        print("\nCopyright (c) 2018 Ashley Wohlrab, Ashley.Wohlrab1@marist.edu")

       
def main():
        GameStart()
        playGame()
        EndGame()
main()
