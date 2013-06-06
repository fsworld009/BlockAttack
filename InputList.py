'''
Created on 2013/6/4

@author: WorldFS
'''
from Input import Input
import pygame

"""
singleton
User inputs may be referenced by other objects in game
abstract the inputList in Game into a singleton class
so that it can be referenced through all objects
"""
class InputList(object):
    __ins = None
    @staticmethod
    def ins(): 
        if InputList.__ins is None:
            InputList.__ins = InputList()
        return InputList.__ins
    
    def __init__(self):
        #attributes
        self.__inputList = []
        
        #Player1
        self.__inputList.append(Input((pygame.K_UP,pygame.K_DOWN,pygame.K_LEFT,pygame.K_RIGHT,pygame.K_KP2,pygame.K_KP1,pygame.K_RETURN)))
            
    def getInput(self,inputNo):
        return self.__inputList[inputNo]
    
    def setPushdown(self,key):
        for _ in self.__inputList:
            _.setPushdown(key)
            
    def setRelease(self,key):
        for _ in self.__inputList:
            _.setRelease(key)
            
    def pushdown(self,inputNo,keycode):
        return self.__inputList[inputNo].pushdown(keycode)
        
    def hold(self,inputNo,keycode):
        return self.__inputList[inputNo].hold(keycode)
            
    def config(self,inputNo,buttonList):
        self.__inputList[inputNo].config(buttonList)
        
    def frameEnd(self):
        for _ in self.__inputList:
            _.frameEnd()