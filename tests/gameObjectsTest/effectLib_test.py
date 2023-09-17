from tkinter import TRUE
import unittest
import _globals
from dataFactory import dataFactory
from gameObjects.sections.battle.effectLib import EffectLib
from gameObjects.specificMon import SpecificMon

class marketTest(unittest.TestCase):
    
    def setUp(self):
        self.initTestGlobals()
    
    def initTestGlobals(self):
        _globals.types = dataFactory.loadClassDictTest('type')
        _globals.moves = dataFactory.loadClassDictTest('move')
        _globals.genericMons = dataFactory.loadClassDictTest('genericMon')
        
    def testPoison_withoutStatus(self):
        defender = SpecificMon(_globals.genericMons['1'], 50)
        EffectLib.poison(defender, 100)
        self.assertEqual(defender.status, 'poison')

    def testPoison_withStatus(self):
        defender = SpecificMon(_globals.genericMons['1'], 50)
        initialStatus : str = 'not normal'
        defender.changeStatus(initialStatus)
        EffectLib.poison(defender, 100)
        self.assertEqual(defender.status, initialStatus)
    
    def testCheckTriggerList_PoisonExists(self):
        self.assertTrue(EffectLib.checkTriggerList('afterMove', 'poison'))
    
    def testCheckTriggerList_DoesntExist(self):
        self.assertFalse(EffectLib.checkTriggerList('afterMove', 'fake effect'))
        
if __name__ == '__main__':
    unittest.main()