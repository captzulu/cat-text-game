import random
from gameObjects.sections.map.nodeEvents import NodeEvents
from typing import Optional

class Node():
    def __init__(self, id : int, name : str, columnIndex : int, backLinks : list, forwardLinks : Optional[list]=None):
        self.id : int = id
        self.name : str = name 
        self.backLinks : list[Node] = backLinks 
        if forwardLinks is None:
            self.forwardLinks : list[Node] = list()
        else:
            self.forwardLinks : list[Node] = forwardLinks
        self.columnIndex : int = columnIndex
    
    def __str__(self) -> str:
        return f"{{{self.id}:{self.name} " + ", ".join(map(str, self.forwardLinks)) + "}}}"
    
    def executeNode(self):
        if self.name == 'fight':
            NodeEvents.enterRandomFight()
        return