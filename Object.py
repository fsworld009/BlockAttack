import pygame
from InputList import InputList
from Rect import Rect
import Global

class Object(object):
    #Object attributes 
    
    def __init__(self,axis=(0,0)):
        #attribute list
        self.__x = axis[0]
        self.__y = axis[1]
        self.__vx = 0
        self.__vy = 0
        
        self.__sprite = None
        self.__spriteNo = 0
        
        self.__bodyList = []
        #also use __bodyNo as current no of bodies
        self.__bodyNo = 0
        
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
            if Global.showRect:
                for _ in range(self.__bodyNo):
                    self.__bodyList[_].blit(screenSurface,self.__x,self.__y)
        

    
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
        
    def _setBody(self,x,y,width,height):
        if self.__bodyNo < len(self.__bodyList):
            self.__bodyList[self.__bodyNo].change(x,y,width,height)
        else:
            self.__bodyList.append( Rect(x,y,width,height))
        self.__bodyNo+=1
        
    def _move(self,x=0,y=0):
        self.__vx += x
        self.__vy += y
    
    #warp long function call of InputList    
    def _iPushdown(self,inputNo,keycode):
        return InputList.ins().pushdown(inputNo,keycode)
        
    def _iHold(self,inputNo,keycode):
        return InputList.ins().hold(inputNo,keycode)
        
    def frameEnd(self):
        self.__noOfBodies = 0
        self.__vx = 0
        self.__vy = 0
        
        self.__bodyNo = 0