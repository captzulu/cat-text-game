from gameObjects.sections.map.autoGenerator import AutoGenerator
from gameObjects.sections.map.node import Node
import unittest

class AutoGeneratorTest(unittest.TestCase):
    
    def testInitClass(self):
        newAutoGenerator = AutoGenerator()
        self.assertIsInstance(newAutoGenerator, AutoGenerator)
    
    def testGenerateRandomNode(self):
        newAutoGenerator = AutoGenerator()
        columnIndex = 0
        node = newAutoGenerator.generateRandomNode([0, 1, 2], 3, columnIndex)
        self.assertIsInstance(node, Node)