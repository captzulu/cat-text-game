from tkinter import TRUE
import unittest
import _globals
from dataObjects.genericMon import GenericMon
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
    
    def initTestGlobals(self):
        _globals.types = dataFactory.loadClassDictTest('type')
        _globals.genericMons = dataFactory.loadClassDictTest('genericMon')
        
    def InitClass(self):
        newSpecificMon1 = SpecificMon(_globals.genericMons[self.TEST_MON_1_NB], 10)
        side1 = Side([newSpecificMon1], newSpecificMon1, False)
        
        newSpecificMon2 = SpecificMon(_globals.genericMons[self.TEST_MON_2_NB], 10)
        side2 = Side([newSpecificMon2], newSpecificMon2, True)
        
        return Battle(side1, side2)
        
    def testCalculateLongestMonNameLength(self):
        longestMonNameLength = self.battle.calculateLongestMonNameLength()
        testMon1 = SpecificMon(_globals.genericMons[self.TEST_MON_1_NB], 10)
        testMon1.nickname = 'Wild ' + testMon1.nickname
        expectedText1 = len(str(testMon1))
        self.assertEqual(longestMonNameLength, expectedText1)

    def testFillTitleLine(self):
        title = f"Battle ! {self.battle.side1.name} Vs {self.battle.side2.name}"
        filledTitle = self.battle.fillTitleLine(title)
        lineFiller = self.battle.Filler * ((self.battle.calculateLongestMonNameLength() - len(title)) // 2)
        expectedText = lineFiller + title + lineFiller
        self.assertEqual(filledTitle, expectedText)
        
        
    def testExecuteIntro(self):
        title = f"Battle ! {self.battle.side1.name} Vs {self.battle.side2.name}"
        titleLine = self.battle.edgeSymbol + self.battle.fillTitleLine(title) + self.battle.edgeSymbol
        self.battle.write(titleLine)
        self.battle.write(str(self.battle.side1.getActiveMonSpecies()))
        
        longestMonNameLength = self.battle.calculateLongestMonNameLength()
        paddingLength = longestMonNameLength // 2
        self.battle.write(' ' * paddingLength + 'VS' + (' ' * paddingLength))
        self.battle.write(str(self.battle.side2.getActiveMonSpecies()))
        self.battle.write(self.battle.edgeSymbol + (self.battle.Filler * longestMonNameLength) + self.battle.edgeSymbol)
    
    def testAttack(self):
        expectedModifier = self.battle.side2.activeMon.weakTo(self.battle.side1.getActiveMonSpecies().type1)
        ExpectedDamage = expectedModifier * self.battle.side1.activeMon.attack
        ExpectedMinDamage = int(ExpectedDamage * self.battle.DAMAGE_VARIATION_MIN)
        ExpectedMaxDamage = int(ExpectedDamage * self.battle.DAMAGE_VARIATION_MAX)
        self.battle.attack(self.battle.side1.activeMon, self.battle.side2.activeMon, self.battle.side1.getActiveMonSpecies().type1)
        actualDamage = self.battle.side2.activeMon.maxHealth - self.battle.side2.activeMon.currentHealth
        
        self.assertTrue(ExpectedMinDamage <= actualDamage <= ExpectedMaxDamage)
        
    def testAttack_notVeryEffective_hasNotVeryEffective(self):
        self.battle.attack(self.battle.side1.activeMon, self.battle.side2.activeMon, self.battle.side1.getActiveMonSpecies().type1)
        actualLine = self.battle.getTurnLog()
        
        self.assertTrue("not very effective" in actualLine)
        

    
if __name__ == '__main__':
    unittest.main()

