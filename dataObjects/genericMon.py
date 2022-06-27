from dataclasses import dataclass, field
from dataObjects.type import Type
from typing import Optional
import _globals  

@dataclass
class GenericMon:
    name: str
    speed: int
    attack: int
    health: int
    type1: Type = field(init=False, repr=False)
    type2: Optional[Type] = field(init=False, repr=False)
    typeText: str = ''

    def __post_init__(self):
        types = self.typeText.split(',')
        self.type1 = _globals.types[types[0]]
        self.type2 = _globals.types[types[1]] if len(types) == 2 else None

    def __str__(self):
        return (self.name + ' || ' + self.printTypeAcronyms() + 
            ' || HP: ' + str(self.health) + ' | ATK: ' + str(self.attack) + ' | SPD: ' + str(self.speed))
    
    def printTypeAcronyms(self) -> str:
        return (self.type1.acronym + (' / ' + self.type2.acronym if self.type2 != None else '')).upper()

    def weakTo(self, incomingType:Type) -> float:
        damageMultiplierType1 = self.type1.checkTypeModifier(incomingType.acronym)
        damageMultiplierType2 = self.type2.checkTypeModifier(incomingType.acronym) if self.type2 != None else 1
        return damageMultiplierType1 * damageMultiplierType2

