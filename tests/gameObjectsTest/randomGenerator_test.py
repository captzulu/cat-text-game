from gameObjects.sections.map.randomGenerator import RandomGenerator
from gameObjects.sections.map.node import Node
import unittest

class RandomGeneratorTest(unittest.TestCase):
    
    def testInitClass(self):
        newRandomGenerator = RandomGenerator()
        self.assertIsInstance(newRandomGenerator, RandomGenerator)
    
    def testGenerateRandomNode(self):
        newRandomGenerator = RandomGenerator()
        columnIndex = 0
        node = newRandomGenerator.generateRandomNode([0, 1, 2], 3, columnIndex)
        self.assertIsInstance(node, Node)