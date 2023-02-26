import unittest
from unittest import mock
import _globals
from dataFactory import dataFactory
from dataObjects.enums.nodeType import NodeType
from gameObjects.sections.map.map import Map
from gameObjects.sections.map.node import Node
from gameObjects.sections.map.nodeEvents import NodeEvents
from gameObjects.sections.player.player import Player
from gameObjects.sections.map.randomFactory import RandomFactory

class mapTest(unittest.TestCase):

    def setUp(self):
        self.initTestGlobals()
    
    @mock.patch('builtins.input', return_value = '1')
    def initTestGlobals(self, mocked_instance):
        _globals.types = dataFactory.loadClassDictTest('type')
        _globals.moves = dataFactory.loadClassDictTest('move')
        _globals.genericMons = dataFactory.loadClassDictTest('genericMon')
        _globals.player = Player('test')

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
        RandomFactory.autoGenerateNode(newMap, 0)
        RandomFactory.autoGenerateNode(newMap, 1)
        RandomFactory.linkAllNodes(newMap)
        oldNode = newMap.nodes[0][0]
        newMap.activeNode = oldNode
        newMap.advance(newMap.nodes[1][0])
        newNode = newMap.activeNode
        self.assertNotEqual(oldNode, newNode)

    def testAdvance_invalidNode_dontMove(self):
        newMap = RandomFactory.generateRandomMap(3)
        newMap.advance(Node(100, NodeType.FIGHT, 100))
        expectedNode = newMap.nodes[0][0]
        newNode = newMap.activeNode
        self.assertEqual(expectedNode, newNode)
        
    @mock.patch('builtins.input', return_value = '1')
    def testAdvance_fightNode_startFight(self, mocked_instance):
        newMap = Map()
        RandomFactory.autoGenerateNode(newMap, 0)
        newMap.nodes[1] = [Node(2, NodeType.FIGHT, 1)]
        newMap.activeNode = newMap.nodes[0][0]
        RandomFactory.linkAllNodes(newMap)

        NodeEvents.fight = mock.MagicMock(return_value=None)
        newMap.advance(newMap.nodes[1][0])
        NodeEvents.fight.assert_called()

    def testAdvance_mapLengthOne_mapGetsCompleted(self):
        newMap = RandomFactory.generateRandomMap(1)
        newMap.advance(newMap.activeNode)
        self.assertTrue(newMap.completed)

    def testAdvance_mapLengthOne_activeNodeStaysSame(self):
        newMap = RandomFactory.generateRandomMap(1)
        oldNode = newMap.activeNode
        newMap.advance(newMap.activeNode)
        newNode = newMap.activeNode
        self.assertEqual(oldNode, newNode)

if __name__ == '__main__':
    unittest.main()
    
