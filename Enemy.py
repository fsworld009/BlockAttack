'''
Created on 2013/6/5

@author: WorldFS
'''
from Object import Object
from random import randint

class Enemy(Object):
    S_UP=0
    S_DOWN=1
    S_LEFT=2
    S_RIGHT=3
    
    def __init__(self,moveDirection,axis=(0,0)):
        super(Enemy, self).__init__(axis)
        self._loadSprite("./sprite/block.png")
        self._outOfScreen(Object.O_DELETE)
        self.__ex=0
        self.__ey=0
        if moveDirection==Enemy.S_UP:
            self.__ex = randint(-10,10)
            self.__ey = randint(-10,-1)
        if moveDirection==Enemy.S_DOWN:
            self.__ex = randint(-10,10)
            self.__ey = randint(1,10)
        if moveDirection==Enemy.S_LEFT:
            self.__ex = randint(-10,-1)
            self.__ey = randint(-10,10)
        if moveDirection==Enemy.S_RIGHT:
            self.__ex = randint(1,10)
            self.__ey = randint(-10,10)
    
    def action(self):
        frame = self._getFrame()
        if frame==0:
            #self._setBody(0, 0, 32, 32)
            self._setSprite(0,0,0)
            self._setBoundBox(0, 0, 32, 32)
            self._move(self.__ex, self.__ey)
