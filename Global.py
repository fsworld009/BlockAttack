'''
Created on 2013/6/5

@author: WorldFS
'''

showRect = False
screenWidth = 640
screenHeight = 480
screenScaledWidth = 640
screenScaledHeight = 480

#
GS_MENU=0
GS_GAME=1
GS_GAMEOVER=2
GS_EXIT=3

gameState=GS_MENU

highScore=0
try:
    hFile = open("highscore.dat","r")
    highScore=int(hFile.readline().rstrip('\n'))
    hFile.close()
except OSError:
    highScore=0

def writeHighScore():
    hFile = open("highscore.dat","w")
    hFile.write(str(highScore))
    hFile.close()
    hFile.close()