from Game import Game
import re #a workaround for cx_freeze
'''
Created on 2013/6/4

@author: WorldFS
'''

def main():
    game = Game()
    game.start()
    print("end")

if __name__ == '__main__':
    main()