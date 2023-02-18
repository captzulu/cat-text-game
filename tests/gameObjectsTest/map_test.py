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
    
    def testAdvance_validNodeIndex_getDifferentNode(self):
        newMap = self.randomFactory.generateRandomMap(3)
        oldNode = newMap.activeNode
        newMap.advance(0)
        newNode = newMap.activeNode
        self.assertNotEqual(oldNode, newNode)

    def testAdvance_invalidNodeIndex_getNodeAt0(self):
        newMap = self.randomFactory.generateRandomMap(3)
        newMap.advance(100)
        currentColumnIndex = newMap.activeNode.columnIndex
        expectedNode = newMap.nodes[currentColumnIndex][0]
        newNode = newMap.activeNode
        self.assertEqual(expectedNode, newNode)

    def testAdvance_mapLengthOne_mapGetsCompleted(self):
        newMap = self.randomFactory.generateRandomMap(1)
        newMap.advance(0)
        self.assertTrue(newMap.completed)

    def testAdvance_mapLengthOne_activeNodeStaysSame(self):
        newMap = self.randomFactory.generateRandomMap(1)
        oldNode = newMap.activeNode
        newMap.advance(0)
        newNode = newMap.activeNode
        self.assertEqual(oldNode, newNode)
    
    def testAdvance_NodesAreLinked_success(self):
        newMap = Map()
        self.randomFactory.autoGenerateNode(newMap, 0)
        newMap.activeNode = newMap.nodes[0][0]
        nextNode : Node = Node(2, "linkedNode", 1, [1], [])
        newMap.nodes[1] = [nextNode]
        newMap.advance(0)

    def testAdvance_NodesNotLinked_dontMove(self):
        newMap = Map()
        self.randomFactory.autoGenerateNode(newMap, 0)
        newMap.activeNode = newMap.nodes[0][0]
        nextNode : Node = Node(2, "linkedNode", 1, [], [])
        newMap.nodes[1] = [nextNode]
        newMap.advance(10)
        self.assertEqual(newMap.activeNode, newMap.nodes[0][0])

if __name__ == '__main__':
    unittest.main()
    
