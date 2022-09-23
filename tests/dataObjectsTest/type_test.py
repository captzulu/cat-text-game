import unittest
from dataObjects.type import Type

class typeTest(unittest.TestCase):

    def testInitClass(self):
        newType = self.createType()
        self.assertIsInstance(newType, Type)
        
    def testGetHitDamageModifier(self):
        newType = self.createType()
        self.assertEqual(newType.checkTypeModifier("dark"), 2)
        
    def createType(self) -> Type:
        return Type("bob", "dark", "psy", "", "")

if __name__ == '__main__':
    unittest.main()
