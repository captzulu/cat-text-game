import unittest
from screenObjects.map import Map

class mapTest(unittest.TestCase):

    def testInitClass(self):
        newMap = Map("Poulet")
        self.assertIsInstance(newMap, Map)
        
if __name__ == '__main__':
    unittest.main()
    
