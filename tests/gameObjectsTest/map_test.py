import unittest
from gameObjects.sections.map.map import Map
from gameObjects.sections.map.node import Node

class mapTest(unittest.TestCase):

    def testInitClass(self):
        newMap = Map({0 : Node(1, 'node 1', [], [2])})
        self.assertIsInstance(newMap, Map)
        
        

if __name__ == '__main__':
    unittest.main()
    
