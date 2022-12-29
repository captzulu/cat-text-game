from gameObjects.sections.map.node import Node

class RandomGenerator():
    
    def __init__(self) -> None:
        pass
    
    #should be moves in Node as a classMethod like generateRandomMap in Map
    def generateRandomNode(self, previousColumnIds: list[int], id : int, columnIndex : int) -> Node:
        name = Node.randomName()
        backLinks = Node.randomBackLinks(previousColumnIds)
       
        return Node(id, name, columnIndex, backLinks)