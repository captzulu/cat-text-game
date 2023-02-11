from gameObjects.sections.map.node import Node
from gameObjects.sections.map.randomGenerator import RandomGenerator
import random
import itertools

class Map():
    nodes : dict[int, list[Node]]
    title : str
    activeNode : Node
    completed : bool
    
    def __init__(self, title : str = "untitled"):
        self.nodeIdGenerator = itertools.count(1)
        self.title = title
        self.nodes = dict()
        self.completed = False
    
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

        if columnIndex not in self.nodes:
            self.nodes[columnIndex] = list()
            
        newNode: Node = Node.generateRandomNode(next(self.nodeIdGenerator), columnIndex, previousColumnIds)
        self.nodes[columnIndex].append(newNode)
        return newNode.id
      
    @classmethod
    def generateRandomMap(cls, length: int, title: str = ""):
        newMap = cls(title)
        i = 0 
        while i < length:
            newMap.randomColumn(i, 1 if i == 0 else 4)
            i += 1
        if 0 in newMap.nodes and len(newMap.nodes[0]) >= 1:
            newMap.activeNode = newMap.nodes[0][0]
        return newMap
    
    def randomColumn(self, columnIndex: int, maxColumnLength: int) -> None:
        columnLength = random.randint(1, maxColumnLength)
        i = 0
        while i < columnLength:
            self.autoGenerateNode(columnIndex)
            i += 1
    
    def advance(self, nodeIndex : int) -> None:
        nextColumnIndex : int = self.activeNode.columnIndex + 1
        if nextColumnIndex in self.nodes:
            column = self.nodes[nextColumnIndex]
            maxIndex = (len(column) - 1)
            newNode = column[0] if maxIndex < nodeIndex else column[nodeIndex]
            if self.areLinked(self.activeNode, newNode):
                self.activeNode = newNode
            else:
                raise Exception("Nodes_Not_Linked", "Given node is not linked to the previous node")
        else:
            self.completed = True
    
    def areLinked(self, firstNode : Node, secondNode : Node) -> bool:
            if firstNode.id in secondNode.backLinks:
                return True
            else:
                return False
            
    def __str__(self) -> str:
        toPrint : str = "Title : " + self.title + "\n"
        for key, column in self.nodes.items():
            toPrint += f"column {key} : " + ", ".join(map(str, column)) + "\n"
        return toPrint