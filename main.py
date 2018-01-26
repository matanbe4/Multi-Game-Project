import pygame
import time
import random
import connect4Game
import SnLGame
from commonFunctions import *

userName1 = None
userName2 = None  
gotNicks = False
#screenSize = (800, 600)
nickFont = pygame.font.SysFont('comicsansms',60,1,1)#The nicknames font.
lightBlue = (0,150,250)
white = (255,255,255)
QAFont = pygame.font.SysFont('comicsansms',30,1,1)
#gameDisplay = pygame.display.set_mode(screenSize) #Open new window in screenSize's resolution.

def nickNamesGet():
    text = ''
    got = 0
    global userName1, userName2
    introduction = pygame.image.load('Images/introduction.png')
    gameDisplay.blit(introduction,(0,0))
    pygame.display.update()
    displayMessage("Enter Player " + str(got + 1) + ":", lightBlue, (200, 280), nickFont)
    while got < 2:#Got User names.
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]#Deletes the last char.
                elif event.key == pygame.K_RETURN:
                    got += 1#User name 2.
                    if got == 1:#first user name.
                        if text == '':
                            text = 'P1'#Default message.
                        userName1 = text
                        text = ''
                    else:
                        if text == '':#Default message.
                            text = 'P2'
                        userName2 = text
                        break        
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                else:
                    ch = event.unicode
                    if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
                        text += ch
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()
            gameDisplay.blit(introduction,(0,0))
            displayMessage("Enter Player " + str(got + 1) + ":", lightBlue, (200, 280), nickFont)
            displayMessage(text, lightBlue, (250, 350), nickFont)
        pygame.display.update()

def mainMenu():
    global gotNicks
    play = True
    if gotNicks == False:
        nickNamesGet()
        gotNicks = True
    menu = pygame.image.load('Images/Main Menu.png')
    gameDisplay.blit(menu,(0,0))
    displayMessage("Found a bag? Contact MultiGameQA@gmail.com", white, (100, 550), QAFont)
    pygame.display.update()
    gameType = None
    while True: #Cursor loop.
        cur = pygame.mouse.get_pos()
        curClick = pygame.mouse.get_pressed()
        if 130 <= cur[0] <= 130 + buttonW and 155 <= cur[1] <= 155 + buttonH:
            if curClick[0] == 1:
                while play == True:
                    play = connect4Game .gameLoop(userName1, userName2)
                    if play != False:
                        play = playAgain()
                mainMenu()
        elif 492 <= cur[0] <= 492 + buttonW and 157 <= cur[1] <= 157 + buttonH:
            if curClick[0] == 1:
                while play == True:
                    play = SnLGame.gameLoop(userName1, userName2)                    
                    if play != False:
                        play = playAgain()
                mainMenu()
        elif 315 <= cur[0] <= 315 + buttonW and 383 <= cur[1] <= 383 + buttonH:
            if curClick[0] == 1:
                pygame.quit()
                quit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()

mainMenu()