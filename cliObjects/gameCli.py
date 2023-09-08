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
        options : dict[int, tuple[str, Callable]] = dict({
            0 : ("Fight", NodeEvents.fight),
            1 : ("Map", self.mapMenu),
            2 : ("Quit", self.quit)
        })
        if _globals.debug:
            options[len(options)] = ("Debug", self.debugMenu)
        while self.gameState == GameStates.RUNNING:
            menuFunctions.menuCallable(options)

    def startMenu(self):
        options : dict[int, tuple[str, Callable]] = dict({
            0 : ("Start", self.createPlayer),
            1 : ("Quit", self.quit)
        })
        menuFunctions.menuCallable(options)

    def debugMenu(self):
        options : dict[int, tuple[str, Callable]] = dict({
            0 : ("Back", lambda : 1 == 1)
        })
        for event in NodeEvents.RANDOM_TYPE_LIST:
            options[len(options)] = (event.value, eval("NodeEvents." + str.lower(event.value)))
        exitMenu = False
        while exitMenu != True:
            exitMenu = menuFunctions.menuCallable(options)
    
    def mapMenu(self):
        if _globals.debug:
            print(self.map)
        
        self.map.start()
        exitMenu = False
        while exitMenu != True:
            options : dict[int, tuple[str, Callable]] = dict({
                0 : ("Back", lambda : 1 == 1),
            })
            if self.map.status is self.map.status.COMPLETED or self.map.status is self.map.status.FAILED:
                options[len(options)] = ("Reset map", self.map.reset)
            else:
                options[len(options)] = ("Advance", self.advanceMenu)
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
        index = self.map.activeNode.columnIndex
        print(f"Current Node : {self.map.activeNode}. At {index}/{len(self.map.nodes)}")
                    
    def addForwardLinks(self, options):
        for node in self.map.activeNode.forwardLinks:
                options[len(options)] = str(node)

    def createPlayer(self):
        _globals.player = Player('test')
        self.mainMenu()