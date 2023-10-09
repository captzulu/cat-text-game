import _globals
from dataObjects.enums.nodeType import NodeType
from typing import Optional

class Node():
    def __init__(self, id : int, type : NodeType, columnIndex : int, forelinks : Optional[list]=None):
        self.id : int = id
        self.name : str = type.value
        self.nodeType : NodeType = type
        self.columnIndex : int = columnIndex

        if forelinks is None:
            self.forelinks : list[Node] = list()
        else:
            self.forelinks : list[Node] = forelinks
    
    def __str__(self) -> str:
        forelinks : list[str] = list()
        for forwardNode in self.forelinks:
            forelinks.append((f"{forwardNode.id}:" if _globals.debug else "") + f"{forwardNode.name}")
            
        return (f"{self.id}:" if _globals.debug else "" ) + f"{self.name} {{" + ", ".join(forelinks) + "}"
    
    def executeNode(self):
        self.nodeType.execute()
        return