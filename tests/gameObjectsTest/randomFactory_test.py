import unittest

from gameObjects.sections.map.node import Node
from gameObjects.sections.map.map import Map
from gameObjects.sections.map.randomFactory import RandomFactory
class randomFactoryTest(unittest.TestCase):
    
    randomFactory : RandomFactory

    def setUp(self) -> None:
        self.randomFactory =  RandomFactory()

    def testInitClass(self):
        self.assertIsInstance(self.randomFactory, RandomFactory)
        
    def testRandomName(self):
        self.assertIsInstance(self.randomFactory.randomName(), str)
    
    def testRandomBackLinks_emptyPrevious(self):
        self.assertIsInstance(self.randomFactory.randomBackLinks([]), list)

    def testRandomBackLinks_PopulatedPrevious(self):
        newMap = Map()
        self.randomFactory.autoGenerateNode(newMap, 0)
        self.assertIsInstance(self.randomFactory.randomBackLinks(newMap.nodes[0]), list)
        
    def testAutoGenerateNode(self):
        columnIndex = 0
        newMap = Map()
        self.randomFactory.autoGenerateNode(newMap, columnIndex)
        self.assertIsInstance(newMap.nodes[0][0], Node)
        
    def testAutoGenerateNode_twoColumns_linkedNodes(self):
        newMap = Map()
        self.randomFactory.autoGenerateNode(newMap, 0)
        expectedBackLinks = [newMap.nodes[0][0]]
        self.randomFactory.autoGenerateNode(newMap, 1)
        actualBackLinks = newMap.nodes[1][0].backLinks
        self.assertEqual(actualBackLinks, expectedBackLinks)

    def testAutoGenerateNode_twoColumns_incrementingId(self):
        newMap = Map()
        self.randomFactory.autoGenerateNode(newMap, 0)
        self.randomFactory.autoGenerateNode(newMap, 1)
        actualId = newMap.nodes[1][0].id
        expectedId = 2
        self.assertEqual(actualId, expectedId)
        
    def testGenerateRandomColumn_firstColumn_success(self):
        newMap = Map()
        self.randomFactory.generateRandomColumn(newMap, 0, 1)
        
        self.assertIsInstance(newMap.nodes[0][0], Node)
        
    def testGenerateRandomColumn_multipleColumns_success(self):
        newMap = Map()
        maxLength = 4
        self.randomFactory.generateRandomColumn(newMap, 0, 1)
        self.randomFactory.generateRandomColumn(newMap, 1, maxLength)
        self.randomFactory.generateRandomColumn(newMap, 2, maxLength)
        
        self.assertTrue(len(newMap.nodes[1]) <= maxLength)
        self.assertTrue(len(newMap.nodes[1]) != 0)
        self.assertTrue(len(newMap.nodes[2]) <= maxLength)
        self.assertTrue(len(newMap.nodes[2]) != 0)
        
    def testGenerateRandomMap_success(self):
        newMap = self.randomFactory.generateRandomMap(4)
        
        self.assertEqual(len(newMap.nodes[0]), 1)
        self.assertEqual(len(newMap.nodes), 4)
    
    def testGenerateRandomMap_LengthZero_success(self):
        newMap = self.randomFactory.generateRandomMap(0)
        self.assertFalse(0 in newMap.nodes)

    def testGenerateRandomMap_LengthZero_NoActiveNode(self):
        newMap = self.randomFactory.generateRandomMap(0)
        self.assertFalse(hasattr(newMap, 'activeNode'))

    def testGenerateRandomMap_withLength_getFirstNodeAsActiveNode(self):
        newMap = self.randomFactory.generateRandomMap(3)
        self.assertIsInstance(newMap.activeNode, Node)
        
if __name__ == '__main__':
    unittest.main()
    
