import pygame
import time
import random

pygame.init()

gameStarted = False

# window size
display_height = 600
display_width = 600

# setting the height and width for the window
win = pygame.display.set_mode((display_width, display_height))  # game display
# set Window title
pygame.display.set_caption("Memory Tiles")


# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Loading Images
cover = pygame.image.load("Cover.jpg")
sponge = pygame.image.load("Image1.jpg")
patrick = pygame.image.load("Image2.jpg")
squid = pygame.image.load("Image3.png")

# Scaling images
cover = pygame.transform.scale(cover, (100, 100))
sponge = pygame.transform.scale(sponge, (100, 100))
patrick = pygame.transform.scale(patrick, (100, 100))
squid = pygame.transform.scale(squid, (100, 100))

# Tile Cordinates
X = [0, 100, 200, 300, 0, 100, 200, 300, 0, 100, 200, 300]
Y = [0, 0, 0, 0, 100, 100, 100, 100, 200, 200, 200, 200]

# Initializing arrays to track tile actvity
revealed = [False] * 12
unlocked = [False] * 12  # tiles that matched
opened = [False] * 12  # tiles checked by user (may have failed)

# The order in which tile are arranged
order = [
    sponge,
    patrick,
    squid,
    sponge,
    patrick,
    squid,
    sponge,
    patrick,
    squid,
    sponge,
    patrick,
    squid,
]
random.shuffle(order)  # ramdomize the tiles

playTime = True  # user is able to choose tiles

run = True  # Game running
runStartScreen = True

currentTiles = [None, None]
tobeclosed = [None, None]

# score
score = 0


def changeScore(changeVal):
    global score
    score += changeVal


def revealTile(index):
    global revealed
    revealed[index] = True


def checkIfRevealed(index):
    global revealed
    return revealed[index]


# handle out of tile clicked
def ImageClicked(x, y):
    global X
    global Y

    Clicked = False
    for count in range(len(X)):
        if X[count] < x and X[count] + 100 > x:
            if Y[count] < y and Y[count] + 100 > y:
                if checkIfRevealed(count):  # check if the image was clicked before
                    ImageIndex = None
                else:
                    revealTile(count)
                    Clicked = True
                    ImageIndex = count
    return Clicked, ImageIndex


def Check(index):
    global currentTiles

    closeTiles()
    if currentTiles == [None, None]:
        currentTiles[0] = index
    elif currentTiles[0] != None and currentTiles[1] == None:
        currentTiles[1] = index
        matchingTiles()


def matchingTiles():
    global currentTiles
    tile1 = currentTiles[0]
    tile2 = currentTiles[1]

    if order[tile1] != None and order[tile1] == order[tile2]:
        changeScore(20)  # add the score
        markMatched(currentTiles[0], currentTiles[1])  # should be left open
    else:
        markNotMatched(tile1, tile2)
        # check if tiles were checked before and minus 5
        # close the titles
        # mark as checked

    emptyCurrentTiles()


def markMatched(tile1, tile2):
    global unlocked
    unlocked[tile1] = True
    unlocked[tile2] = True


def markNotMatched(tile1, tile2):
    global tobeclosed
    tobeclosed = [tile1, tile2]


def closeTiles():
    global revealed
    global tobeclosed
    tile1, tile2 = tobeclosed
    if tile1 != None and tile2 != None:
        revealed[tile1] = False
        revealed[tile2] = False
        tobeclosed = [None] * 2


def emptyCurrentTiles():
    global currentTiles
    currentTiles = [None] * 2


StartTime = time.time()
t = 5


def calcTimeLeft():
    global t
    t = 30 - (time.time() - StartTime)
    if t >= 0:
        return t
    else:
        return 0.0


# count dowm
def timerDisp():
    TimeLeft = calcTimeLeft()
    Font = pygame.font.SysFont("Comin Sans Ms", 32)
    SurfaceTime = Font.render(str(round(TimeLeft, 1)), True, black)
    win.blit(SurfaceTime, (500, 30))


def checkTimeOut():
    return t <= 0


def display_update():
    # bliting image
    global revealed
    global unlocked
    for count in range(len(X)):
        if revealed[count] == True or unlocked[count] == True:
            win.blit(order[count], (X[count], Y[count]))
        else:
            win.blit(cover, (X[count], Y[count]))
    # update display
    pygame.display.update()

def startScreen():
    global runStartScreen
    global gameStarted
    start = "Click to Start"
    win.fill(white)
    Font = pygame.font.SysFont('Comin Sans Ms', 64)#font
    SurfaceMenu = Font.render(str(start), True, black)
    win.blit(SurfaceMenu, (350,400))#bliting and pos
    run = True
    pygame.display.update()
    while runStartScreen == True:
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:#if pressed
                runStartScreen = False #stop function
                gameStarted = True

def level1():
    print('this runs')
    global run
    global playTime
    while run:
        pygame.time.delay(100)  # initial delay
        win.fill((white))
        timerDisp()  # timer display
        # score display
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and playTime:
                x, y = pygame.mouse.get_pos()
                Clicked, ImageIndex = ImageClicked(x, y)
                if ImageIndex != None:
                    Check(ImageIndex)
        display_update()

        if checkTimeOut():
            playTime = False
            win.fill((0, 0, 0))
            pygame.display.flip()

while gameStarted != True:
    startScreen()
level1()

