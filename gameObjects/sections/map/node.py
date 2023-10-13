import _globals
from gameObjects.sections.map.nodeType import NodeType
import random
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
    
    @staticmethod
    def chooseRandomNodeType(randomizedNodeType : str) -> NodeType:
        if ":" in randomizedNodeType:
            return Node.parseWithOdds(randomizedNodeType)
        else:
            return Node.parseWithoutOdds(randomizedNodeType)        
    
    @staticmethod
    def parseWithOdds(nodeTypeWithOdds : str) -> NodeType:
        choices : dict[str, int] = {}
        for nodeType in nodeTypeWithOdds.split(','):
            if ':' in nodeType:
                nodeType = nodeType.split(':')
                if nodeType[0] not in NodeType.__members__:
                    continue
                choices[nodeType[0]] = int(nodeType[1])
            else:
                continue
        results : list[str] = random.choices(list(choices.keys()), weights=list(choices.values()))
        return NodeType[results[0]]

    @staticmethod
    def parseWithoutOdds(nodeTypeWithOdds : str) -> NodeType:
        choices : list[NodeType] = []
        for nodeType in nodeTypeWithOdds.split(','):
            choices.append(NodeType[nodeType])
        results : list[NodeType] = random.choices(choices)
        return results[0]

    def __str__(self) -> str:
        forelinks : list[str] = list()
        for forwardNode in self.forelinks:
            forelinks.append((f"{forwardNode.id}:" if _globals.debug else "") + f"{forwardNode.name}")
            
        return (f"{self.id}:" if _globals.debug else "" ) + f"{self.name} {{" + ", ".join(forelinks) + "}"
    
    def executeNode(self):
        self.nodeType.execute()
        return