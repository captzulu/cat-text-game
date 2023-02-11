import unittest
from gameObjects.sections.map.node import Node

class nodeTest(unittest.TestCase):

    def testInitClass(self):
        newNode =  Node(1, 'node 1', 0, [])
        self.assertIsInstance(newNode, Node)
        
    def testRandomName(self):
        self.assertIsInstance(Node.randomName(), str)
    
    def testRandomBackLinks_emptyPrevious(self):
        self.assertIsInstance(Node.randomBackLinks([]), list)

    def testRandomBackLinks_PopulatedPrevious(self):
        self.assertIsInstance(Node.randomBackLinks([1, 2, 3]), list)
        
    def testGenerateRandomNode(self):
        columnIndex = 0
        node = Node.generateRandomNode(3, columnIndex, [0, 1, 2])
        self.assertIsInstance(node, Node)
        
if __name__ == '__main__':
    unittest.main()
    
