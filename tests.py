import random

#  logics only
def Check(index):
    global currentTiles
    if currentTiles == [None, None]:
        currentTiles[0] = index
    elif currentTiles[0] != None and currentTiles[1] == None:
        currentTiles[1] = index
    print("checkeds", index)

order = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
random.shuffle(order)

currentTiles = [None, None]

checked = [False]*12

def checkallChecked():
    global checked
    for x in checked:
        if checked[x] == True:
            

def matchingTiles():
    global currentTiles
    if currentTiles[0] != None and currentTiles[0] == currentTiles[1]:
        # add the score
        # should be left open
        print("tiles match")
    else:
        # check if tiles were checked before and minus 5
        # close the titles
        # mark as checked
        print("tiles did not match")


def printTiles():
    global order
    print(order[:4])
    print(order[4:8])
    print(order[8:])


gameFinished = False

while gameFinished == False:
    printTiles()

