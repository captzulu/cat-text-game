import _globals
import random
from cliObjects.menuFunctions import menuFunctions
from dataObjects.enums.gameStates import GameStates
from gameObjects.sections.player.player import Player
from gameObjects.sections.map.randomFactory import RandomFactory
from gameObjects.sections.map.map import Map
from gameObjects.sections.map.nodeEvents import NodeEvents
from typing import Callable
import sys
class GameCli:
    map : Map 
    def __init__(self) -> None:
        self.gameState : GameStates = GameStates.RUNNING
        self.map = RandomFactory().generateRandomMap(5, "new map")

    def quit(self):
        self.gameState = GameStates.ENDED
        sys.exit()
    
    def mainMenu(self):
        options : list[tuple[str, Callable]] = [("Fight", self.standaloneFight),("Map", self.mapMenu),("Quit", self.quit)]
        if _globals.debug:
            options.append(("Debug", self.debugMenu))
        while self.gameState == GameStates.RUNNING:
            menuFunctions.menuCallable(options)

    def startMenu(self):
        options : list[tuple[str, Callable]] = [("Start", self.standaloneFight),("Quit", self.mapMenu)]
        menuFunctions.menuCallable(options)

    def debugMenu(self):
        if len(_globals.player.party.mons) == 0:
            print('Pick a mon to avoid errors')
            _globals.player.chooseMon(1)
        options : list[tuple[str, Callable]] = [("Back", lambda : 1 == 1)]
        for event in NodeEvents.RANDOM_TYPE_LIST:
            options.append((event.value, eval("NodeEvents." + str.lower(event.value))))
        options.append(('Status', _globals.player.status))
        exitMenu = False
        while exitMenu != True:
            exitMenu = menuFunctions.menuCallable(options)
    
    def mapMenu(self):
        if _globals.debug:
            print(self.map)
        
        self.map.start()
        exitMenu = False
        while exitMenu != True:
            options : list[tuple[str, Callable]] = [("Back", lambda : 1 == 1)]
            if self.map.status is self.map.status.COMPLETED or self.map.status is self.map.status.FAILED:
                options.append(("Reset map", self.map.reset))
            else:
                options.append(("Advance", self.advanceMenu))
            exitMenu : bool = menuFunctions.menuCallable(options)
            
    def advanceMenu(self):
        while self.map.status is not self.map.status.COMPLETED and self.map.status is not self.map.status.FAILED:
            options : dict[int, str] = dict({
                0 : "Back",
                1 : "Status"
            })
            self.showCurrentNode()
            offset : int = len(options)
            self.addForwardLinks(options)
            
            if len(options) == offset:
                return

            pickedOption : int = menuFunctions.menuInt(options)
            if pickedOption == 0:
                return
            elif pickedOption == 1:
                _globals.player.status
            else:
                nodeIndex : int = pickedOption - offset
                self.map.advance(self.map.activeNode.forwardLinks[nodeIndex])
                if _globals.player.party.isDefeated():
                    self.map.fail()
                    print('Game over !')
    
    def showCurrentNode(self):
        index = self.map.activeNode.columnIndex + 1
        print(f"Current Node : {self.map.activeNode}. At {index}/{len(self.map.nodes)}")
                    
    def addForwardLinks(self, options):
        for node in self.map.activeNode.forwardLinks:
            options[len(options)] = str(node)

    def createPlayer(self):
        _globals.player = Player('test')
        self.mainMenu()
        
    def standaloneFight(self):
        NodeEvents.fight()
        _globals.player.party.activeMon.fullHeal()