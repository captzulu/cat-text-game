from gameObjects.sections.map.node import Node
from dataObjects.enums.mapStates import MapStates
from dataObjects.enums.nodeType import NodeType
from dataFactory import dataFactory
from typing import Self
import itertools

class Map():
    nodes : dict[int, list[Node]]
    title : str
    activeNode : Node
    status : MapStates
    
    def __init__(self, title : str = "untitled"):
        self.nodeIdGenerator = itertools.count(1)
        self.title = title
        self.nodes = dict()
        self.status = MapStates.READY
        
    def start(self) -> None:
        self.status = MapStates.STARTED
        self.activeNode = self.nodes[0][0]
        self.activeNode.executeNode()
        
    def complete(self) -> None:
        self.status = MapStates.COMPLETED
        print()
        print(f"You have completed {self.title} !")
        print()
        
    def reset(self) -> None:
        self.start()
        print(f"{self.title} has been reset.")
    
    def getColumnAtIndex(self, columnIndex : int) -> list[Node]:
        if columnIndex < 0 or columnIndex not in self.nodes:
            return []
        return self.nodes[columnIndex]

    def advance(self, node : Node) -> None:
        if self.areLinked(self.activeNode, node):
            self.activeNode = node
            node.executeNode()
        else:
            print("Given node is not linked to the previous node")

        if len(self.activeNode.forelinks) == 0:
            self.complete()
    
    def areLinked(self, firstNode : Node, secondNode : Node) -> bool:
            if secondNode in firstNode.forelinks:
                return True
            else:
                return False
    
    def fail(self):
        self.status = MapStates.FAILED

    @classmethod
    def fromJson(cls, filePath : str) -> Self:
        mapJson : dict = dataFactory.objectFromJson(filePath)
        map : Map = cls(mapJson['title'])
        columnIndex : int = 0
        for nodeColumn in mapJson['nodes']:
            map.nodes[columnIndex] = []
            for node in nodeColumn:
                newNode = Node(next(map.nodeIdGenerator), NodeType[node['type']], columnIndex, forelinks=node['type'])
                map.nodes[columnIndex].append(newNode)
            map.linkLastColumn(columnIndex - 1)
            columnIndex += 1
        return map
    
    def linkLastColumn(self, columnIndex : int):
        lastColumn : list[Node] = self.nodes[columnIndex]
        for node in lastColumn:
            for link in foreLinks:
                link : int = link - 1
                nodeLinkedTo : Node = lastColumn[link if link in lastColumn else 0]
        return
            
    def __str__(self) -> str:
        toPrint : str = "Title : " + self.title + "\n"
        for key, column in self.nodes.items():
            toPrint += f"column {key} : " + ", ".join(map(str, column)) + "\n"
        return toPrint