import pygame
import time
import random
from commonFunctions import *


#LOCAL VARIABLES:
xMove = 90#x jumps.
yMove = 80#y jumps.
xS = 13#x Start.
yS = 44#y Start.
E = 0#Empty.
F1 = 1#Full by p1.
F2 = 2#Full by p2.

win = False #When a player wins, win will be changed to True.
vsCom = False #From User's Choice.
WIDTH = 7 #Number of coins in a row.
HEIGHT = 6 #Number of coins in a col.
connect4FileName = 'connect 4 Recordes.txt'

#Loading images.
board = pygame.image.load('Images/board.png')#Game table.
connect4Menu = pygame.image.load('Images/Connect 4 Menu.png')
connect4Ins = pygame.image.load('Images/connect 4 instructions.jpeg')
p1 =[F1, pygame.image.load('Images/red.png')] #Player1 image.
p2 =[F2, pygame.image.load('Images/yellow.png')] #Player2 image.
turn = p1 #By default player1 starts first.

startPos = [xS + xMove * 3, yS]
FoE = [#Game matrix.
    [[xS,yS+yMove,E],[xS+xMove,yS+yMove,E],[xS+xMove*2,yS+yMove,E],[xS+xMove*3,yS+yMove,E],[xS+xMove*4,yS+yMove,E],[xS+xMove*5,yS+yMove,E],[xS+xMove*6,yS+yMove,E]],
    [[xS,yS+yMove*2,E],[xS+xMove,yS+yMove*2,E],[xS+xMove*2,yS+yMove*2,E],[xS+xMove*3,yS+yMove*2,E],[xS+xMove*4,yS+yMove*2,E],[xS+xMove*5,yS+yMove*2,E],[xS+xMove*6,yS+yMove*2,E]],
    [[xS,yS+yMove*3,E],[xS+xMove,yS+yMove*3,E],[xS+xMove*2,yS+yMove*3,E],[xS+xMove*3,yS+yMove*3,E],[xS+xMove*4,yS+yMove*3,E],[xS+xMove*5,yS+yMove*3,E],[xS+xMove*6,yS+yMove*3,E]],
    [[xS,yS+yMove*4,E],[xS+xMove,yS+yMove*4,E],[xS+xMove*2,yS+yMove*4,E],[xS+xMove*3,yS+yMove*4,E],[xS+xMove*4,yS+yMove*4,E],[xS+xMove*5,yS+yMove*4,E],[xS+xMove*6,yS+yMove*4,E]],
    [[xS,yS+yMove*5,E],[xS+xMove,yS+yMove*5,E],[xS+xMove*2,yS+yMove*5,E],[xS+xMove*3,yS+yMove*5,E],[xS+xMove*4,yS+yMove*5,E],[xS+xMove*5,yS+yMove*5,E],[xS+xMove*6,yS+yMove*5,E]],
    [[xS,yS+yMove*6,E],[xS+xMove,yS+yMove*6,E],[xS+xMove*2,yS+yMove*6,E],[xS+xMove*3,yS+yMove*6,E],[xS+xMove*4,yS+yMove*6,E],[xS+xMove*5,yS+yMove*6,E],[xS+xMove*6,yS+yMove*6,E]]
    ]

def displayMenu(): #Function that displays the connect 4 main menu.
    global vsCom #Boolean variable.
    mainMenu = showIns(connect4Ins)
    if mainMenu:
        return True
    gameDisplay.blit(connect4Menu,(0,0)) #Displays the menu image.
    pygame.display.update()
    while True:
        cur = pygame.mouse.get_pos() #Getting the mouse position.
        curClick = pygame.mouse.get_pressed() #Getting the pressed mouse button.
        if 300 <= cur[0] <= 300 + buttonW and 50 <= cur[1] <= 50 + buttonH: #If the mouse is in the borders of the wanted box
            if curClick[0] == 1: #Check if it was clicked.
                vsCom = False #Turn off VS COM mode.
                return
            
        elif 300 <= cur[0] <= 300 + buttonW and 200 <= cur[1] <= 200 + buttonH: #If the mouse is in the borders of the wanted box
            if curClick[0] == 1: #Check if it was clicked.
                vsCom = True #Turn on VS COM mode.
                return
           
        elif 300 <= cur[0] <= 300 + buttonW and 470 <= cur[1] <= 470 + buttonH: #If the mouse is in the borders of the wanted box
            if curClick[0] == 1: #Check if it was clicked.
                return True #back to the main menu.
                
        elif 45 <= cur[0] <= 45 + buttonW and 470 <= cur[1] <= 470 + buttonH: #If the mouse is in the borders of the wanted box
            if curClick[0] == 1: #Check if it was clicked.
                displayRecords(connect4FileName)
                return True
                
        for event in pygame.event.get(): #Closing the game.
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                mainMenu()
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()

def display():
    gameDisplay.blit(backGround,(0,0))
    for i in FoE:
        for j in i:
            if j[2] == F1:
                gameDisplay.blit(p1[1],(j[0],j[1]))
            if j[2] == F2:
                gameDisplay.blit(p2[1],(j[0],j[1]))
    gameDisplay.blit(board,(0,120))
    pygame.display.update()

def getLowest(x):
    for i in range(len(FoE[0])):
        for j in range(len(FoE) - 1 ,-1 ,-1):
            if FoE[j][i][0] == x and FoE[j][i][2] == E:
                return [FoE[j][i],j,i]
    return False

def dropAnimation(loc,p):
    temp = p[0]
    x,y = loc[0], startPos[1]
    while y != loc[1]:
        y += yMove
        gameDisplay.blit(p[1],(x,y))
        pygame.display.update()
        clock.tick(10)
        display()
    loc[2] = temp
    display()

def isWinner(y, x, color):#Each pair of for loops counts the possibly sequence, from both sides.
    counter = 1
    for i in range(1,4):#DOWN
        if y + i >= HEIGHT or FoE[y + i][x][2] != color:
            break
        counter += 1
    if counter >= 4:
        return True
    counter = 1
    for i in range(1,4):#RIGHT
        if x + i >= WIDTH or FoE[y][x + i][2] != color:
            break
        counter += 1
    for i in range(1,4):#LEFT
        if x - i < 0 or FoE[y][x - i][2] != color:
            break
        counter += 1
    if counter >= 4:
        return True
    counter = 1
    for i in range(1,4):#\DOWN
        if x + i >= WIDTH or y + i >= HEIGHT or FoE[y + i][x + i][2] != color:
            break
        counter += 1
    for i in range(1,4):#\UP
        if x - i < 0 or y - i < 0 or FoE[y - i][x - i][2] != color:
            break
        counter += 1
    if counter >= 4:
        return True
    counter = 1
    for i in range(1,4):#/DOWN
        if x - i < 0 or y + i >= HEIGHT or FoE[y + i][x - i][2] != color:
            break
        counter += 1
    for i in range(1,4):#/UP
        if x + i >= WIDTH or y - i < 0 or FoE[y - i][x + i][2] != color:
            break
        counter += 1
    if counter >= 4:
        return True
    return False

def computerMove(color):
    dropLoc = []
    global win
    for i in range(WIDTH):#Win Search situation.
        for j in range(HEIGHT):
            if isWinner(j, i, color):
                dropLoc = getLowest(i * xMove + xS)
                if dropLoc != False:
                    if dropLoc[1] == j and dropLoc[2] == i:
                        win = True
                        return dropLoc
    if color == 1:
        otherColor = 2
    else:
        otherColor = 1         
    for i in range(WIDTH):#Block Search situation.
        for j in range(HEIGHT):
            if isWinner(j, i, otherColor):
                dropLoc = getLowest(i * xMove + xS)
                if dropLoc != False:
                    if dropLoc[1] == j and dropLoc[2] == i:
                        return dropLoc
    while True:#Randomly inserts to the table.
        i = random.randint(0,WIDTH - 1)
        dropLoc = getLowest(i * xMove + xS)
        if dropLoc != False:
            return dropLoc  
def initBoard():
    global FoE, startPos, turn
    turn = p1
    
    startPos = [xS + xMove * 3, yS]
    for i in FoE:
        for j in i:
            j[2] = E    
    
def gameLoop(userName1,userName2):
    global win,turn
    coins = 0 #Coins counter
    comTurn = False #If the user want to play VS computer, comTurn will be changed to True.
    initBoard()
    mainMenu = displayMenu()
    if mainMenu:#Return to main menu after showing records.
        return False
    display()       
    
    #GAME LOOP
    while True:    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return False
            gameDisplay.blit(turn[1],startPos)
            if event.type == pygame.KEYDOWN and comTurn == False:
                if event.key == pygame.K_LEFT:
                    if startPos[0] - xMove >= xS:
                        startPos[0] -= xMove
                elif event.key == pygame.K_RIGHT:
                    if startPos[0] + xMove <= xS + xMove * 6:
                        startPos[0] += xMove
                elif event.key == pygame.K_SPACE:
                    dropLoc = getLowest(startPos[0])
                    if dropLoc != False:
                        dropAnimation(dropLoc[0], turn)
                        win = isWinner(dropLoc[1],dropLoc[2],dropLoc[0][2])
                        if win == False:
                            if turn == p1:
                                turn = p2
                            else:
                                turn = p1
                            if vsCom == True:
                                comTurn = True
                        else:
                            if turn == p1:
                                UpdateRecords(userName1,connect4FileName)
                                victory("Victory! " + userName1)
                                return True
                            else:
                                UpdateRecords(userName2,connect4FileName)
                                victory("Victory! " + userName2)
                                return True
                        coins += 1
                gameDisplay.blit(turn[1],startPos)
                display()
            if comTurn == True:
                if win == False:
                    dropLoc = computerMove(2)
                    dropAnimation(dropLoc[0], turn)
                    display()
                    if win == False:
                        turn = p1
                        comTurn = False
                    else:
                        victory("Computer")
                        return
                coins += 1
            if coins == 42:
                gameDisplay.blit(backGround,(0,0))
                displayMessage("Game Over", red, (250, 250), font)
                pygame.display.update()
                clock.tick(5)
            pygame.display.update()