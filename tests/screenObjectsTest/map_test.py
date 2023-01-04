import unittest
from screenObjects.map import Map

class mapTest(unittest.TestCase):

    @unittest.skip("not testable")
    def testInitClass(self) -> None:
        newMap: Map = Map("Poulet")
        self.assertIsInstance(newMap, Map)
        
if __name__ == '__main__':
    unittest.main()
    
