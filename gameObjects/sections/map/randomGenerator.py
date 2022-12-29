from gameObjects.sections.map.node import Node
from gameObjects.sections.map.map import Map

class RandomGenerator():
    
    def __init__(self) -> None:
        pass
    
    def generateRandomNode(self, previousColumnIds: list[int], id : int, columnIndex : int) -> Node:
        name = Node.randomName()
        backLinks = Node.randomBackLinks(previousColumnIds)
       
        return Node(id, name, columnIndex, backLinks)
    
    def generateRandomMap(self, length: int) -> Map:
        newMap = Map()
        i = 0 
        while i < length:
            newMap.autoGenerateNode(i)
            i += 1
        return newMap