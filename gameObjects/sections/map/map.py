from gameObjects.sections.map.node import Node
from gameObjects.sections.map.randomGenerator import RandomGenerator
import itertools

class Map():
    nodes : dict[int, list[Node]] = dict()
    
    def __init__(self):
        self.nodeIdGenerator = itertools.count()
    
    def getColumnAtIndex(self, columnIndex : int) -> list[Node]:
        if columnIndex < 0 or columnIndex not in self.nodes:
            return []
        return self.nodes[columnIndex]
    
    def getColumnIds(self, column : list[Node]) -> list[int]:
        ids : list[int] = list()
        for node in column:
            ids.append(node.id)
        return ids
    
    def autoGenerateNode(self, columnIndex : int) -> int:
        previousColumn = self.getColumnAtIndex(columnIndex - 1)
        previousColumnIds = self.getColumnIds(previousColumn)
        randomGenerator = RandomGenerator()

        if columnIndex not in self.nodes:
            self.nodes[columnIndex] = list()
            
        newNode = randomGenerator.generateRandomNode(previousColumnIds, next(self.nodeIdGenerator), columnIndex)
        self.nodes[columnIndex].append(newNode)
        return newNode.id