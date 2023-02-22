import unittest
from gameObjects.sections.map.map import Map
from gameObjects.sections.map.node import Node
from gameObjects.sections.map.randomFactory import RandomFactory

class mapTest(unittest.TestCase):
    
    randomFactory : RandomFactory

    def setUp(self) -> None:
        self.randomFactory =  RandomFactory()

    def testInitClass(self):
        newMap = Map()
        self.assertIsInstance(newMap, Map)

    def testInitClass_withTitle_hasTitle(self):
        newMap = Map("poulet")
        self.assertEqual(newMap.title, "poulet")

    def testInitClass_withoutTitle_hasUntitled(self):
        newMap = Map()
        self.assertEqual(newMap.title, "untitled")
    
    def testAdvance_validNode_getDifferentNode(self):
        newMap = Map()
        self.randomFactory.autoGenerateNode(newMap, 0)
        self.randomFactory.autoGenerateNode(newMap, 1)
        self.randomFactory.linkAllNodes(newMap)
        oldNode = newMap.nodes[0][0]
        newMap.activeNode = oldNode
        newMap.advance(newMap.nodes[1][0])
        newNode = newMap.activeNode
        self.assertNotEqual(oldNode, newNode)

    def testAdvance_invalidNode_getNodeAt0(self):
        newMap = self.randomFactory.generateRandomMap(3)
        newMap.advance(Node(100, 'fakeNode', 100))
        expectedNode = newMap.nodes[0][0]
        newNode = newMap.activeNode
        self.assertEqual(expectedNode, newNode)

    def testAdvance_mapLengthOne_mapGetsCompleted(self):
        newMap = self.randomFactory.generateRandomMap(1)
        newMap.advance(newMap.activeNode)
        self.assertTrue(newMap.completed)

    def testAdvance_mapLengthOne_activeNodeStaysSame(self):
        newMap = self.randomFactory.generateRandomMap(1)
        oldNode = newMap.activeNode
        newMap.advance(newMap.activeNode)
        newNode = newMap.activeNode
        self.assertEqual(oldNode, newNode)

if __name__ == '__main__':
    unittest.main()
    
