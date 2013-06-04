import pygame, sys

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
        
        while True:
              
            for event in pygame.event.get():
                #user presses "X"
                if event.type ==  pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                """elif event.type == KEYDOWN and event.key == K_SPACE:
                    y+=5
                elif event.type == MOUSEBUTTONDOWN:
                    sound.play()
                elif event.type == KEYDOWN and event.key == K_F12:
                    #save screenshot
                    pygame.image.save(screen,"screenshot.png")"""
            self.__screen.fill((0,0,0))  #clean screen
            pygame.display.flip()   #draw screen
                    
            clock.tick(60)  #fps control