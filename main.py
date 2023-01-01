from cliObjects.menuFunctions import menuFunctions
import pygame
import ext_modules.ptext as ptext
from dataFactory import dataFactory
import _globals  
from game import Game
from dataObjects.enums.gameStates import GameStates
from cliObjects.gameCli import GameCli


def loadData():
    _globals.types = dataFactory.loadClassDict('type') 
    _globals.genericMons = dataFactory.loadClassDict('genericMon')

def main():
    #playerName = _globals.playerName = input("What's your name? > ").capitalize()
    #print(f'Your name is {playerName}')
    menuFunctions.menuCallable({1 : ("Pygame", withPygame), 2 : ("CLI", withCli)})

def withPygame():
    pygame.init()
    pygame.display.set_caption("Pokemon Clone")
    #print(pygame.font.get_fonts())
    ptext.DEFAULT_FONT_NAME = pygame.font.match_font('dejavusansmono')
    game = Game()
    while game.gameState == GameStates.RUNNING:
        game.run()
        
def withCli():
    game = GameCli()
    game.mainMenu()

if __name__ == '__main__':
    loadData()
    main()
