import unittest
from gameObjects.sections.map.map import Map

class mapTest(unittest.TestCase):

    def testInitClass(self):
        newMap = Map()
        self.assertIsInstance(newMap, Map)
    
    def testAutoGenerate(self):
        newMap = Map()
        rowIndex = 0
        actualId = newMap.autoGenerateNode(rowIndex)
        expectedId = 0
        self.assertEqual(len(newMap.nodes), 1)
        self.assertEqual(actualId, expectedId)
        
    def testAutoGenerate_twoRows_incrementingId(self):
        newMap = Map()
        newMap.autoGenerateNode(0)
        actualId = newMap.autoGenerateNode(1)
        expectedId = 1
        self.assertEqual(actualId, expectedId)
        
    def testAutoGenerate_twoRows_linkedNodes(self):
        newMap = Map()
        expectedId = newMap.autoGenerateNode(0)
        newMap.autoGenerateNode(1)
        actualId = newMap.nodes[1][0].backLinks
        self.assertEqual(actualId, [expectedId])       
        

if __name__ == '__main__':
    unittest.main()
    
