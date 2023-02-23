import _globals
from gameObjects.sections.map.nodeEvents import NodeEvents
from dataObjects.enums.nodeType import NodeType
from typing import Optional

class Node():
    def __init__(self, id : int, type : NodeType, columnIndex : int, backLinks : Optional[list]=None, forwardLinks : Optional[list]=None):
        self.id : int = id
        self.name : str = type.value
        self.nodeType : NodeType = type
        self.columnIndex : int = columnIndex

        if backLinks is None:
            self.backLinks : list[Node] = list()
        else:
            self.backLinks : list[Node] = backLinks

        if forwardLinks is None:
            self.forwardLinks : list[Node] = list()
        else:
            self.forwardLinks : list[Node] = forwardLinks
    
    def __str__(self) -> str:
        forwardLinks : list[str] = list()
        for forwardNode in self.forwardLinks:
            forwardLinks.append((f"{forwardNode.id}:" if _globals.debug else "") + f"{forwardNode.name}")
            
        return (f"{self.id}:" if _globals.debug else "" ) + f"{self.name} {{" + ", ".join(forwardLinks) + "}"
    
    def executeNode(self):
        if self.nodeType == NodeType.FIGHT:
            NodeEvents.enterRandomFight()
        elif self.nodeType == NodeType.CHICKENS:
            NodeEvents.chickenEvent()
        return