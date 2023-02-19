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
        self.map = RandomFactory().generateRandomMap(10, "new map")

    def quit(self):
        self.gameState = GameStates.ENDED
        sys.exit()
    
    def mainMenu(self):
        options : dict[int, tuple[str, Callable]] = dict({
            0 : ("Fight", NodeEvents.enterRandomFight),
            1 : ("Map", self.mapView),
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
    
    def mapView(self):
        print(self.map)
        options : dict[int, tuple[str, Callable]] = dict({
            0 : ("Advance", self.advanceMenu),
            1 : ("Back", self.mainMenu)
        })
        while self.gameState == GameStates.RUNNING:
            menuFunctions.menuCallable(options)
            
    def advanceMenu(self):
        options : dict[int, str] = dict({0 : "Back"})
        
        for node in self.map.activeNode.forwardLinks:
            options[len(options)] = str(node)
        
        if len(options) <= 1:
            self.mapView()

        pickedOption : int = menuFunctions.menuInt(options)
        if pickedOption == 0:
            self.mapView()
        else:
            nodeIndex : int = pickedOption - 1
            self.map.advance(nodeIndex)
            
    def createPlayer(self):
        _globals.player = Player('test')
        self.mainMenu()