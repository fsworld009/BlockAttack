'''
Created on 2013/6/5

@author: WorldFS
'''
import pygame

# Rect Coordinates
# Data structure

class RectC(object):
    def __init__(self):
        self.top = 0
        self.left = 0
        self.right = 0
        self.bottom = 0
    def print(self):
        return str(self.left)+" "+str(self.top)+" "+str(self.right)+" "+str(self.bottom)

#if __width==__height= 0 then the rect does not collide with any other rect in game
class Rect(object):
    def __init__(self,x,y,width,height):
        self.change(x,y,width,height)
        
    def change(self,x,y,width,height):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
    
    #if __width==__height= 0 then there is no rectC    
    def getRectC(self,objX,objY):
        if self.__width==0 and self.__height==0:
            return None
        else:
            rc = RectC()
            rc.left = objX + self.__x
            rc.top = objY + self.__y
            rc.right = objX + self.__x + self.__width-1
            rc.bottom = objY + self.__y + self.__height-1
            return rc
        
    def blit(self,screenSurface,objX,objY):
        if self.__width==0 and self.__height ==0:
            return
        else:
            pygame.draw.rect(screenSurface,(0,128,0), pygame.Rect((objX+self.__x,objY+self.__y),(self.__width,self.__height)),1)
    @staticmethod
    def collide(r1, r2):
        #print("r1: "+r1.print())
        #print("r2: "+r2.print())
        if r1 is None or r2 is None:
            return False
        else:
            return ((r1.left <= r2.right) and (r2.left <= r1.right) and (r1.top <= r2.bottom) and (r2.top <=r1.bottom))
        
