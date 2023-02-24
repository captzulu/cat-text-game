from dataFactory import dataFactory
import _globals  
from dataObjects.enums.gameStates import GameStates
from cliObjects.gameCli import GameCli


def loadData():
    _globals.types = dataFactory.loadClassDict('type')
    _globals.moves = dataFactory.loadClassDict('move')
    _globals.genericMons = dataFactory.loadClassDict('genericMon')

def main():
    withCli()
        
def withCli():
    game = GameCli()
    game.startMenu()

if __name__ == '__main__':
    loadData()
    main()
