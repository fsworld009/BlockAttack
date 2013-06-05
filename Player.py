'''
Created on 2013/6/4

@author: WorldFS
'''
from Object import Object
from InputList import InputList,Input

class Player(Object):
    
    def __init__(self,playerNo,axis=(0,0)):
        super(Player, self).__init__(axis)
        if playerNo==0:
            self._loadSprite("./sprite/player1.png")
            self.__playerNo = 0
        elif playerNo==1:
            self._loadSprite("./sprite/player2.png")
            self.__playerNo = 1
    
    def action(self):
        frame = self._getFrame()
        if frame==0:
            if InputList.ins().hold(self.__playerNo,Input.UP):
                self._move(0,-5)
            if InputList.ins().hold(self.__playerNo,Input.DOWN):
                self._move(0,5)
            if InputList.ins().hold(self.__playerNo,Input.LEFT):
                self._move(-5,0)
            if InputList.ins().hold(self.__playerNo,Input.RIGHT):
                self._move(5,0)
        