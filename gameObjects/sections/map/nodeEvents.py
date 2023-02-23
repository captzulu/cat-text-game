import _globals
import random
from gameObjects.specificMon import SpecificMon
from gameObjects.sections.battle.side import Side
from gameObjects.sections.battle.battle import Battle
from cliObjects.menuFunctions import menuFunctions
from dataObjects.enums.nodeType import NodeType

class NodeEvents():
    TYPE_LIST: list[NodeType] = [NodeType.CITY, NodeType.MARKET, NodeType.FIGHT, NodeType.CHICKENS, NodeType.REST]
    

    @staticmethod
    def enterRandomFight():
        monNo1 = str(NodeEvents.pickMon())
        monNo2 = str(random.randint(0, len(_globals.genericMons) - 1))
        monster1 = SpecificMon(_globals.genericMons[monNo1], 10)
        monster2 = SpecificMon(_globals.genericMons[monNo2], 10)
        side1 = Side([monster1], monster1, False, _globals.player.name)
        side2 = Side([monster2], monster2, True)
        battle: Battle = Battle(side1, side2)
        #battle menu
        battle.executeBattle()
        return
    
    @staticmethod
    def chickenEvent():
        print("You have found an unguarded chicken coop. You quickly capture and kill a hen.")
        _globals.player.addItem('Whole chicken')
        print()
        return
    
    @staticmethod
    def pickMon() -> int:
        mons : dict[int, str] = dict()
        for no, mon in _globals.genericMons.items():
            mons[int(no)] = str(mon)
    
        print("")
        return menuFunctions.menuInt(mons)