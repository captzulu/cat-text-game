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
        edgeSymbol = '°'
        horizontalWidth = 50
        string = "\n" + edgeSymbol + ('-' * horizontalWidth) + edgeSymbol + "\n   "
        
        string += self.name + ' || ' 
        string += (self.type1.acronym + (' / ' + self.type2.acronym if self.type2 != None else '')).upper()
        string += '\n   HP: ' + str(self.health)
        string += '\n   ATK: ' + str(self.attack)
        string += '\n   SPD: ' + str(self.speed)
        string += "\n" + edgeSymbol + ('-' * horizontalWidth) + edgeSymbol + "\n"
        return string

    def weakTo(self, incomingType:Type) -> float:
        damageMultiplierType1 = self.type1.checkTypeModifier(incomingType.acronym)
        damageMultiplierType2 = self.type2.checkTypeModifier(incomingType.acronym) if self.type2 != None else 1
        return damageMultiplierType1 * damageMultiplierType2

