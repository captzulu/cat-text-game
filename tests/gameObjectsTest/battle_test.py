import unittest
import _globals
from dataObjects.genericMon import GenericMon
from dataFactory import dataFactory
from gameObjects.side import Side
from gameObjects.specificMon import SpecificMon
from gameObjects.battle import Battle

class battleTest(unittest.TestCase):
    TEST_MON_1_NB : str = '1'
    TEST_MON_2_NB : str = '2'
    battle : Battle
    
    def setUp(self):
        self.initTestGlobals()
        self.battle = self.InitClass()
    
    def initTestGlobals(self):
        _globals.types = dataFactory.loadClassDictTest('type')
        _globals.genericMons = dataFactory.loadClassDictTest('genericMon')
        
    def InitClass(self):
        newSpecificMon1 = SpecificMon(_globals.genericMons[self.TEST_MON_1_NB], 1)
        side1 = Side([newSpecificMon1], newSpecificMon1)
        
        newSpecificMon2 = SpecificMon(_globals.genericMons[self.TEST_MON_2_NB], 1)
        side2 = Side([newSpecificMon2], newSpecificMon2)
        
        return Battle(side1, side2)
        
    def testCalculateLongestMonNameLength(self):
        longestMonNameLength = self.battle.calculateLongestMonNameLength()
        expectedText = len(str(_globals.genericMons[self.TEST_MON_1_NB]))
        self.assertEqual(longestMonNameLength, expectedText)

    def testFillTitleLine(self):
        title = f"Battle ! {self.battle.side1.name} Vs {self.battle.side2.name}"
        filledTitle = self.battle.fillTitleLine(title)
        lineFiller = self.battle.Filler * ((len(str(self.battle.side1.getActiveMonSpecies())) - len(title)) // 2)
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
        

    
if __name__ == '__main__':
    unittest.main()

