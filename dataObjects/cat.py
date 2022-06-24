from dataclasses import dataclass, field
from dataObjects.type import Type
from globals import _GLOBALS

@dataclass
class Cat:
    name: str
    speed: int
    attack: int
    health: int
    type1: Type = field(init=False, repr=False)
    type2: Type = field(init=False, repr=False)
    type1_text: Type = str
    type2_text: Type = str

    def __post_init__(self):
        self.type1 = _GLOBALS['types'][self.type1_text]
        self.type2 = _GLOBALS['types'][self.type2_text]