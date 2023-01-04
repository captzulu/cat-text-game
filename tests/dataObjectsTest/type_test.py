import unittest
from dataObjects.type import Type

class typeTest(unittest.TestCase):

    def testInitClass(self):
        newType = self.createType()
        self.assertIsInstance(newType, Type)

    def testCheckTypeModifier_superEffective(self):
        newType = self.createType()
        self.assertEqual(newType.checkTypeModifier("dark"), 2)

    def testCheckTypeModifier_resisted(self):
        newType = self.createType()
        self.assertEqual(newType.checkTypeModifier("psy"), 0.5)

    def testCheckTypeModifier_neutral(self):
        newType = self.createType()
        self.assertEqual(newType.checkTypeModifier("fake"), 1)
        
    def testCheckTypeModifier_immune(self):
        newType = self.createType()
        self.assertEqual(newType.checkTypeModifier("wat"), 0)

    def createType(self) -> Type:
        return Type("bob", "dark", "psy", "wat", "")
 # type: ignore
if __name__ == '__main__':
    unittest.main()
