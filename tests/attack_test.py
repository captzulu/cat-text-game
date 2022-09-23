import unittest
from dataObjects.attack import Attack
from dataObjects.type import Type 

class attackTest(unittest.TestCase):

    def testInitClass(self):
        newAttack = Attack("Slash", 70, self.createType())
        self.assertIsInstance(newAttack, Attack)
        
    def createType(self) -> Type:
        return Type("bob", "dark", "psy", "", "")
        

if __name__ == '__main__':
    unittest.main()