import random
from gameObjects.sections.map.node import Node
from gameObjects.sections.map.map import Map
from dataObjects.enums.nodeType import NodeType

class RandomFactory():
    def __init__(self):
        return
    
    @staticmethod
    def randomType() -> NodeType:
        nodeTypeList = list(NodeType)
        nodeTypeList.remove(NodeType.START)
        results : list[NodeType] = random.choices(nodeTypeList, weights=[1, 1, 8, 1, 5])
        return results[0]
    
    @staticmethod
    def generateRandomMap(length: int, title: str = "") -> Map:
        newMap: Map = Map(title)
        RandomFactory.generateAllNodes(newMap, length)    
        RandomFactory.linkAllNodes(newMap)

        if 0 in newMap.nodes and len(newMap.nodes[0]) >= 1:
            newMap.activeNode = newMap.nodes[0][0]
        return newMap
    
    @staticmethod
    def generateAllNodes(map : Map, length : int) -> None:
        i = 0
        while i < length:
            RandomFactory.generateRandomColumn(map, i, 1 if i == 0 else 4)
            i += 1
        return
    
    @staticmethod
    def generateRandomColumn(map : Map, columnIndex: int, maxColumnLength: int) -> None:
        columnLength: int = random.randint(1, maxColumnLength)
        i = 0
        while i < columnLength:
            RandomFactory.autoGenerateNode(map, columnIndex)
            i += 1
            
    @staticmethod
    def autoGenerateNode(map : Map, columnIndex : int) -> None:
        if columnIndex not in map.nodes:
            map.nodes[columnIndex] = list()

        nodeType = NodeType.START if columnIndex == 0 else RandomFactory.randomType()
        map.nodes[columnIndex].append(Node(next(map.nodeIdGenerator), nodeType, columnIndex))
        return

    @staticmethod
    def linkAllNodes(map : Map) -> None:
        for i, column in map.nodes.items():
            for node in column:
                nextColumn = map.nodes[i + 1] if (i + 1) in map.nodes else []
                RandomFactory.generateForwardLinks(node, nextColumn)
        return
    
    @staticmethod
    def generateForwardLinks(node : Node, nextColumn : list[Node]) -> None:
        nextColumnTmp = nextColumn.copy()

        amount : int = random.choices([1, 2], weights=[5, 3])[0]
        while amount > 0 and len(nextColumnTmp) > 0:
            pickedNode = random.choice(nextColumnTmp)
            node.forwardLinks.append(pickedNode)
            nextColumnTmp.remove(pickedNode)
            amount -= 1
        return