'''
Created on 2013/6/4

@author: WorldFS
'''


class Input(object):
    
    def __init__(self,buttonList):
        #button list
        #up, down, left, right, ok, cancel, pause
        self.__buttonList = None
        self.__pushdown = [0b0,0b0,0b0,0b0,0b0,0b0,0b0]
        self.__hold =     [0b0,0b0,0b0,0b0,0b0,0b0,0b0]
        self.config(buttonList)
        
    def config(self,buttonList):
        self.__buttonList = buttonList
        
    def pushdown(self,key):
        for i in range(7):
            if key == self.__buttonList[i]:
                self.__pushdown[i] = 0b1
                self.__hold[i] = 0b1
                
    def release(self,key):
        for i in range(7):
            if key == self.__buttonList[i]:
                self.__hold[i] = 0b0     
    
    def printButtons(self):
        print("hold:"+str(self.__hold)+" pd:"+str(self.__pushdown))
                
    def frameend(self):
        for i in range(7):
            self.__pushdown[i] = 0b0