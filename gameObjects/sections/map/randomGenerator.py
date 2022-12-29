from gameObjects.sections.map.node import Node

class RandomGenerator():
    
    def __init__(self) -> None:
        pass
    
    def generateRandomNode(self, previousColumnIds: list[int], id : int, columnIndex : int) -> Node:
        name = Node.randomName()
        backLinks = Node.randomBackLinks(previousColumnIds)
       
        return Node(id, name, columnIndex, backLinks)