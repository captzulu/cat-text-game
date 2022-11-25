import unittest
import _globals
from dataObjects.genericMon import GenericMon
from dataFactory import dataFactory
from gameObjects.side import Side
from gameObjects.specificMon import SpecificMon
from gameObjects.battle import Battle

class battleTest(unittest.TestCase):
    TEST_MON_1 = _globals.genericMons['1']
    TEST_MON_2 = _globals.genericMons['2']
        
    def setUp(self):
        self.initTestGlobals()
    
    def initTestGlobals(self):
        _globals.types = dataFactory.loadClassDictTest('type')
        _globals.genericMons = dataFactory.loadClassDictTest('genericMon')
        
    def InitClass(self):
        newSpecificMon1 = SpecificMon(self.TEST_MON_1, 1)
        side1 = Side([newSpecificMon1], newSpecificMon1)
        
        newSpecificMon2 = SpecificMon(self.TEST_MON_2, 1)
        side2 = Side([newSpecificMon2], newSpecificMon2)
        
        return Battle(side1, side2)
        
    def testInitClass(self):
        self.assertIsInstance(self.InitClass(), Battle)
        
    def testCalculateLongestMonNameLength(self):
        battle = self.InitClass()
        longestMonNameLength = battle.calculateLongestMonNameLength()
        expectedText = len(str(self.TEST_MON_2))
        self.assertEqual(longestMonNameLength, expectedText)

    def testFillTitleLine(self):
        battle = self.InitClass()
        title = f"Battle ! {self.TEST_MON_1.name} Vs {self.TEST_MON_2.name}"
        filledTitle = battle.fillTitleLine(title)
        lineFiller = battle.Filler * ((len(self.TEST_MON_2.name) - len(title)) // 2)
        expectedText = lineFiller + title + lineFiller
        self.assertEqual(filledTitle, expectedText)
        
        
    def testExecuteIntro(self):
        battle = self.InitClass()
        title = f"Battle ! {self.TEST_MON_1.name} Vs {self.TEST_MON_2.name}"
        titleLine = battle.edgeSymbol + battle.fillTitleLine(title) + battle.edgeSymbol
        battle.write(titleLine)
        battle.write(str(battle.side1.getActiveMonSpecies()))
        
        longestMonNameLength = battle.calculateLongestMonNameLength()
        paddingLength = longestMonNameLength // 2
        battle.write(' ' * paddingLength + 'VS' + (' ' * paddingLength))
        battle.write(str(battle.side2.getActiveMonSpecies()))
        battle.write(battle.edgeSymbol + (battle.Filler * longestMonNameLength) + battle.edgeSymbol)
        
    def testToString(self):
        newGenericMon = GenericMon('bob', 90, 90, 90, '1,2')
        #currently tests printTypeAcronyms() too
        self.assertEqual(newGenericMon.__str__(), ('bob || 1 / 2 || HP: 90 | ATK: 90 | SPD: 90'))
    
if __name__ == '__main__':
    unittest.main()

