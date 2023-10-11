import unittest
from gameObjects.sections.map.node import Node
from dataObjects.enums.nodeType import NodeType

class nodeTest(unittest.TestCase):

    def testInitClass(self):
        newNode =  Node(1, NodeType.MARKET, 0, [])
        self.assertIsInstance(newNode, Node)
        
    def testChooseRandomNodeType_nodeTypesWithOdds_goodApproximateResults(self):
        fightOdds : int = 60
        restOdds : int = 30
        marketOdds : int = 10
        randomizedNodeType = f"FIGHT:{fightOdds},REST:{restOdds},MARKET:{marketOdds}"
        results : dict[str, int] = {}
        numberOfTests : int = 2000
        for i in range(1,numberOfTests):
            nodeType : NodeType = Node.chooseRandomNodeType(randomizedNodeType)
            results[nodeType.name] = results[nodeType.name] + 1 if nodeType.name in results else 1
        
        deltaMultiplier = 0.20
        oddsTotal = fightOdds + restOdds + marketOdds
        for nodeTypeWithOdds in randomizedNodeType.split(','):
            nodeTypeWithOdds = nodeTypeWithOdds.split(':')
            nodeTypeName = nodeTypeWithOdds[0]
            nodeTypeOdds = int(nodeTypeWithOdds[1])

            expectedValue = nodeTypeOdds * (numberOfTests / oddsTotal)
            expectedFightDelta = expectedValue * deltaMultiplier
            self.assertAlmostEqual(expectedValue, results[nodeTypeName], None, None, expectedFightDelta)
    
    def testChooseRandomNodeType_nodeTypesWithOddsAndWithout_ignoresNodeTypeWithoutOdds(self):

        randomizedNodeType = f"FIGHT:1,REST:1,CITY,MARKET:1"
        results : dict[str, int] = {}
        numberOfTests : int = 100
        for i in range(1,numberOfTests):
            nodeType : NodeType = Node.chooseRandomNodeType(randomizedNodeType)
            results[nodeType.name] = results[nodeType.name] + 1 if nodeType.name in results else 1

        self.assertEqual(len(results), 3)
        

    def testChooseRandomNodeType_nodeTypesWithoutOdds_goodApproximateResults(self):
        odds : float = 1 / 3
        randomizedNodeType = f"FIGHT,REST,MARKET"
        results : dict[str, int] = {}
        numberOfTests : int = 2000
        for i in range(1,numberOfTests):
            nodeType : NodeType = Node.chooseRandomNodeType(randomizedNodeType)
            results[nodeType.name] = results[nodeType.name] + 1 if nodeType.name in results else 1
        
        deltaMultiplier = 0.20
        oddsTotal = odds * 3

        expectedValue = odds * (numberOfTests / oddsTotal)
        expectedDelta = expectedValue * deltaMultiplier
        for nodeTypeName in randomizedNodeType.split(','):
            self.assertAlmostEqual(expectedValue, results[nodeTypeName], None, None, expectedDelta)
        
if __name__ == '__main__':
    unittest.main()
    
