from gameObjects.sections.map.node import Node
from gameObjects.sections.map.randomGenerator import RandomGenerator
import random
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
      
    @classmethod
    def generateRandomMap(cls, length: int):
        newMap = cls()
        i = 0 
        while i < length:
            newMap.randomColumn(i, 1 if i == 0 else 4)
            i += 1
        return newMap
    
    def randomColumn(self, columnIndex: int, maxColumnLength: int) -> None:
        columnLength = random.randint(1, maxColumnLength)
        i = 0
        while i < columnLength:
            self.autoGenerateNode(columnIndex)
            i += 1