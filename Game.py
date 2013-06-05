import pygame, sys
from Player import Player
from InputList import InputList
import Global

'''
Created on 2013/6/4

@author: WorldFS
'''

class Game(object):
    def __init__(self):
        #var list
        self.__screenWidth = 640
        self.__screenHeight = 480
        self.__screen = None #pygame  screen Surface

    def start(self):
        pygame.init()
        self.__screen = pygame.display.set_mode((self.__screenWidth,self.__screenHeight))
        self.__run()
        
    def __run(self):
        clock = pygame.time.Clock()
        
        #initialize objects
        InputList.ins()
        
        playerList=[]
        playerList.append(Player(0,(0,0)))
        
        
        
        while True:
              
            for event in pygame.event.get():
                #user presses "X"
                if event.type ==  pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_d:
                        Global.showRect = True if not Global.showRect else False
                    InputList.ins().setPushdown(event.key)
                elif event.type == pygame.KEYUP:
                    InputList.ins().setRelease(event.key)
                """"elif event.type == KEYDOWN and event.key == K_SPACE:
                    y+=5
                elif event.type == MOUSEBUTTONDOWN:
                    sound.play()
                elif event.type == KEYDOWN and event.key == K_F12:
                    #save screenshot
                    pygame.image.save(screen,"screenshot.png")"""
            #action
            for _ in playerList:
                _.action()
                
            #update obj positions and status
            for _ in playerList:
                _.update()
                     
            #blit
            self.__screen.fill((0,0,0))  #clean screen
            for _ in playerList:
                _.blit(self.__screen)
            pygame.display.flip()   #draw screen
            
            #frameend
            for _ in playerList:
                _.frameEnd()
                    
            InputList.ins().frameEnd()
            
            #fps control
            clock.tick(60)  