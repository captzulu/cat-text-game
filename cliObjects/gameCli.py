import _globals
import random
from cliObjects.menuFunctions import menuFunctions
from dataObjects.enums.gameStates import GameStates
from dataObjects.enums.colors import Colors
from gameObjects.sections.battle.battle import Battle
from gameObjects.specificMon import SpecificMon
from gameObjects.sections.battle.side import Side
from gameObjects.sections.map.map import Map
class GameCli:
    map : Map 
    def __init__(self) -> None:
        self.gameState : GameStates = GameStates.RUNNING
        self.map = Map.generateRandomMap(10, "new map")

    def quit(self):
        self.gameState = GameStates.ENDED
        exit()
                        
    def enterFight(self):
        monNo1 = str(random.randint(0, len(_globals.genericMons) - 1))
        monNo2 = str(random.randint(0, len(_globals.genericMons) - 1))
        monster1 = SpecificMon(_globals.genericMons[monNo1], 10)
        monster2 = SpecificMon(_globals.genericMons[monNo2], 10)
        side1 = Side([monster1], monster1, _globals.playerName)
        side2 = Side([monster2], monster2)
        battle = Battle(side1, side2)
        #battle menu
        battle.executeIntro()
        self.displayTurnLog(battle)
        input("Hit a key to start the fight...")
        while battle.hasCompleted() == False:
            battle.executeTurn()
            self.displayTurnLog(battle)
            if battle.hasCompleted() == False:
                input("Hit a key to continue...")
        return
    
    def displayTurnLog(self, battle : Battle) -> None:
        print(battle.getTurnLog())
        return
    
    def mainMenu(self):
        options = dict({
            0 : ("Fight", self.enterFight),
            1 : ("Map", self.mapView),
            2 : ("Quit", self.quit)
        })
        while self.gameState == GameStates.RUNNING:
            menuFunctions.menuCallable(options)
    
    def mapView(self):
        print(self.map)