from gameObjects.sections.map.node import Node
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
        
    def resetMap(self) -> None:
        self.completed = False
        if (0 in self.nodes and len(self.nodes[0]) > 0):
            self.activeNode = self.nodes[0][0]

        print(f"{self.title} has been reset.")
    
    def getColumnAtIndex(self, columnIndex : int) -> list[Node]:
        if columnIndex < 0 or columnIndex not in self.nodes:
            return []
        return self.nodes[columnIndex]

    def advance(self, node : Node) -> None:
        if self.areLinked(self.activeNode, node):
            self.activeNode = node
            node.executeNode()
        else:
            print("Given node is not linked to the previous node")
            return
        if len(self.activeNode.forwardLinks) == 0:
            self.completed = True
            return
    
    def areLinked(self, firstNode : Node, secondNode : Node) -> bool:
            if secondNode in firstNode.forwardLinks:
                return True
            else:
                return False
            
    def __str__(self) -> str:
        toPrint : str = "Title : " + self.title + "\n"
        for key, column in self.nodes.items():
            toPrint += f"column {key} : " + ", ".join(map(str, column)) + "\n"
        return toPrint