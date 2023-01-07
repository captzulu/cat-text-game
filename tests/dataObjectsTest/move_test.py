import unittest
import _globals
from dataFactory import dataFactory
from dataObjects.move import Move

class moveTest(unittest.TestCase):
    
    def setUp(self):
        self.initTestTypes()
    
    def initTestTypes(self):
        _globals.types = dataFactory.loadClassDictTest('type')
        
    def testLoadFile(self):
        _globals.types = dataFactory.loadClassDict('type')
        moves : dict[str, object] = dataFactory.loadClassDict('move')
        self.assertIsInstance(moves['0'], Move)

    def testInitClass(self):
        newAttack = Move("Slash", 70, '1')
        self.assertIsInstance(newAttack, Move)
        
if __name__ == '__main__':
    unittest.main()