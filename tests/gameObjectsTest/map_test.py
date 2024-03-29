import unittest
from unittest import mock
import _globals
from dataFactory import dataFactory
from gameObjects.sections.map.nodeType import NodeType
from gameObjects.sections.map.map import Map
from gameObjects.sections.map.node import Node
from gameObjects.sections.player.player import Player
from gameObjects.sections.map.randomFactory import RandomFactory

class mapTest(unittest.TestCase):

    def setUp(self):
        self.initTestGlobals()
    
    def initTestGlobals(self):
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
    
    @mock.patch('builtins.input', return_value = '1')
    def testAdvance_validNode_getDifferentNode(self, mocked_instance):
        newMap = Map.fromJson('data/maps/map_withLinks.json')
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

        NodeType.fight = mock.MagicMock(return_value=None)
        newMap.advance(newMap.nodes[1][0])
        NodeType.fight.assert_called()

    def testAdvance_mapLengthOne_mapGetsCompleted(self):
        newMap = RandomFactory.generateRandomMap(1)
        newMap.advance(newMap.activeNode)
        self.assertTrue(newMap.status is newMap.status.COMPLETED)

    def testAdvance_mapLengthOne_activeNodeStaysSame(self):
        newMap = RandomFactory.generateRandomMap(1)
        oldNode = newMap.activeNode
        newMap.advance(newMap.activeNode)
        newNode = newMap.activeNode
        self.assertEqual(oldNode, newNode)
    
    def testFromJson_mapWithoutLinks_validMapAndCorrectTitle(self):
        newMap = Map.fromJson('data/maps/map_withoutLinks.json')
        self.assertIsInstance(newMap, Map)
        
        self.assertEqual(newMap.title, 'map_withoutLinks')
        
    def testFromJson_mapWithLinks_validLinks(self):
        newMap = Map.fromJson('data/maps/map_withLinks.json')
        self.assertEqual(newMap.nodes[0][0].forelinks[0], newMap.nodes[1][0])
        self.assertEqual(newMap.nodes[1][0].forelinks[0], newMap.nodes[2][0])
        self.assertEqual(newMap.nodes[1][0].forelinks[1], newMap.nodes[2][1])
        #invalid links are set to 0 instead
        self.assertEqual(newMap.nodes[1][2].forelinks[0], newMap.nodes[2][0])
    
    def testChooseRandomNodeType_mapWithRandomNodeTypes_validMap(self):
        newMap = Map.fromJson('data/maps/map_withRandomNodeTypes.json')
        self.assertIsInstance(newMap, Map)

if __name__ == '__main__':
    unittest.main()
    
