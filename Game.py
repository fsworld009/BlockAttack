import pygame
from Player import Player
from InputList import InputList, Input
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
        #Game screen control
        while True:
            if Global.gameState == Global.GS_MENU:
                self.__menu()
            elif Global.gameState == Global.GS_GAME:
                self.__run()
            elif Global.gameState == Global.GS_GAMEOVER:
                self.__gameover()
            elif Global.gameState == Global.GS_EXIT:
                self.__exit()
                return
    
    def __exit(self):
        Global.writeHighScore()
        pygame.quit()
    
    def __gameover(self):
        clock = pygame.time.Clock()
        #lastScreen = self.__screen.copy()
        font = pygame.font.SysFont("Arial", 80)
        self.__screen.blit(font.render("GAME OVER", 1, (255,0,0)), (80, 100))
        font2 = pygame.font.SysFont("Arial", 24)
        self.__screen.blit(font2.render("YOU ARE CRUSHED", 1, (255,0,0)), (200, 250))
        self.__screen.blit(font2.render("Press ENTER to start the game", 1, (255,0,0)), (150, 300))
        

        #write high score to file
        Global.writeHighScore()
        
        while True:
            for event in pygame.event.get():
                if event.type ==  pygame.QUIT:
                    Global.gameState = Global.GS_EXIT
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_d:
                        Global.showRect = True if not Global.showRect else False
                    InputList.ins().setPushdown(event.key)
                elif event.type == pygame.KEYUP:
                    InputList.ins().setRelease(event.key)
            pygame.display.flip()
            clock.tick(60)
            if InputList.ins().getInput(0).pushdown(Input.PAUSE):
                Global.gameState = Global.GS_GAME
                return 
        
    def __menu(self):
        clock = pygame.time.Clock()
  
        while True:
            for event in pygame.event.get():
                if event.type ==  pygame.QUIT:
                    Global.gameState = Global.GS_EXIT
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_d:
                        Global.showRect = True if not Global.showRect else False
                    InputList.ins().setPushdown(event.key)
                elif event.type == pygame.KEYUP:
                    InputList.ins().setRelease(event.key)
                    
            self.__screen.fill((0,0,0))  #clean screen
            font = pygame.font.SysFont("Arial", 80)
            self.__screen.blit(font.render("BLOCK ATTACK", 1, (255,255,255)), (20, 100))
            font2 = pygame.font.SysFont("Arial", 24)
            self.__screen.blit(font2.render("Press ENTER to start the game", 1, (255,255,255)), (150, 300))
            self.__screen.blit(font2.render("use movement keys to move the blue block", 1, (255,255,255)), (80, 350))
            pygame.display.flip()
            clock.tick(60)
            
            if InputList.ins().getInput(0).pushdown(Input.PAUSE):
                Global.gameState = Global.GS_GAME
                return 
        
        
    def __run(self):
        clock = pygame.time.Clock()
        
        #initialize objects
        InputList.ins()
        
        playerList=[]
        playerList.append(Player(0,(300,216)))
        
        enemyList=[]

        
        counter=10
        playTime=0
        #TIMEREVENT =pygame.USEREVENT+1
        #pygame.time.set_timer(TIMEREVENT,1000)
        
        font = pygame.font.SysFont("Arial", 20)
        
        
        while True:
            
            #generate a block when a specific time frame ocurs  
            if counter==0:
                no = randint(1,3)
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
                    Global.gameState = Global.GS_EXIT
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_d:
                        Global.showRect = True if not Global.showRect else False
                    InputList.ins().setPushdown(event.key)
                elif event.type == pygame.KEYUP:
                    InputList.ins().setRelease(event.key)
                #elif event.type == TIMEREVENT:
                #    print("timer triggerd")
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
            
            #display timer
            self.__screen.blit(font.render("Time:"+str(playTime)+" frames", 1, (255,0,255)), (0, 0))
            self.__screen.blit(font.render("High Score:"+str(Global.highScore)+" frames", 1, (255,0,255)), (0, 20)) 
            
            #display fps
            self.__screen.blit(font.render("FPS: "+str(clock.get_fps()), 1, (255,0,255)), (540, 0))     
            pygame.display.flip()   #draw screen
                
            
            #gameover check
            if playerList[0].crushed():
                Global.gameState = Global.GS_GAMEOVER
                return
            
            
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
            playTime+=1 
            #refresh highscore
            if playTime > Global.highScore:
                Global.highScore = playTime