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

    def testInitClass_withoutTitle_hasUntitled(self):
        newMap = Map()
        self.assertEqual(newMap.title, "untitled")
        
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
    
    def testGenerateRandomMap_LengthZero_success(self):
        newMap = Map.generateRandomMap(0)
        self.assertFalse(0 in newMap.nodes)

    def testGenerateRandomMap_LengthZero_NoActiveNode(self):
        newMap = Map.generateRandomMap(0)
        self.assertFalse(hasattr(newMap, 'activeNode'))

    def testGenerateRandomMap_withLength_getFirstNodeAsActiveNode(self):
        newMap = Map.generateRandomMap(3)
        self.assertIsInstance(newMap.activeNode, Node)
    
    def testAdvance_validNodeIndex_getDifferentNode(self):
        newMap = Map.generateRandomMap(3)
        oldNode = newMap.activeNode
        newMap.advance(0)
        newNode = newMap.activeNode
        self.assertNotEqual(oldNode, newNode)

    def testAdvance_invalidNodeIndex_getNodeAt0(self):
        newMap = Map.generateRandomMap(3)
        newMap.advance(100)
        currentColumnIndex = newMap.activeNode.columnIndex
        expectedNode = newMap.nodes[currentColumnIndex][0]
        newNode = newMap.activeNode
        self.assertEqual(expectedNode, newNode)

    def testAdvance_mapLengthOne_mapGetsCompleted(self):
        newMap = Map.generateRandomMap(1)
        newMap.advance(0)
        self.assertTrue(newMap.completed)

    def testAdvance_mapLengthOne_activeNodeStaysSame(self):
        newMap = Map.generateRandomMap(1)
        oldNode = newMap.activeNode
        newMap.advance(0)
        newNode = newMap.activeNode
        self.assertEqual(oldNode, newNode)

if __name__ == '__main__':
    unittest.main()
    
