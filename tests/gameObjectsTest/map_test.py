import unittest
from gameObjects.sections.map.map import Map
from gameObjects.sections.map.node import Node

class mapTest(unittest.TestCase):

    def testInitClass(self):
        newMap = Map()
        self.assertIsInstance(newMap, Map)
        
    def testAutoGenerate_twoColumns_linkedNodes(self):
        newMap = Map()
        expectedBackLinks = [newMap.autoGenerateNode(0)]
        newMap.autoGenerateNode(1)
        actualBackLinks = newMap.nodes[1][0].backLinks
        self.assertEqual(actualBackLinks, expectedBackLinks)

    def testAutoGenerate_twoColumns_incrementingId(self):
        newMap = Map()
        newMap.autoGenerateNode(0)
        actualId = newMap.autoGenerateNode(1)
        expectedId = 1
        self.assertEqual(actualId, expectedId)
        
    def testRandomColumn_firstColumn_success(self):
        newMap = Map()
        newMap.randomColumn(0, 1)
        
        self.assertIsInstance(newMap.nodes[0][0], Node)

if __name__ == '__main__':
    unittest.main()
    
