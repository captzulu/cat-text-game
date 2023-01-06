import unittest
import _globals
from dataFactory import dataFactory
from dataObjects.attack import Attack

class attackTest(unittest.TestCase):
    
    def setUp(self):
        self.initTestTypes()
    
    def initTestTypes(self):
        _globals.types = dataFactory.loadClassDictTest('type')
        
    def testLoadFile(self):
        _globals.types = dataFactory.loadClassDict('type')
        attacks : dict[str, object] = dataFactory.loadClassDict('attack')
        self.assertIsInstance(attacks['0'], Attack)

    def testInitClass(self):
        newAttack = Attack("Slash", 70, '1')
        self.assertIsInstance(newAttack, Attack)
        
if __name__ == '__main__':
    unittest.main()