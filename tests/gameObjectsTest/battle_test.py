from tkinter import TRUE
import unittest
from unittest import mock
import _globals
from dataFactory import dataFactory
from gameObjects.sections.battle.side import Side
from gameObjects.specificMon import SpecificMon
from gameObjects.sections.battle.battle import Battle

class battleTest(unittest.TestCase):
    TEST_MON_1_NB : str = '3'
    TEST_MON_2_NB : str = '2'
    battle : Battle
    
    def setUp(self):
        self.initTestGlobals()
        self.battle = self.InitClass()
        self.battle.quickMode = True
    
    def initTestGlobals(self):
        _globals.types = dataFactory.loadClassDictTest('type')
        _globals.moves = dataFactory.loadClassDictTest('move')
        _globals.genericMons = dataFactory.loadClassDictTest('genericMon')
        
    def InitClass(self):
        newSpecificMon1 = SpecificMon(_globals.genericMons[self.TEST_MON_1_NB], 10)
        side1 = Side([newSpecificMon1])
        
        newSpecificMon2 = SpecificMon(_globals.genericMons[self.TEST_MON_2_NB], 10)
        side2 = Side([newSpecificMon2], '', True)
        
        return Battle(side1, side2)
        
    def testCalculateLongestMonNameLength(self):
        longestMonNameLength = self.battle.calculateLongestMonNameLength()
        testMon1 = SpecificMon(_globals.genericMons[self.TEST_MON_1_NB], 10)
        testMon1.nickname = 'Wild ' + testMon1.nickname
        expectedText1 = len(str(testMon1))
        self.assertEqual(longestMonNameLength, expectedText1)

    def testFillTitleLine(self):
        title = f"Battle ! {self.battle.side1.name} Vs {self.battle.side2.name}"
        filledTitle = self.battle.writeTitle(title)
        lineFiller = self.battle.Filler * ((self.battle.calculateLongestMonNameLength() - len(title)) // 2)
        expectedText = lineFiller + title + lineFiller
        self.assertEqual(filledTitle, expectedText)
        
    def testExecuteIntro(self):
        title = f"Battle ! {self.battle.side1.name} Vs {self.battle.side2.name}"
        titleLine = self.battle.edgeSymbol + self.battle.writeTitle(title) + self.battle.edgeSymbol
        self.battle.write(titleLine)
        self.battle.write(str(self.battle.side1.getActiveMonSpecies()))
        
        longestMonNameLength = self.battle.calculateLongestMonNameLength()
        paddingLength = longestMonNameLength // 2
        self.battle.write(' ' * paddingLength + 'VS' + (' ' * paddingLength))
        self.battle.write(str(self.battle.side2.getActiveMonSpecies()))
        self.battle.write(self.battle.edgeSymbol + (self.battle.Filler * longestMonNameLength) + self.battle.edgeSymbol)
    
    def testAttack_damageWithinVariation(self):
        move = self.battle.side1.getActiveMonSpecies().moves[0]
        expectedModifier = self.battle.side2.activeMon.weakTo(move.type)
        ExpectedDamage = expectedModifier * self.battle.side1.activeMon.attack
        ExpectedMinDamage = int(ExpectedDamage * self.battle.DAMAGE_VARIATION_MIN)
        ExpectedMaxDamage = int(ExpectedDamage * self.battle.DAMAGE_VARIATION_MAX)
        self.battle.attack(self.battle.side1.activeMon, self.battle.side2.activeMon, move)
        actualDamage = self.battle.side2.activeMon.maxHealth - self.battle.side2.activeMon.currentHealth
        
        self.assertTrue(ExpectedMinDamage <= actualDamage <= ExpectedMaxDamage)
        
    def testAttack_notVeryEffective_hasNotVeryEffective(self):
        self.battle.attack(self.battle.side1.activeMon, self.battle.side2.activeMon, self.battle.side1.getActiveMonSpecies().moves[0])
        actualLine = self.battle.getTurnLog()
        
        self.assertTrue("not very effective" in actualLine)
    
    def testGetFastestSide(self):
        expectedFastestSide = self.battle.side1
        self.assertEqual(expectedFastestSide, self.battle.getFastestSide())
        
    def testGetFastestSide_side1Priority(self):
        verySlowSpecificMon = SpecificMon(_globals.genericMons['5'], 1)
        side1 = Side([verySlowSpecificMon])
        veryFastSpecificMon = SpecificMon(_globals.genericMons['4'], 100)
        side2 = Side([veryFastSpecificMon])
        newBattle = Battle(side1, side2)
        newBattle.sideWithPriority = newBattle.side1
        
        expectedFastestSide = newBattle.side1
        self.assertEqual(expectedFastestSide, newBattle.getFastestSide())
    
    @mock.patch('builtins.input', return_value = '1')
    def testBattleLoop_getsCompleted(self, mocked_instance):
        veryWeakSpecificMon = SpecificMon(_globals.genericMons['5'], 1)
        side1 = Side([veryWeakSpecificMon])
        veryStrongSpecificMon = SpecificMon(_globals.genericMons['4'], 100)
        side2 = Side([veryStrongSpecificMon])
        newBattle = Battle(side1, side2)
        _globals.debug = False #causes an error otherwise

        newBattle.battleLoop()
        self.assertTrue(newBattle.completed)
        
    @mock.patch('builtins.input', return_value = '1')
    def testBattleLoop_getsCompletedByStall(self, mocked_instance):
        veryWeakSpecificMon = SpecificMon(_globals.genericMons['2'], 100)
        side1 = Side([veryWeakSpecificMon])
        veryStrongSpecificMon = SpecificMon(_globals.genericMons['4'], 100)
        side2 = Side([veryStrongSpecificMon])
        newBattle = Battle(side1, side2)
        newBattle.quickMode = True
        _globals.debug = False #causes an error otherwise

        newBattle.battleLoop()
        self.assertIn('stalled', newBattle.getTurnLog())
        
    def testTriggerStatus_poison(self):
        monInitialHp = self.battle.side1.activeMon.currentHealth
        self.battle.side1.activeMon.status = "poison"
        self.battle.triggerStatus()
        
        self.assertTrue(monInitialHp > self.battle.side1.activeMon.currentHealth)
        
    
if __name__ == '__main__':
    unittest.main()