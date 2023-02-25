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
            0 : ("Fight", NodeEvents.enterRandomFight),
            1 : ("Map", self.mapMenu),
            2 : ("Quit", self.quit)
        })
        while self.gameState == GameStates.RUNNING:
            menuFunctions.menuCallable(options)

    def startMenu(self):
        options : dict[int, tuple[str, Callable]] = dict({
            0 : ("Start", self.createPlayer),
            1 : ("Quit", self.quit)
        })
        while self.gameState == GameStates.RUNNING:
            menuFunctions.menuCallable(options)
    
    def mapMenu(self):
        if _globals.debug:
            print(self.map)
            
        while self.gameState == GameStates.RUNNING:
            options : dict[int, tuple[str, Callable]] = dict({
                0 : ("Back", self.mainMenu),
            })
            if self.map.completed:
                options[len(options)] = ("Reset map", self.map.resetMap)
            else:
                options[len(options)] = ("Advance", self.advanceMenu)
            menuFunctions.menuCallable(options)
            
    def advanceMenu(self):
        while not self.map.completed:
            print(f"Current Node : {self.map.activeNode}")
            options : dict[int, str] = dict({
                0 : "Back",
                1 : "Status"
            })
            
            offset : int = len(options)
            for node in self.map.activeNode.forwardLinks:
                options[len(options)] = str(node)
            
            if len(options) <= 1:
                return

            pickedOption : int = menuFunctions.menuInt(options)
            if pickedOption == 0:
                return
            elif pickedOption == 1:
                print(_globals.player)
            else:
                nodeIndex : int = pickedOption - offset
                self.map.advance(self.map.activeNode.forwardLinks[nodeIndex])
            
    def createPlayer(self):
        _globals.player = Player('test')
        self.mainMenu()