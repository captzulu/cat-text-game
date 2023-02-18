import random
from gameObjects.sections.map.node import Node
from gameObjects.sections.map.nodeEvents import NodeEvents
from gameObjects.sections.map.map import Map
from typing import Optional

class RandomFactory():
    def __init__(self):
        return
    
    @staticmethod
    def randomName() -> str:
        results : list[str] = random.choices(NodeEvents.NAME_LIST, weights=[1, 1, 8, 1, 5])
        return results[0]
    
    @staticmethod
    def randomBackLinks(previousColumn : list[Node]) -> list[Node]:
        previousColumnTmp = previousColumn.copy()
        if len(previousColumnTmp) == 0:
            return []

        amount : int = random.choices([1, 2, 3], weights=[2, 5, 3])[0]
        results : list[Node] = list()
        while amount > 0 and len(previousColumnTmp) > 0:
            pickedNode: Node = random.choice(previousColumnTmp)
            results.append(pickedNode)
            previousColumnTmp.remove(pickedNode)
            amount -= 1
        return results
    
    @staticmethod
    def autoGenerateNode(map : Map, columnIndex : int) -> None:
        previousColumn: list[Node] = map.getColumnAtIndex(columnIndex - 1)

        if columnIndex not in map.nodes:
            map.nodes[columnIndex] = list()
            
        backLinks: list[Node] = RandomFactory.randomBackLinks(previousColumn)
        newNode: Node = Node(next(map.nodeIdGenerator), RandomFactory.randomName(), columnIndex, backLinks)
        for node in previousColumn:
            if node in newNode.backLinks:
                node.forwardLinks.append(newNode)
        map.nodes[columnIndex].append(newNode)
        return
    
    @staticmethod
    def generateRandomMap(length: int, title: str = "") -> Map:
        newMap: Map = Map(title)
        i = 0 
        while i < length:
            RandomFactory.generateRandomColumn(newMap, i, 1 if i == 0 else 4)
            i += 1
        if 0 in newMap.nodes and len(newMap.nodes[0]) >= 1:
            newMap.activeNode = newMap.nodes[0][0]
        return newMap
    
    @staticmethod
    def generateRandomColumn(map : Map, columnIndex: int, maxColumnLength: int) -> None:
        columnLength: int = random.randint(1, maxColumnLength)
        i = 0
        while i < columnLength:
            RandomFactory.autoGenerateNode(map, columnIndex)
            i += 1