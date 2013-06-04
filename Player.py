'''
Created on 2013/6/4

@author: WorldFS
'''
from Object import Object

class Player(Object):
    
    def __init__(self,playerNo,axis=(0,0)):
        super(Player, self).__init__(axis)
        if playerNo==0:
            self._loadSprite("./sprite/player1.png")
        elif playerNo==1:
            self._loadSprite("./sprite/player2.png")