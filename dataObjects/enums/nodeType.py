from enum import Enum
import _globals
import random
from gameObjects.specificMon import SpecificMon
from gameObjects.sections.map.market import Market
from gameObjects.sections.battle.side import Side
from gameObjects.sections.battle.battle import Battle
from typing import Callable
class NodeType(Enum):
    CITY = 'City'
    MARKET = 'Market'
    FIGHT = 'Fight'
    CHICKENS = 'Chickens'
    REST = 'Rest'
    START = 'Start'
    
    def execute(self) -> None:
        if self == NodeType.CITY:
            self.city()
        elif self == NodeType.MARKET:
            self.market()
        elif self == NodeType.FIGHT:
            self.fight()
        elif self == NodeType.CHICKENS:
            self.chickens()
        elif self == NodeType.REST:
            self.rest()
        elif self == NodeType.START:
            self.start()
    
    def fight(self):
        if len(_globals.player.party.mons) == 0:
            _globals.player.chooseMon(1)
        enemyMon = self.randomMon(1)
        enemySide = Side([enemyMon], '', True)
        battle: Battle = Battle(_globals.player.party, enemySide)
        battle.executeBattle()
        if battle.winner == _globals.player.party:
            _globals.player.addGold(10)
        _globals.player.party.activeMon.changeStatus('normal')
        return

    def randomMon(self, level : int):
        monNo2 = str(random.randint(0, len(_globals.genericMons) - 1))
        return SpecificMon(_globals.genericMons[monNo2], level)
    
    def chickens(self):
        print("You have found an unguarded chicken coop. You quickly capture and kill a hen.")
        _globals.player.addItem('Whole chicken')
        print()
        return
    
    def rest(self):
        print("You stumble upon clearing with a creek flowing nearby. You take a moment to rest and restore 20% of your max HP.")
        _globals.player.party.healParty(20)
        _globals.player.status()
        return
    
    def start(self):
        _globals.player.chooseMon(1)
        return

    def city(self): 
        return
    
    def market(self):
        market = Market()
        market.marketMenu()
        return