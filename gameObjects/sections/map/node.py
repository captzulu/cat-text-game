import random
from gameObjects.sections.map.nodeEvents import NodeEvents
from typing import Optional

class Node():
    def __init__(self, id : int, name : str, columnIndex : int, backLinks : list[int], forwardLinks : Optional[list[int]]=None):
        self.id : int = id
        self.name : str = name 
        self.backLinks : list[int] = backLinks 
        if forwardLinks is None:
            self.forwardLinks : list[int] = list()
        else:
            self.forwardLinks : list[int] = forwardLinks
        self.columnIndex : int = columnIndex
    
    def __str__(self) -> str:
        return f"{{{self.id}:{self.name} {self.forwardLinks}}}"

    @staticmethod
    def randomName() -> str:
        results : list[str] = random.choices(NodeEvents.NAME_LIST, weights=[1, 1, 8, 1, 5])
        return results[0]

    @staticmethod
    def randomBackLinks(previousIds : list[int]) -> list[int]:
        if len(previousIds) == 0:
            return []

        amount : int = random.choices([1, 2, 3], weights=[2, 5, 3])[0]
        results : list[int] = list()
        while amount > 0 and len(previousIds) > 0:
            pickedId: int = random.choice(previousIds)
            results.append(pickedId)
            previousIds.remove(pickedId)
            amount -= 1
        return results
    
    def executeNode(self):
        if self.name == 'fight':
            NodeEvents.enterRandomFight()
            return