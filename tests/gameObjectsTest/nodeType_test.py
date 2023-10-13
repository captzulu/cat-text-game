import unittest
from unittest import mock
import _globals
from dataFactory import dataFactory
from gameObjects.sections.map.node import Node
from gameObjects.sections.map.nodeType import NodeType
from gameObjects.sections.player.player import Player
from gameObjects.sections.battle.battle import Battle

class nodeTypeTest(unittest.TestCase):
    
    def setUp(self):
        self.initTestGlobals()
        _globals.player = Player('test')
        _globals.testMode = True
        
    def initTestGlobals(self):
        _globals.types = dataFactory.loadClassDictTest('type')
        _globals.moves = dataFactory.loadClassDictTest('move')
        _globals.genericMons = dataFactory.loadClassDictTest('genericMon')
    
    @mock.patch('builtins.input', return_value = '1')    
    def testFight_executeFightNode_getBattle(self, mocked_instance):
        _globals.debug = False
        _globals.player.chooseMon(1)
        battle = NodeType.FIGHT.execute()
        self.assertIsInstance(battle, Battle)
        
if __name__ == '__main__':
    unittest.main()
    
