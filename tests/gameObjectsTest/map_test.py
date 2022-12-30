import unittest
from gameObjects.sections.map.map import Map
from gameObjects.sections.map.node import Node

class mapTest(unittest.TestCase):

    def testInitClass(self):
        newMap = Map()
        self.assertIsInstance(newMap, Map)

    def testInitClass_withTitle_hasTitle(self):
        newMap = Map("poulet")
        self.assertEqual(newMap.title, "poulet")
        
    def testAutoGenerateNode_twoColumns_linkedNodes(self):
        newMap = Map()
        expectedBackLinks = [newMap.autoGenerateNode(0)]
        newMap.autoGenerateNode(1)
        actualBackLinks = newMap.nodes[1][0].backLinks
        self.assertEqual(actualBackLinks, expectedBackLinks)

    def testAutoGenerateNode_twoColumns_incrementingId(self):
        newMap = Map()
        newMap.autoGenerateNode(0)
        actualId = newMap.autoGenerateNode(1)
        expectedId = 1
        self.assertEqual(actualId, expectedId)
        
    def testRandomColumn_firstColumn_success(self):
        newMap = Map()
        newMap.randomColumn(0, 1)
        
        self.assertIsInstance(newMap.nodes[0][0], Node)
        
    def testRandomColumn_multipleColumns_success(self):
        newMap = Map()
        maxLength = 4
        newMap.randomColumn(0, 1)
        newMap.randomColumn(1, maxLength)
        newMap.randomColumn(2, maxLength)
        
        self.assertTrue(len(newMap.nodes[1]) <= maxLength)
        self.assertTrue(len(newMap.nodes[1]) != 0)
        self.assertTrue(len(newMap.nodes[2]) <= maxLength)
        self.assertTrue(len(newMap.nodes[2]) != 0)
        
    def testGenerateRandomMap_success(self):
        newMap = Map.generateRandomMap(4)
        
        self.assertEqual(len(newMap.nodes[0]), 1)
        self.assertEqual(len(newMap.nodes), 4)

if __name__ == '__main__':
    unittest.main()
    
