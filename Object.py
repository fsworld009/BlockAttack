import pygame


class Object(object):
    
    def __init__(self,x,y):
        #attribute list
        self.__x = x
        self.__y = y
        self.__vx = 0
        self.__vy = 0
        
        self.__sprite = None
        self.__spriteNo = 0
        
        self.__bodyList = []
        
    #override this function
    def move(self):
        pass

    def update(self):
        self.__x += self.__vx
        self.__y += self.__vy
        
    def frameend(self):
        pass