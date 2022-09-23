import unittest
from dataObjects.position import Position

class positionTest(unittest.TestCase):

    def testInitClass(self):
        newPosition = Position(0, 0, 0, 0)
        self.assertIsInstance(newPosition, Position)
        
    def testFromTuple(self):
        newPosition = Position.fromTuple(tuple((0, 0, 0, 0)))
        self.assertIsInstance(newPosition, Position)
    
    def testGetTuple(self):
        newPosition = Position(0, 0, 0, 0)
        self.assertIsInstance(newPosition.getTuple(), tuple)

    def testModifyBy(self):
        newPosition = Position(0, 0, 0, 0)
        expectedTuple = (10, 10, 10, 10)
        newPosition.modifyBy(expectedTuple)
        self.assertEqual(newPosition.getTuple(), expectedTuple)
 
if __name__ == '__main__':
    unittest.main()
