from gameObjects.sections.map.node import Node
from gameObjects.sections.map.autoGenerator import AutoGenerator
import itertools

class Map():
    nodes : dict[int, list[Node]] = dict()
    
    def __init__(self):
        self.nodeIdGenerator = itertools.count()
    
    def getRowAtIndex(self, columnIndex : int) -> list[Node]:
        if columnIndex < 0 or columnIndex not in self.nodes:
            return []
        return self.nodes[columnIndex]
    
    def getColumnIds(self, column : list[Node]) -> list[int]:
        ids : list[int] = list()
        for node in column:
            ids.append(node.id)
        return ids
    
    def autoGenerateNode(self, columnIndex : int) -> int:
        previousColumn = self.getRowAtIndex(columnIndex - 1)
        previousColumnIds = self.getRowIds(previousColumn)
        autoGenerator = AutoGenerator()

        newNode = autoGenerator.autoGenerateNode(previousColumnIds, next(self.nodeIdGenerator), columnIndex)
        
        self.nodes[columnIndex].append(newNode)
        return newNode.id