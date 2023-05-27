from tkinter import TRUE
import unittest
from unittest import mock
import _globals
from dataFactory import dataFactory
from gameObjects.sections.battle.side import Side
from gameObjects.specificMon import SpecificMon
from gameObjects.sections.player.player import Player

class playerTest(unittest.TestCase):
    
    def setUp(self):
        self.initTestGlobals()
    
    def initTestGlobals(self):
        _globals.types = dataFactory.loadClassDictTest('type')
        _globals.moves = dataFactory.loadClassDictTest('move')
        _globals.genericMons = dataFactory.loadClassDictTest('genericMon')
        
    def testInitClass(self):
        newPlayer = Player('test')
        self.assertIsInstance(newPlayer, Player)
        
    def testAddItem(self):
        newPlayer = Player('test')
        newPlayer.addItem('test')
        self.assertEqual(len(newPlayer.items), 1)
        
    
if __name__ == '__main__':
    unittest.main()