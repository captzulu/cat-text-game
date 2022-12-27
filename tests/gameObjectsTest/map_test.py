import unittest
from gameObjects.sections.map.map import Map

class mapTest(unittest.TestCase):

    def testInitClass(self):
        newMap = Map()
        self.assertIsInstance(newMap, Map)
        
    def testGetRowAtIndex(self):
        newMap = Map()
        columnIndex = 0
        actualId = newMap.autoGenerateNode(columnIndex)
        expectedId = 0
        self.assertEqual(len(newMap.nodes), 1)
        self.assertEqual(actualId, expectedId)
        
    def testAutoGenerate_twoRows_linkedNodes(self):
        newMap = Map()
        expectedBackLinks = [newMap.autoGenerateNode(0)]
        newMap.autoGenerateNode(1)
        actualBackLinks = newMap.nodes[1][0].backLinks
        self.assertEqual(actualBackLinks, expectedBackLinks)
    
    def testAutoGenerate_twoRows_incrementingId(self):
        newMap = Map()
        newMap.autoGenerateNode(0)
        actualId = newMap.autoGenerateNode(1)
        expectedId = 1
        self.assertEqual(actualId, expectedId)   

if __name__ == '__main__':
    unittest.main()
    
