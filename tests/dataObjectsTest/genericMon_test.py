import unittest
import _globals
from dataObjects.genericMon import GenericMon
from dataFactory import dataFactory

class genericMonTest(unittest.TestCase):
    def setUp(self):
        self.initTestTypes()
        
    def initTestTypes(self):
        _globals.types = dataFactory.loadClassDictTest('type')
        _globals.moves = dataFactory.loadClassDictTest('move')

    def __newGenericMon(self, type : str):
        return GenericMon('bob', 90, 90, 90, type, '1')
        
    def testInitClass(self):
        self.assertIsInstance(self.__newGenericMon('1'), GenericMon)
        
    def testToString(self):
        newGenericMon = str(self.__newGenericMon('1,2'))
        #currently tests printTypeAcronyms() too
        self.assertEqual(newGenericMon, ('bob || 1/2 || HP: 90 | ATK: 90 | SPD: 90'))
    
    def testWeakTo_hasRes(self):
        mon1 = self.__newGenericMon('1')
        self.assertEqual(mon1.weakTo(_globals.types['2']), 0.5)
    
    def testWeakTo_isImm(self):
        mon1 = self.__newGenericMon('1')
        self.assertEqual(mon1.weakTo(_globals.types['3']), 0)
    
    def testWeakTo_isWeak(self):
        mon1 = self.__newGenericMon('1')
        self.assertEqual(mon1.weakTo(_globals.types['4']), 2)
    
    def testWeakTo_WithDoubleType_isDoubleWeak(self):
        mon1a1 = self.__newGenericMon('1,a1')
        self.assertEqual(mon1a1.weakTo(_globals.types['4']), 4)
        
    def testWeakTo_WithDoubleType_isNeutral(self):
        mon13 = self.__newGenericMon('1,3')
        self.assertEqual(mon13.weakTo(_globals.types['4']), 1)
     
    def testWeakTo_WithDoubleType_isImm(self):
        mon12 = self.__newGenericMon('1,2')
        self.assertEqual(mon12.weakTo(_globals.types['4']), 0)
    
    def testWeakTo_WithDoubleType_hasDoubleRes(self):
        mon1a1 = self.__newGenericMon('1,a1')
        self.assertEqual(mon1a1.weakTo(_globals.types['2']), 0.25)

if __name__ == '__main__':
    unittest.main()

