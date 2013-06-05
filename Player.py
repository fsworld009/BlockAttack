'''
Created on 2013/6/4

@author: WorldFS
'''
from Object import Object
from InputList import Input

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
            #self._setBody(4, 0, 32, 48)
            self._setBoundBox(4, 0, 32, 48)
            if self._iHold(Input.UP):
                self._move(0,-5)
            if self._iHold(Input.DOWN):
                self._move(0,5)
            if self._iHold(Input.LEFT):
                self._move(-5,0)
            if self._iHold(Input.RIGHT):
                self._move(5,0)
                

    
    def _iPushdown(self,keycode):
        return super(Player,self)._iPushdown(self.__playerNo,keycode)
        
    def _iHold(self,keycode):
        return super(Player,self)._iHold(self.__playerNo,keycode)