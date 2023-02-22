import unittest
from gameObjects.sections.map.node import Node
from dataObjects.enums.nodeType import NodeType

class nodeTest(unittest.TestCase):

    def testInitClass(self):
        newNode =  Node(1, NodeType.MARKET, 0, [])
        self.assertIsInstance(newNode, Node)
        
if __name__ == '__main__':
    unittest.main()
    
