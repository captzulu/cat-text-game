from dataclasses import dataclass
from gameObjects.sections.map.node import Node
@dataclass
class Map():
    nodes: dict[int, Node]