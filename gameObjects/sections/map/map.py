from gameObjects.sections.map.node import Node
from gameObjects.sections.map.randomGenerator import RandomGenerator
import random
import itertools

class Map():
    nodes : dict[int, list[Node]]
    title : str
    
    def __init__(self, title : str = "untitled"):
        self.nodeIdGenerator = itertools.count()
        self.title = title
        self.nodes = dict()
    
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
    def generateRandomMap(cls, length: int, title: str = ""):
        newMap = cls(title)
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
            
    def __str__(self) -> str:
        toPrint : str = "Title : " + self.title + "\n"
        for key, column in self.nodes.items():
            toPrint += f"column {key} : " + ", ".join(map(str, column)) + "\n"
        return toPrint