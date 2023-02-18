from gameObjects.sections.map.node import Node
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

    def advance(self, nodeIndex : int) -> None:
        nextColumnIndex : int = self.activeNode.columnIndex + 1
        if nextColumnIndex in self.nodes:
            column = self.nodes[nextColumnIndex]
            maxIndex = (len(column) - 1)
            newNode = column[0] if maxIndex < nodeIndex else column[nodeIndex]
            if self.areLinked(self.activeNode, newNode):
                self.activeNode = newNode
            else:
                print("Given node is not linked to the previous node")
                return
        else:
            self.completed = True
    
    def areLinked(self, firstNode : Node, secondNode : Node) -> bool:
            if firstNode in secondNode.backLinks:
                return True
            else:
                return False
            
    def __str__(self) -> str:
        toPrint : str = "Title : " + self.title + "\n"
        for key, column in self.nodes.items():
            toPrint += f"column {key} : " + ", ".join(map(str, column)) + "\n"
        return toPrint