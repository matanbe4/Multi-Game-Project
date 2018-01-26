import pygame
import time
import random
from commonFunctions import *


#Loading images.
moveFont = pygame.font.SysFont('comicsansms',30,1)
board = pygame.image.load('Images/board.jpg')
p1 = pygame.image.load('Images/p1.jpeg')#players images
p2 = pygame.image.load('Images/p2.jpeg')
c1 = pygame.image.load('Images/c1.jpg')#dice images
c2 = pygame.image.load('Images/c2.jpg')
c3 = pygame.image.load('Images/c3.jpg')
c4 = pygame.image.load('Images/c4.jpg')
c5 = pygame.image.load('Images/c5.jpg')
c6 = pygame.image.load('Images/c6.jpg')
SnLIns = pygame.image.load('Images/SnL instructions.jpeg')
SnLMenu = pygame.image.load('Images/SnL Menu.png')
SnLFileName = 'S And L Recordes.txt'


square = 60 #Size of game board tiles - square * square.
#res = 0
right = 1 #Directions.
left = -1
p2Turn = False
p1Location = [0, square * 9] #The initial location of p1.
p2Location = [square//2, square * 19//2] #The initial location of p2.
diceLocation = [650,120]


SLlist = [ #List of Snakes/Ladders.
    [[240,300],[180,540]], #4th snake.
    [[360,540],[480,360]], #7th ladder.
    [[480,180],[420,420]], #28th snake.
    [[0,420],[0,360]], #21st ladder.
    [[180,180],[120,360]], #38th snake.
    [[240,120],[180,300]], #44th snake.
    [[420,180],[360,60]], #88th ladder.
    [[60,180],[0,0]], #62nd ladder.
    [[120,120],[120,0]], #78th ladder.
    [[180,0],[180,60]], #84th snake.
    [[480,120],[420,0]], #72nd ladder.
    [[360,240],[300,360]] #35th snake.
    ]

def displayMenu(): #Function that display the connect 4 main menu.
    showIns(SnLIns)
    gameDisplay.blit(SnLMenu,(0,0)) #Display the menu image.
    pygame.display.update()
    while True:
        cur = pygame.mouse.get_pos() #Getting the mouse position.
        curClick = pygame.mouse.get_pressed() #Getting the pressed mouse button.
        if 300 <= cur[0] <= 300 + buttonW and 50 <= cur[1] <= 50 + buttonH: #If the mouse is in the borders of the wanted box
            if curClick[0] == 1: #Check if it was pressed
                return
           
        elif 300 <= cur[0] <= 300 + buttonW and 470 <= cur[1] <= 470 + buttonH: #If the mouse is in the borders of the wanted box
            if curClick[0] == 1: #Check if it was pressed
                return True #If it was, it means the user wanted to go back to the main menu.
                
        elif 45 <= cur[0] <= 45 + buttonW and 470 <= cur[1] <= 470 + buttonH: #If the mouse is in the borders of the wanted box
            if curClick[0] == 1: #Check if it was pressed
                displayRecords(SnLFileName)
                return True
        for event in pygame.event.get(): #Closing the game
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return True
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
#Function that displays the dice's roll and finally the steps.
def diceDisplay():
    val = random.randint(1,6)#The amount of steps.
    x = []#List of the roll.
    for _ in range(8):
        x.append(random.randint(1,6)) #Random values for the roll images.
    for a in x: #Roll display loop.
        if a == 1:
            gameDisplay.blit(c1,diceLocation)
        elif a == 2:
            gameDisplay.blit(c2,diceLocation)
        elif a == 3:
            gameDisplay.blit(c3,diceLocation)
        elif a == 4:
            gameDisplay.blit(c4,diceLocation)
        elif a == 5:
            gameDisplay.blit(c5,diceLocation)
        elif a == 6:
            gameDisplay.blit(c6,diceLocation)
        pygame.display.update()
        clock.tick(8)
    displayMessage("Movement:",lightBlue,[620,80], moveFont)
    if val == 1:#The actual steps.
        gameDisplay.blit(c1,diceLocation)
    elif val == 2:
        gameDisplay.blit(c2,diceLocation)
    elif val == 3:
        gameDisplay.blit(c3,diceLocation)
    elif val == 4:
        gameDisplay.blit(c4,diceLocation)
    elif val == 5:
        gameDisplay.blit(c5,diceLocation)
    elif val == 6:
        gameDisplay.blit(c6,diceLocation)
    pygame.display.update()
    clock.tick(1)
    gameDisplay.fill(white)   
    return val

#Display of the regular objects which is the board, p1 and p2.
def display():
    gameDisplay.blit(backGround,(0,0))
    gameDisplay.blit(board,(0,0))
    gameDisplay.blit(p1,p1Location)
    gameDisplay.blit(p2,p2Location)
    pygame.display.update()  
    
def movementDirection(playerLoc): 
    return left if (playerLoc[1] % (square * 2) < square) else right #Returns the direction of the movement at every row.

def snakeOrLadder(playerLoc):
    newPos = False
    secondPlayer = False 
    if playerLoc[0] % square != 0: #If the player is the second.
        playerLoc[0]-= square//2
        playerLoc[1]-= square//2
        secondPlayer = True
    for loc in SLlist:
        if loc[0] == playerLoc:
            clock.tick(10)
            x,y = loc[1]
            newPos = [x,y]
            break
    if secondPlayer == True: #Returns the second player to its location.               
        playerLoc[0] += square//2
        playerLoc[1] += square//2
        if newPos != False:
            newPos[0] += square//2
            newPos[1] += square//2
    return newPos
    
def isWin(playerLoc):
    if 0 <= playerLoc[0] < square and 0 <= playerLoc[1] < square:
        return True
    return False

def movement(res, playerLoc):
    direction = movementDirection(playerLoc)
    for _ in range(res):
        if 0 <= playerLoc[0] + square * direction < 600:#Between row borders.
            playerLoc[0] += square * direction
        else: #Out of row borders.
            direction *= -1
            playerLoc[1] -= square
        if 0 <= playerLoc[0] < square and 0 <= playerLoc[1] < square and _ != res - 1:#Stepped on FINISH but not in the last step.
            direction = right
        display()
        clock.tick(10)
        
def initBoard():
    global p1Location, p2Location
    p1Location = [0, square * 9] #The initial location of p1.
    p2Location = [square//2, square * 19//2] #The initial location of p2.
    
def gameLoop(userName1,userName2):
    global p1Location, p2Location, p2Turn
    mainMenu = displayMenu()
    if mainMenu:
        return False
    win = False
    initBoard()#Initial the players on the 0 square.
    turn = p1Location#First turn.
    #GAME LOOP
    while True:
        display()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    res = diceDisplay()
                    movement(res, turn)
                    newPos = snakeOrLadder(turn)
                    if newPos != False:
                        x,y = newPos
                        turn[0],turn[1] = x,y
                    if isWin(turn):
                        display()
                        if turn == p1Location:
                            UpdateRecords(userName1, SnLFileName)
                            victory("Victory! " + userName1)
                            return True
                        else:
                            UpdateRecords(userName2, SnLFileName)
                            victory("Victory! " + userName2)
                            return True
                    if p2Turn == False:
                        turn = p2Location
                        p2Turn = True
                    else:
                        turn = p1Location
                        p2Turn = False
                break
            display()                
        pygame.display.update()
