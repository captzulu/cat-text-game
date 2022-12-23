from gameObjects.sections.map.node import Node
import itertools

class Map():
    nodes : dict[int, list[Node]] = dict()
    
    def __init__(self):
        self.nodeIdGenerator = itertools.count()
    
    def autoGenerateNode(self, columnIndex : int) -> int:
        name = Node.randomName()
        previousRow = self.getRowAtIndex(columnIndex - 1)
        backLinks = Node.randomBackLinks(self.getRowIds(previousRow))
        
        if columnIndex not in self.nodes:
            self.nodes[columnIndex] = list()

        newNode = Node(next(self.nodeIdGenerator), name, columnIndex, backLinks)
        self.nodes[columnIndex].append(newNode)
        return newNode.id
    
    def getRowAtIndex(self, columnIndex : int) -> list[Node]:
        if columnIndex < 0 or columnIndex not in self.nodes:
            return []
        return self.nodes[columnIndex]
    
    def getRowIds(self, row : list[Node]) -> list[int]:
        ids : list[int] = list()
        for node in row:
            ids.append(node.id)
        return ids