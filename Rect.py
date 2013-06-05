'''
Created on 2013/6/5

@author: WorldFS
'''

# Rect Coordinates
# Data structure

class RectC(object):
    def __init__(self):
        self.top = 0
        self.left = 0
        self.right = 0
        self.bottom = 0
        
class Rect(object):
    def __init__(self,x,y,width,height):
        self.change(x,y,width,height)
        
    def change(self,x,y,width,height):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        
    def getRectC(self,objX,objY):
        rc = RectC()
        rc.left = objX+self.__x
        rc.top = objX+self.__y
        rc.right = objX+self.__width-1
        rc.bottom = objY+self.__height-1
        return rc
        
    @staticmethod
    def collide(r1, r2):
        return ((r1.left <= r2.right) and (r2.left <= r1.right) and (r1.top <= r2.bottom) and (r2.top <=r1.bottom))
        
