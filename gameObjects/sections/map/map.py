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
                raise Exception("Nodes_Not_Linked", "Given node is not linked to the previous node")
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
            toPrint += f"column {key} : "
            nodesTxt : list[str] = list()
            for node in column:
                forwardNodesTxt : list[str] = list()
                for forwardNode in node.forwardLinks:
                    forwardNodesTxt.append(f"{forwardNode.id}:{forwardNode.name}")
                nodesTxt.append(f"{node.id}:{node.name} {{" + ", ".join(forwardNodesTxt) + "}")
            toPrint += ", ".join(nodesTxt) + "\n"
        return toPrint