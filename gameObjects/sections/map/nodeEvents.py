import _globals
import random
from gameObjects.specificMon import SpecificMon
from dataObjects.genericMon import GenericMon
from gameObjects.sections.battle.side import Side
from gameObjects.sections.battle.battle import Battle
from cliObjects.menuFunctions import menuFunctions
from dataObjects.enums.nodeType import NodeType

class NodeEvents():
    TYPE_LIST: list[NodeType] = [NodeType.CITY, NodeType.MARKET, NodeType.FIGHT, NodeType.CHICKENS, NodeType.REST]
    

    @staticmethod
    def fight():
        ennemyMon = NodeEvents.randomMon(4)
        ennemySide = Side([ennemyMon], ennemyMon, True)
        battle: Battle = Battle(_globals.player.party, ennemySide)
        battle.executeBattle()
        return

    @staticmethod
    def randomMon(level : int):
        monNo2 = str(random.randint(0, len(_globals.genericMons) - 1))
        return SpecificMon(_globals.genericMons[monNo2], level)
    
    @staticmethod
    def chickens():
        print("You have found an unguarded chicken coop. You quickly capture and kill a hen.")
        _globals.player.addItem('Whole chicken')
        print()
        return
    
    @staticmethod
    def rest():
        print("You stumble upon clearing with a creek flowing nearby. You take a moment to rest and restore 20% of your max HP.")
        _globals.player.party.healParty(20)
        _globals.player.status()
        return
    
    @staticmethod
    def city():
        return
    
    @staticmethod
    def market():
        return