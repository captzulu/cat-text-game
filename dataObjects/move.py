from dataclasses import dataclass
from dataObjects.type import Type 
@dataclass
class Attack:
    name: str
    power: int
    type1: Type