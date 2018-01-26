import pygame
import time
import random



#GLOBAL VARIABLES:
screenSize = (800, 600) 
white = (255,255,255)
red = (255,0,0)
lightBlue = (0,150,250)
buttonH = 80 #The button's height.
buttonW = 175 #The button's width.
SnL = 0
connect4 = 1


#Display initial:
gameDisplay = pygame.display.set_mode(screenSize) #Open new window in screenSize's resolution.
pygame.init()
clock = pygame.time.Clock() #For delaying the image's display.
victoryFireworks = pygame.image.load('Images/victory.jpg')
backGround = pygame.image.load('Images/BackGround.jpg')
recordsBackground = pygame.image.load('Images/records background.png')
pygame.display.set_caption("Multi Game")
font = pygame.font.SysFont('comicsansms',40,1)#Default font
victoryFont = pygame.font.SysFont('comicsansms',60,1)


def displayMessage(msg,color, loc, font): #Function that displays the sent message on the screen.
    message = font.render(msg,True,color)
    gameDisplay.blit(message,loc)
    pygame.display.update()


def displayRecords(gameType = False):
    gameDisplay.blit(recordsBackground,(0,0))
    PrintRecordes(gameType)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()

def showIns(insImage):
    gameDisplay.blit(insImage,(0,0)) #Display the instructions image.
    pygame.display.update()
    while True:
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return True
                    elif event.key == pygame.K_RETURN:
                        return
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

def playAgain():
    gameDisplay.blit(backGround,(0,0))
    displayMessage("Play again? (Y/N)", red, (200, 250), font)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if  event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    return True
                elif event.key == pygame.K_n:
                    return False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()  
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit() 

def victory(pName): #When one of the players wins, that function calls.
    clock.tick(0.3)
    gameDisplay.blit(victoryFireworks,(0,0))
    displayMessage(str(pName) + " Wins!", lightBlue, (160, 200), victoryFont)
    pygame.display.update()
    clock.tick(0.3)
   
             
def UpdateRecords(name, fileName):
    name1 = name.split()
    name = ''
    for ch in name1:
        name += ch
    result = []
    nameExist = False
    rec = open(fileName,'a')
    rec.close
    rec = open(fileName,'r+')
    for i in rec.readlines():
        tmp = i.split()
        if tmp[0] == name:
            result.append([tmp[0],int(tmp[1])+1])
            nameExist = True
        else:
             result.append([tmp[0],int(tmp[1])])
    rec.close
    if not nameExist:
        result.append([name,1])
    else:
        for i in range(len(result)):
            for j in range(i):
                if result[i][1] >= result[j][1]:
                    temp = result[i]
                    result[i] = result[j]
                    result[j] = temp        
    rec = open(fileName, 'w')
    for i in result:
        rec.write(i[0])
        rec.write(' ')
        rec.write(str(i[1]))
        rec.write('\n')
    rec.close

def ReturnRecordes(fileName):
    result = []
    rec = open(fileName,'a')
    rec.close
    rec = open(fileName,'r')
    for i in rec.readlines():
        tmp = i.split()
        result.append((tmp[0],tmp[1]))
    return result

def PrintRecordes(fileName):
    rec = ReturnRecordes(fileName)
    y = 155
    displayMessage("NAME", red,(75, y), font)
    displayMessage("SCORE", red,(500, y), font)
    for i in rec:
        y += 50
        displayMessage(i[0], red,(75, y), font)
        displayMessage(i[1], red,(550, y), font)
                       