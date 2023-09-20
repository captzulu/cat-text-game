from tkinter import TRUE
import unittest
from unittest import mock
import _globals
from dataFactory import dataFactory
from gameObjects.sections.player.player import Player
from gameObjects.specificMon import SpecificMon
from gameObjects.sections.map.market import Market
from gameObjects.sections.map.marketItem import MarketItem

class marketTest(unittest.TestCase):
    
    def setUp(self):
        self.initTestGlobals()
    
    def initTestGlobals(self):
        _globals.types = dataFactory.loadClassDictTest('type')
        _globals.moves = dataFactory.loadClassDictTest('move')
        _globals.genericMons = dataFactory.loadClassDictTest('genericMon')
        
    def testInitClass(self):
        newMarket = Market()
        self.assertIsInstance(newMarket, Market)
        
    def testProcessPayment_noEnoughGold(self):
        _globals.player = Player('test')
        _globals.player.addGold(8)
        newMarket = Market()
        newMarket.processPayment(MarketItem('test', lambda : True, 10))
        self.assertEqual(_globals.player.gold, 8)
        
    def testProcessPayment_enoughGold(self):
        _globals.player = Player('test')
        _globals.player.addGold(12)
        newMarket = Market()
        newMarket.processPayment(MarketItem('test', lambda : True, 10))
        self.assertEqual(_globals.player.gold, 2)
        
    def testProcessPayment_levelUp(self):
        _globals.player = Player('test')
        _globals.player.addGold(12)
        newMarket = Market()
        newMarket.generateSelection()
        _globals.player.party.addMon(SpecificMon(_globals.genericMons['5'], 1))
        levelBeforeLevelUp = _globals.player.party.activeMon.level
        newMarket.selection[0].giveItem()
        self.assertEqual(_globals.player.party.activeMon.level, levelBeforeLevelUp + 1)
    
    @mock.patch('builtins.input', return_value = '1')
    def testChooseMon(self, mocked_instance):
        #also tests pickGenericMon and pickSpecificMon
        newPlayer = Player('test')
        newPlayer.chooseMon(1)
        self.assertEqual(len(newPlayer.party.mons), 1)
    
if __name__ == '__main__':
    unittest.main()