import pygame
from InputList import InputList

class Object(object):
    
    def __init__(self,axis=(0,0)):
        #attribute list
        self.__x = axis[0]
        self.__y = axis[1]
        self.__vx = 0
        self.__vy = 0
        
        self.__sprite = None
        self.__spriteNo = 0
        
        self.__bodyList = []
        self.__noOfBodies = 0
        
        self.__frame = 0
        
    
    def _getFrame(self):
        return self.__frame
    
    def _setFrame(self,nextFrame):
        self.__frame = nextFrame
        
    #override this function
    def action(self):
        pass

    def update(self):
        self.__x += self.__vx
        self.__y += self.__vy
        
    def blit(self,screenSurface):
        if not screenSurface is None:
            screenSurface.blit(self.__sprite,(self.__x,self.__y))
        
    def frameEnd(self):
        self.__noOfBodies = 0
        self.__vx = 0
        self.__vy = 0
    
    def _loadSprite(self,spritePath):
        #only support png files with transparency
        self.__sprite = pygame.image.load(spritePath)#.convert_alpha()
        #print(self.__sprite.get_alpha())
        #self.__sprite.set_alpha(100)
        #print(self.__sprite.get_at((0,0)))
        #print(self.__sprite.get_colorkey())
        #self.__sprite.set_colorkey((0,0,0))
        #print(self.__sprite.get_colorkey())
        
    def _setSprite(self,spriteNo):
        self.__spriteNo = spriteNo
        
    def _setBody(self):
        pass
        
    def _move(self,x=0,y=0):
        self.__vx += x
        self.__vy += y
    
    #warp long function call of InputList    
    def _iPushdown(self,inputNo,keycode):
        return InputList.ins().pushdown(inputNo,keycode)
        
    def _iHold(self,inputNo,keycode):
        return InputList.ins().hold(inputNo,keycode)
        
    