import _globals
import random
from gameObjects.specificMon import SpecificMon
from gameObjects.market import Market
from dataObjects.genericMon import GenericMon
from gameObjects.sections.battle.side import Side
from gameObjects.sections.battle.battle import Battle
from cliObjects.menuFunctions import menuFunctions
from dataObjects.enums.nodeType import NodeType

class NodeEvents():
    RANDOM_TYPE_LIST: list[NodeType] = [NodeType.CITY, NodeType.MARKET, NodeType.FIGHT, NodeType.CHICKENS, NodeType.REST]
    
    @staticmethod
    def fight():
        if len(_globals.player.party.mons) == 0:
            _globals.player.chooseMon(5)
        enemyMon = NodeEvents.randomMon(4)
        enemySide = Side([enemyMon], '', True)
        battle: Battle = Battle(_globals.player.party, enemySide)
        battle.executeBattle()
        if battle.winner == _globals.player.party:
            _globals.player.addGold(10)
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
    def start():
        _globals.player.chooseMon(5)
        return

    @staticmethod
    def city(): 
        return
    
    @staticmethod
    def market():
        market = Market()
        market.marketMenu()
        return