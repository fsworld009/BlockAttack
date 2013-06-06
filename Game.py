import pygame, sys
from Player import Player
from InputList import InputList
import Global
from Enemy import Enemy
from random import randint
'''
Created on 2013/6/4

@author: WorldFS
'''

class Game(object):
    def __init__(self):
        #var list
        self.__screen = None #pygame  screen Surface

    def start(self):
        pygame.init()
        pygame.display.set_caption("Block Attack")
        self.__screen = pygame.display.set_mode((Global.screenWidth,Global.screenHeight))
        self.__run()
        
    def __run(self):
        clock = pygame.time.Clock()
        
        #initialize objects
        InputList.ins()
        
        playerList=[]
        playerList.append(Player(0,(300,216)))
        
        enemyList=[]

        #enemyList.append(Enemy((352,220)))
        #enemyList.append(Enemy((250,300)))
        
        counter=10
        
        while True:
            
            #generate a block when a specific time frame ocurs  
            if counter==0:
                no = randint(1,5)
                while no>0:
                    direction = randint(0,3)
                    if direction==0:
                        pos=randint(-32,640)
                        enemyList.append(Enemy(Enemy.S_UP,(pos,480)))
                    elif direction==1:
                        pos=randint(-32,640)
                        enemyList.append(Enemy(Enemy.S_DOWN,(pos,-32)))
                    elif direction==2:
                        pos=randint(-32,480)
                        enemyList.append(Enemy(Enemy.S_LEFT,(640,pos)))
                    elif direction==3:
                        pos=randint(-32,480)
                        enemyList.append(Enemy(Enemy.S_RIGHT,(-32,pos)))
                    no-=1
                counter=randint(0,10)
            else:
                counter-=1
              
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
            for _ in enemyList:
                _.action()

            #collision detection
            for p in playerList:
                for e in enemyList:
                    p.collisionCorrection(e)
                    
            #update obj positions and status
            for _ in playerList:
                _.update()
            for _ in enemyList:
                _.update()
            
                     
            #blit
            self.__screen.fill((0,0,0))  #clean screen
            for _ in playerList:
                _.blit(self.__screen)
            for _ in enemyList:
                _.blit(self.__screen)
            pygame.display.flip()   #draw screen
                
            
            #gameover check
            if playerList[0].crushed():
                Global.gameState = Global.GS_GAMEOVER
            
            
            #frameend
            for _ in enemyList:
                _.frameEnd()
            for _ in playerList:
                _.frameEnd()
                
            #remove objects that are marked to delete
            for _ in enemyList:
                if _.delete():
                    enemyList.remove(_)

                    
            InputList.ins().frameEnd()
            
            
            
            #print(len(enemyList))
            
            #fps control
            clock.tick(60)  