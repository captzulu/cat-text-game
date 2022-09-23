import unittest
from dataObjects.fourSides import FourSides

class fourSidesTest(unittest.TestCase):

    def testInitClass(self):
        newFourSides = FourSides(0, 0, 0, 0)
        self.assertIsInstance(newFourSides, FourSides)
        
    def testFromTuple(self):
        newFourSides = FourSides.fromTuple(tuple((0, 0, 0, 0)))
        self.assertIsInstance(newFourSides, FourSides)
    
    def testGetTuple(self):
        newFourSides = FourSides(0, 0, 0, 0)
        self.assertIsInstance(newFourSides.getTuple(), tuple)
        

if __name__ == '__main__':
    unittest.main()
    
