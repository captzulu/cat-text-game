from gameObjects.sections.map.node import Node
import itertools

class Map():
    nodes : dict[int, list[Node]] = dict()
    nodeIdGenerator = itertools.count()
    
    def __init__(self):
        return
    
    def autoGenerateNode(self, rowIndex : int) -> int:
        name = Node.randomName()
        previousRow = self.getRowAtIndex(rowIndex - 1)
        backLinks = Node.randomBackLinks(self.getRowIds(previousRow))
        
        if rowIndex not in self.nodes:
            self.nodes[rowIndex] = list()

        newNode = Node(next(self.nodeIdGenerator), name, rowIndex, backLinks)
        self.nodes[rowIndex].append(newNode)
        return newNode.id
    
    def getRowAtIndex(self, rowIndex : int) -> list[Node]:
        if rowIndex < 0 or rowIndex not in self.nodes:
            return []
        return self.nodes[rowIndex]
    
    def getRowIds(self, row : list[Node]) -> list[int]:
        ids : list[int] = list()
        for node in row:
            ids.append(node.id)
        return ids
    
    