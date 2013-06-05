'''
Created on 2013/6/4

@author: WorldFS
'''


class Input(object):
    #Input keycode constants
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    OK = 4
    CANCEL = 5
    PAUSE = 6
    def __init__(self,buttonList):
        #button list
        #up, down, left, right, ok, cancel, pause
        self.__buttonList = None
        self.__pushdown = [0b0,0b0,0b0,0b0,0b0,0b0,0b0]
        self.__hold =     [0b0,0b0,0b0,0b0,0b0,0b0,0b0]
        self.config(buttonList)
        
    def config(self,buttonList):
        self.__buttonList = buttonList
        
    def setPushdown(self,key):
        for i in range(7):
            if key == self.__buttonList[i]:
                self.__pushdown[i] = 0b1
                self.__hold[i] = 0b1
                
    def setRelease(self,key):
        for i in range(7):
            if key == self.__buttonList[i]:
                self.__hold[i] = 0b0  
                
    def pushdown(self,keycode):
        if self.__pushdown[keycode] == 0b1:
            return True
        else:
            return False
        
    def hold(self,keycode):
        if self.__hold[keycode] == 0b1:
            return True
        else:
            return False
    
    def printButtons(self):
        print("hold:"+str(self.__hold)+" pd:"+str(self.__pushdown))
                
    def frameEnd(self):
        for i in range(7):
            self.__pushdown[i] = 0b0