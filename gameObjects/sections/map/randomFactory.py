import random
from gameObjects.sections.map.node import Node
from gameObjects.sections.map.nodeEvents import NodeEvents
from gameObjects.sections.map.map import Map
from typing import Optional

class RandomFactory():
    def __init__(self):
        return
    
    def randomName(self) -> str:
        results : list[str] = random.choices(NodeEvents.NAME_LIST, weights=[1, 1, 8, 1, 5])
        return results[0]
    
    def randomBackLinks(self, previousIds : list[int]) -> list[int]:
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
    
    def autoGenerateNode(self, map : Map, columnIndex : int) -> int:
        previousColumn: list[Node] = map.getColumnAtIndex(columnIndex - 1)
        previousColumnIds: list[int] = map.getColumnIds(previousColumn)

        if columnIndex not in map.nodes:
            map.nodes[columnIndex] = list()
            
        backLinks: list[int] = self.randomBackLinks(previousColumnIds)
        newNode: Node = Node(next(map.nodeIdGenerator), self.randomName(), columnIndex, backLinks)
        for node in previousColumn:
            if node.id in newNode.backLinks:
                node.forwardLinks.append(newNode.id)
        map.nodes[columnIndex].append(newNode)
        return newNode.id
    
    def generateRandomMap(self, length: int, title: str = "") -> Map:
        newMap: Map = Map(title)
        i = 0 
        while i < length:
            self.generateRandomColumn(newMap, i, 1 if i == 0 else 4)
            i += 1
        if 0 in newMap.nodes and len(newMap.nodes[0]) >= 1:
            newMap.activeNode = newMap.nodes[0][0]
        return newMap
    
    def generateRandomColumn(self, map : Map, columnIndex: int, maxColumnLength: int) -> None:
        columnLength: int = random.randint(1, maxColumnLength)
        i = 0
        while i < columnLength:
            self.autoGenerateNode(map, columnIndex)
            i += 1