import time
import random

CurrentRoom = 1
XPosition = 0
YPosition = 0

RestrictedX = [random.randint(2,3), -abs(random.randint(2,3))]
RestrictedY = [random.randint(2,3), -abs(random.randint(2,3))]

Chest1Location = [0,0]
Chest2Location = [0,0]

print("X Co-ordinates:", RestrictedX[0], RestrictedX[1])
print("X Co-ordinates:", RestrictedY[0], RestrictedY[1])

PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLDTEXT = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'

def GenerateChests():
    global Chest1Location, Chest2Location
    DistanceBetweenX = RestrictedX[0] + abs(RestrictedX[1])
    DistanceBetweenY = RestrictedY[0] + abs(RestrictedY[1])
    print(DistanceBetweenX, RestrictedX, "- Distance between integers")
    print(DistanceBetweenY, RestrictedY, "- Distance between integers")

    Chest1Location[0] = RestrictedX[0] - (random.randint(1,DistanceBetweenX))
    Chest1Location[1] = RestrictedY[0] - (random.randint(1, DistanceBetweenY))
    print(Chest1Location)

    Chest2Location[0] = RestrictedX[0] - (random.randint(1,DistanceBetweenX))
    if Chest2Location[0] == Chest1Location[0]:
        GenerateChests()
        return
    Chest2Location[1] = RestrictedY[0] - (random.randint(1,DistanceBetweenY))
    print(Chest2Location)

GenerateChests()

print("Hello, Tom")

def CheckPossibleMovements():
    global YPosition, XPosition, RestrictedX, RestrictedY
    cangonorth = False
    cangoeast = False
    cangosouth = False
    cangowest = False

    if (YPosition + 1) <= RestrictedY[0]:
        cangonorth = True

    if (YPosition - 1) >= RestrictedY[1]:
        cangosouth = True

    if (XPosition + 1) <= RestrictedX[0]:
        cangoeast = True

    if (XPosition - 1) >= RestrictedX[1]:
        cangowest = True

    return cangonorth, cangoeast, cangosouth, cangowest

    print("North movement: ", cangonorth)
    print("East movement: ", cangoeast)
    print("South movement: ", cangosouth)
    print("West movement: ", cangowest)

def Movement(Direction):
    global YPosition, XPosition, RestrictedX, RestrictedY
    if str.lower(Direction) == "1":
        if CheckPossibleMovements()[0] == True:
            YPosition = YPosition + 1
    if str.lower(Direction) == "4":
        if CheckPossibleMovements()[1] == True:
            XPosition = XPosition + 1
    if str.lower(Direction) == "2":
        if CheckPossibleMovements()[2] == True:
            YPosition = YPosition - 1
    if str.lower(Direction) == "3":
        if CheckPossibleMovements()[3] == True:
            XPosition = XPosition - 1     

    print(XPosition, YPosition, "- Current Co-ordinates")
    PrintInfo()
    Movement(input("Select Next Movement"))

def PrintInfo():
    global YPosition, XPosition, RestrictedX, RestrictedY
    PossiblePaths = CheckPossibleMovements()
    print("") # For spaces between segments
    print(UNDERLINE + "Possible Movements:" + END)
    if PossiblePaths[0]: print(BOLDTEXT + "Up - 1" + END)
    if PossiblePaths[2]: print(BOLDTEXT + "Down - 2" + END)
    if PossiblePaths[3]: print(BOLDTEXT + "Left - 3" + END)
    if PossiblePaths[1]: print(BOLDTEXT + "Right - 4" + END)
    if Chest1Location[0] == XPosition and Chest1Location[1] == YPosition:
        print("") # For spaces between segments
        print(PURPLE + "Chest 1 is in this room" + END)
    if Chest2Location[0] == XPosition and Chest2Location[1] == YPosition:
        print("") # For spaces between segments
        print(PURPLE + "Chest 2 is in this room" + END)
    print("") # For spaces between segments

def PyramidPattern():
    CurrentGrid = [0,0]
    for i in range(50):
        for j in range(5):
           print("|_|", end="")
        print()

PyramidPattern()

PrintInfo()
Movement(input("Select Movement"))