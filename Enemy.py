'''
Created on 2013/6/5

@author: WorldFS
'''
from Object import Object


class Enemy(Object):
    
    def __init__(self,axis=(0,0)):
        super(Enemy, self).__init__(axis)
        self._loadSprite("./sprite/block.png")
        
    
    def action(self):
        frame = self._getFrame()
        if frame==0:
            #self._setBody(0, 0, 32, 32)
            self._setSprite(0,0,0)
            self._setBoundBox(0, 0, 32, 32)
            #self._move(0,5)
