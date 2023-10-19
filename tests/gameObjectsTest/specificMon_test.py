import unittest
from unittest import mock
import _globals
from dataFactory import dataFactory
from gameObjects.specificMon import SpecificMon
from gameObjects.sections.battle.effectLib import EffectLib
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
    
    def testLearnMovesFromMoveList(self):
        _globals.genericMons['0'].moveList = [(1, _globals.moves['1']), (2, _globals.moves['1'])]
        newSpecificMon = SpecificMon(_globals.genericMons['0'], 1)
        newSpecificMon.levelUp()
        self.assertEqual(2, len(newSpecificMon.moves))
    
    def testLevelUp(self):
        initialLevel = 25
        newSpecificMon = SpecificMon(_globals.genericMons['0'], initialLevel)
        newSpecificMon.levelUp()
        self.assertEqual(newSpecificMon.level, initialLevel + 1)
        
    def testCalculateStats(self):
        newSpecificMon = SpecificMon(_globals.genericMons['3'], 5)
        initialHp = newSpecificMon.maxHealth
        initialAttack = newSpecificMon.attack
        initialSpeed = newSpecificMon.speed
        newSpecificMon.levelUp()
        self.assertGreater(newSpecificMon.maxHealth, initialHp)
        self.assertGreater(newSpecificMon.attack, initialAttack)
        self.assertGreater(newSpecificMon.speed, initialSpeed)
        
    def testGetStatusAcronym(self):
        newSpecificMon = SpecificMon(_globals.genericMons['3'], 5)
        EffectLib.poison(newSpecificMon, 100)
        self.assertEqual(newSpecificMon.getStatusAcronym(), 'psn')
    
if __name__ == '__main__':
    unittest.main()