import unittest
from unittest import mock
import _globals
from dataFactory import dataFactory
from gameObjects.specificMon import SpecificMon
from gameObjects.sections.player.player import Player

class specificMon_Test(unittest.TestCase):
    
    def setUp(self):
        self.initTestGlobals()
    
    def initTestGlobals(self):
        _globals.types = dataFactory.loadClassDictTest('type')
        _globals.moves = dataFactory.loadClassDictTest('move')
        _globals.genericMons = dataFactory.loadClassDictTest('genericMon')
        
    def testInitClass(self):
        newSpecificMon = SpecificMon(_globals.genericMons['0'], 1)
        self.assertIsInstance(newSpecificMon, SpecificMon)

    def testAssignDefaultMoves(self):
        _globals.genericMons['0'].moveList = [
            (1, _globals.moves['1']),
            (5, _globals.moves['1']),
            (10, _globals.moves['5']),
            (15, _globals.moves['4']),
            (20, _globals.moves['3']),
            (25, _globals.moves['2']),
        ]
        newSpecificMon = SpecificMon(_globals.genericMons['0'], 25)
        self.assertEqual(newSpecificMon.moves, [_globals.moves['2'],_globals.moves['3'],_globals.moves['4'],_globals.moves['5']])
        
    @mock.patch('builtins.input', return_value = '1')
    def testChooseMon(self, mocked_instance):
        #also tests pickGenericMon and pickSpecificMon
        newPlayer = Player('test')
        newPlayer.chooseMon(1)
        self.assertEqual(len(newPlayer.party.mons), 1)
    
if __name__ == '__main__':
    unittest.main()