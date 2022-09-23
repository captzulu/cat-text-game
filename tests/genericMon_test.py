import unittest
import _globals
from dataObjects.genericMon import GenericMon
from dataObjects.type import Type
from dataFactory import dataFactory

class genericMonTest(unittest.TestCase):
    def setUp(self):
        self.initTestTypes()
        
    def initTestTypes(self):
        _globals.types = dataFactory.loadClassDictTest('type')

    def testInitClass(self):
        newGenericMon = GenericMon('bob', 90, 90, 90, '1')
        self.assertIsInstance(newGenericMon, GenericMon)
        
    def testToString(self):
        newGenericMon = GenericMon('bob', 90, 90, 90, '1,2')
        #currently tests printTypeAcronyms() too
        self.assertEqual(newGenericMon.__str__(), ('bob || 1 / 2 || HP: 90 | ATK: 90 | SPD: 90'))
    
    def testWeakTo_hasRes(self):
        mon1 = GenericMon('bob', 90, 90, 90, '1')
        self.assertEqual(mon1.weakTo(_globals.types['2']), 0.5)
    
    def testWeakTo_isImm(self):
        mon1 = GenericMon('bob', 90, 90, 90, '1')
        self.assertEqual(mon1.weakTo(_globals.types['3']), 0)
    
    def testWeakTo_isWeak(self):
        mon1 = GenericMon('bob', 90, 90, 90, '1')
        self.assertEqual(mon1.weakTo(_globals.types['4']), 2)
    
    def testWeakTo_WithDoubleType_isDoubleWeak(self):
        mon1a1 = GenericMon('bob', 90, 90, 90, '1,a1')
        self.assertEqual(mon1a1.weakTo(_globals.types['4']), 4)
        
    def testWeakTo_WithDoubleType_isNeutral(self):
        mon13 = GenericMon('bob', 90, 90, 90, '1,3')
        self.assertEqual(mon13.weakTo(_globals.types['4']), 1)
     
    def testWeakTo_WithDoubleType_isImm(self):
        mon12 = GenericMon('bob', 90, 90, 90, '1,2')
        self.assertEqual(mon12.weakTo(_globals.types['4']), 0)
    
    def testWeakTo_WithDoubleType_hasDoubleRes(self):
        mon1a1 = GenericMon('bob', 90, 90, 90, '1,a1')
        self.assertEqual(mon1a1.weakTo(_globals.types['2']), 0.25)

if __name__ == '__main__':
    unittest.main()

