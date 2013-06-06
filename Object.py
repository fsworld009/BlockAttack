import pygame
from InputList import InputList
from Rect import Rect
import Global

class Object(object):
    #Object attributes 
    D_UP=0
    D_DOWN=1
    D_LEFT=2
    D_RIGHT=3
    def __init__(self,axis=(0,0)):
        #attribute list
        self.__x = axis[0]
        self.__y = axis[1]
        self.__vx = 0
        self.__vy = 0
        
        self.__sprite = None
        self.__spriteNo = 0
        
        self.__boundBox = Rect(0,0,0,0)
        
        self.__bodyList = []
        #also use __bodyNo as current no of bodies
        self.__bodyNo = 0
        
        self.__frame = 0
        
        self.__collision = [0b0,0b0,0b0,0b0]
        
        self.__spriteX =0
        self.__spriteY = 0
        

    
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
            screenSurface.blit(self.__sprite,(self.__x+self.__spriteX,self.__y+self.__spriteY))
            if Global.showRect:
                self.__boundBox.blit(screenSurface,self.__x,self.__y)
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
        
    def _setSprite(self,spriteNo,x,y):
        self.__spriteNo = spriteNo
        self.__spriteX = x
        self.__spriteY = y
        
    def _setBody(self,x,y,width,height):
        if self.__bodyNo < len(self.__bodyList):
            self.__bodyList[self.__bodyNo].change(x,y,width,height)
        else:
            self.__bodyList.append( Rect(x,y,width,height))
        self.__bodyNo+=1
        
    def _setBoundBox(self,x,y,width,height):
        self.__boundBox.change(x, y, width, height)
        
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
        #print(self.__collision)
        self.__collision[Object.D_UP] = 0b0
        self.__collision[Object.D_DOWN] = 0b0
        self.__collision[Object.D_LEFT] = 0b0
        self.__collision[Object.D_RIGHT] = 0b0
        
        self.__spriteX = 0
        self.__spriteY = 0
        
        
    def collisionCorrection(self,targetObj):
        
        adjust_vx = 0
        adjust_vy = 0
        #LEFT
        if self.__vx - targetObj.__vx <0:
            r1 = self.__boundBox.getRectC(self.__x+self.__vx, self.__y)
            r2 = targetObj.__boundBox.getRectC(targetObj.__x+targetObj.__vx, targetObj.__y)
            if Rect.collide(r1, r2):
                #print("LEFT collide")
                adjust_vx+= r2.right+1 - (r1.left)
                self.__collision[Object.D_LEFT] = 0b1
                
        #RIGHT
        if self.__vx - targetObj.__vx >0:
            r1 = self.__boundBox.getRectC(self.__x+self.__vx, self.__y)
            r2 = targetObj.__boundBox.getRectC(targetObj.__x+targetObj.__vx, targetObj.__y)
            if Rect.collide(r1, r2):
                #print("RIGHT collide")
                adjust_vx-= r1.right - (r2.left-1)
                self.__collision[Object.D_RIGHT] = 0b1
                
        #UP
        if self.__vy - targetObj.__vy <0:
            r1 = self.__boundBox.getRectC(self.__x, self.__y+self.__vy)
            r2 = targetObj.__boundBox.getRectC(targetObj.__x, targetObj.__y+targetObj.__vy)
            if Rect.collide(r1, r2):
                #print("LEFT collide")
                adjust_vy+= r2.bottom+1 - (r1.top)
                self.__collision[Object.D_UP] = 0b1
                
        #DOWN
        if self.__vy - targetObj.__vy >0:
            r1 = self.__boundBox.getRectC(self.__x, self.__y+self.__vy)
            r2 = targetObj.__boundBox.getRectC(targetObj.__x, targetObj.__y+targetObj.__vy)
            if Rect.collide(r1, r2):
                #print("LEFT collide")
                adjust_vy-= r1.bottom - (r2.top-1)
                self.__collision[Object.D_DOWN] = 0b1
                
        #UPPER LEFT CORNER
        if self.__vx - targetObj.__vx <0 and self.__vy - targetObj.__vy <0 and self.__collision[Object.D_LEFT] == 0b0 and self.__collision[Object.D_UP] == 0b0:
            r1 = self.__boundBox.getRectC(self.__x+self.__vx, self.__y+self.__vy)
            r2 = targetObj.__boundBox.getRectC(targetObj.__x+targetObj.__vx, targetObj.__y+targetObj.__vy)
            if Rect.collide(r1, r2):
                adjust_vx+= r2.right+1 - (r1.left)
                adjust_vy+= r2.bottom+1 - (r1.top)
                adjust_vy-=1
                
        #UPPER RIGHT CORNER
        if self.__vx - targetObj.__vx >0 and self.__vy - targetObj.__vy <0 and self.__collision[Object.D_RIGHT] == 0b0 and self.__collision[Object.D_UP] == 0b0:
            r1 = self.__boundBox.getRectC(self.__x+self.__vx, self.__y+self.__vy)
            r2 = targetObj.__boundBox.getRectC(targetObj.__x+targetObj.__vx, targetObj.__y+targetObj.__vy)
            if Rect.collide(r1, r2):
                adjust_vx-= r1.right - (r2.left-1)
                adjust_vy+= r2.bottom+1 - (r1.top)
                adjust_vy-=1
                
        #BOTTOM LEFT CORNER
        if self.__vx - targetObj.__vx <0 and self.__vy - targetObj.__vy >0 and self.__collision[Object.D_LEFT] == 0b0 and self.__collision[Object.D_DOWN] == 0b0:
            r1 = self.__boundBox.getRectC(self.__x+self.__vx, self.__y+self.__vy)
            r2 = targetObj.__boundBox.getRectC(targetObj.__x+targetObj.__vx, targetObj.__y+targetObj.__vy)
            if Rect.collide(r1, r2):
                adjust_vx+= r2.right+1 - (r1.left)
                adjust_vy-= r1.bottom - (r2.top-1)
                adjust_vy+=1  
                
        #BOTTOM RIGHT CORNER
        if self.__vx - targetObj.__vx <0 and self.__vy - targetObj.__vy >0 and self.__collision[Object.D_LEFT] == 0b0 and self.__collision[Object.D_DOWN] == 0b0:
            r1 = self.__boundBox.getRectC(self.__x+self.__vx, self.__y+self.__vy)
            r2 = targetObj.__boundBox.getRectC(targetObj.__x+targetObj.__vx, targetObj.__y+targetObj.__vy)
            if Rect.collide(r1, r2):
                adjust_vx-= r1.right - (r2.left-1)
                adjust_vy-= r1.bottom - (r2.top-1)
                adjust_vy+=1  
                
        #print(str(adjust_vx))
        self.__vx += adjust_vx
        self.__vy += adjust_vy