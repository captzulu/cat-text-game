from dataclasses import dataclass, field
from dataObjects.type import Type 
import _globals
@dataclass
class Move:
    name: str
    power: int
    typeText: str = ''
    type: Type = field(init=False, repr=False)
    
    def __post_init__(self):
        self.type = _globals.types[self.typeText]