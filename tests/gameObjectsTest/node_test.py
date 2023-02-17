import unittest
from gameObjects.sections.map.node import Node

class nodeTest(unittest.TestCase):

    def testInitClass(self):
        newNode =  Node(1, 'node 1', 0, [])
        self.assertIsInstance(newNode, Node)
        
if __name__ == '__main__':
    unittest.main()
    
