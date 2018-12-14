#CMPT 120L
#Game Project
#Ashley Wohlrab



def title():
        print("\ESCAPE FROM THE DEATH STAR: A STAR WARS GAME"
              "\n========\n")

def playerCust():
        P1.name = input("What is your name?")
        P1.gender = input("What is your gender?")
        print(" ")
        print("Hello", P1.name)
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

class Location:
        def __init__(self, room, item, message, visited):
                self.room = room
                self.item = item
                self.message = message
                self.visited = visited
                
controlRoom = Location("Control Room", "Map", "You are standing in the empty control room. There is an air duct on the south wall, doors on the east and west walls, and a rolled up scroll laying on the desk.", False)
northHallway = Location("North Hallway", None, "You find yourself back in the hallway you exited before.", False)
armory = Location("Armory", "Tool", "You arrive in a small armory. Surrounding you are numerous weapons and shields. There's a strange looking tool on the floor ahead of you.", False)
airDuct = Location("Air Duct", None, "You pry the vent from the duct. It's dark inside, but you can just make out the path in front of you. There is another vent straight ahead.", False)
uniformCloset = Location("Uniform Closet", None, "You pry open the vent, and find yourself inside a storage closet containing Storm Trooper uniforms and a single exit door on the south wall.", False)
southHallway = Location("South Hallway", None, "You find a hallway with Storm Troopers heading East down the hall. There is another corridor in the Eastern direction of the hallway.", False)
foodCloset = Location("Food Closet", "Can", "You find yourself inside a food storage room. The walls are lined with cans and snacks.", False)
hangar = Location("Hangar", None, "You find your way to the ship's vehicle hangar. There are Rebels and Storm-troopers fighting closeby, and an empty tie fighter on the east wall.", False)
medicalBay = Location("Medical Bay", "Med-pak", "The room is filled with medical tools and has a large medical table in the center. There are med-paks lying on a nearby table.", False)
library = Location("Library", "Book", "There are books lining the walls. You notice a leather-bound book on a nearby shelf. It seems to have been recently opened.", False)


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
        if P1.location.visited == False:
                P1.score = P1.score + 5
                P1.location.visited = True
        print(scoreMessage + str(P1.score))


def printCount():
        #global count
        print("Moves made: " + str(P1.moves))

def printItem(playerLocation):
        print("Item located at this location: " + str(P1.location.item) + ".")

def printMap():
        print("        ----------------------------------------")
        print("        |      North Hallway      | Medical Bay |")
        print("        -----------------------------------------")
        print("             |             |       ")
        print("     --------|Control Room |-------")
        print("    | Armory |             |Library|")
        print("     -------------------------------")
        print("             | Air Duct |            ")
        print("             ----------------      ")
        print("             |Uniform Closet|      ")
        print(" -------------------------------------")
        print(" |Food Closet| North Hallway | Hangar |")
        print(" --------------------------------------")


def printLocation():
        print("Current Location: " + str(P1.location.room) + ".")
             
def playerUpdate(playerLocation):
        printLocation()
        printScore(playerLocation)
        printCount()
        printItem(playerLocation)

def useTool():
        print("Uses Tool")
        

North=""
East=""
West=""
South=""


#Create function for each locale

def ControlRoom():
        global North
        North = "North Hallway"
        global East
        East = "Library"
        global West
        West = "Armory"
        global South
        South = "Air Duct"
        P1.location = controlRoom
        playerUpdate(P1.location)
        print(P1.location.message)
        

def NorthHallway():
        global North
        North = ""
        global East
        East = "Medical Bay"
        global West
        West = ""
        global South
        South = "Control Room"
        P1.location = northHallway
        playerUpdate(P1.location)
        print(P1.location.message)
       

def Armory():
        global North
        North = ""
        global East
        East = "Control Room"
        global West
        West = ""
        global South
        South = ""
        P1.location = armory
        playerUpdate(P1.location)
        print(P1.location.message)



def AirDuct():
        global North
        North = "Control Room"
        global East
        East = ""
        global West
        West = ""
        global South
        South = "Uniform Closet"
        P1.location = airDuct
        playerUpdate(P1.location)
        print(P1.location.message)


def UniformCloset():
        global North
        North = "Air Duct"
        global East
        East = ""
        global West
        West = ""
        global South
        South = "South Hallway"
        P1.location = uniformCloset
        playerUpdate(P1.location)
        print(P1.location.message)


def SouthHallway():
        global North
        North = "Uniform Closet"
        global East
        East = "Hangar"
        global West
        West = "Food Closet"
        global South
        South = ""
        P1.location = southHallway
        playerUpdate(P1.location)
        print(P1.location.message)

def FoodCloset():
        global North
        North = ""
        global East
        East = "South Hallway"
        global West
        West = ""
        global South
        South = ""
        P1.location = foodCloset
        playerUpdate(P1.location)
        print(P1.location.message)


def Hangar():
        global North
        North = ""
        global East
        East = ""
        global West
        West = "South Hallway"
        global South
        South = ""
        P1.location = hangar
        playerUpdate(P1.location)
        print(P1.location.message)


def MedicalBay():
        global North
        North = ""
        global East
        East = ""
        global West
        West = "North Hallway"
        global South
        South = ""
        P1.location = medicalBay
        playerUpdate(P1.location)
        print(P1.location.message)


def Library():
        global North
        North = ""
        global East
        East = ""
        global West
        West = "Control Room"
        global South
        South = ""
        P1.location = library
        playerUpdate(P1.location)
        print(P1.location.message)


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
                        elif East == "Medical Bay":
                                MedicalBay()
                        elif East == "Library":
                                Library()
                        else:
                                print("You cannot go east here.")
                elif input == "west":
                        if West == "Armory":
                                Armory()
                        elif West == "South Hallway":
                                SouthHallway()
                        elif West == "Food Closet":
                                FoodCloset()
                        elif West == "North Hallway":
                                NorthHallway()
                        elif West == "Control Room":
                                ControlRoom()
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
                        print("The valid commands are: north, south, east, west, help, map, take, and quit.")
                elif input == "quit":
                        break
                elif input == "map":
                        hasMap = False
                        for i in range(0, len(P1.inventory)):
                                if P1.inventory[i] == "Map":
                                        hasMap = True;
                                        printMap()
                                        break
                        if not hasMap:
                                print("You do not have the map")
                elif input == "take":
                        if P1.location.item != None:
                                P1.inventory.append(P1.location.item)
                                P1.location.item = None
                        elif P1.location.item == None:
                                print("There is no item to take here")
                elif input == "inventory":
                        print(P1.inventory)
                elif input.split(" ")[0] == "use":
                        if len(input.split(" ")) > 1 and input.split(" ")[1] == "map":
                                if P1.inventory.count("Map") > 0:
                                        printMap()
                                else:
                                        print("You do not have this item.")
                        elif len(input.split(" ")) > 1 and input.split(" ")[1] == "tool":
                                if P1.inventory.count("Tool") > 0:
                                        useTool()
                                else:
                                        print("You do not have this item.")
                        elif len(input.split(" ")) > 1 and input.split(" ")[1] == "can":
                                if P1.inventory.count("Can") > 0:
                                        P1.score = P1.score +10
                                        print("You consume the delicious canned food and your score goes up by ten points!")
                                else:
                                        print("You do not have this item.")
                        elif len(input.split(" ")) > 1 and input.split(" ")[1] == "med-pak":
                                if P1.inventory.count("Med-pak") > 0:
                                        P1.score = P1.score + 10
                                        print("You heal previous battle wounds and your score increases by 10 points.")
                                else:
                                        print("You do not have this item.")
                        elif len(input.split(" ")) > 1 and input.split(" ")[1] == "book":
                                if P1.inventory.count("Book") > 0:
                                        P1.score = P1.score + 10
                                        print("Reading about battle strategies, you improve your stealthiness and increase your points by 10.")   
                                else:
                                        print("You do not have this item.")
                        
                else:
                              print("The command you have entered is invalid.")
                              continue
                P1.moves = P1.moves + 1
                if P1.moves == 18:
                        print("You have been caught! Game Over!")
                        break
                else:
                        continue


#In current state of game, player must quit when reaching "hangar" for dialogue to flow.

class Player:
        def __init__(self, name, gender, score,location, moves, inventory):
                self.name = name
                self.gender = gender
                self.score = score
                self.location = location
                self.moves = moves
                self.inventory = inventory

P1 = Player("", "", 0, controlRoom, 0, [])


#player = {
        #"Player Name": "person",
        #"Player Gender": "gender",
        #"Player Score": 0,
        #"Player Location": locNames[0],
        #"Moves Made": -1,
        #"Inventory": []
        #}

              
#end the game and show credits
def EndGame():
        print("Getting into the tie fighter, you turn the key and start the engine. Flying away from the vessel, you look out into space and feel hopeful for the future of the galaxy. Game over!")
        print("\nCopyright (c) 2018 Ashley Wohlrab, Ashley.Wohlrab1@marist.edu")

       
def main():
        GameStart()
        keepPlaying = True
        while keepPlaying:
                playGame()
                userInput = input("Would you like to play again? (Y/N)")
                if userInput == "N":
                        keepPlaying = False  
        EndGame()
main()
