from dataclasses import dataclass, field
from dataObjects.type import Type
from dataObjects.move import Move
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
    moves: dict[int, Move] = field(init=False)
    movesText: str = ''

    def __post_init__(self):
        types : list[str] = self.typeText.split(',')
        self.type1 = _globals.types[types[0]]
        self.type2 = None if len(types) == 1 else _globals.types[types[1]]
        
        self.moves : dict[int, Move] = dict()
        if self.movesText != "":
            moveIdList : list[str] = self.movesText.split(',')
            for i, id in enumerate(moveIdList):
                self.moves[i] = _globals.moves[id]

    def __str__(self):
        return (self.name + ' || ' + self.printTypeAcronyms() + 
            ' || HP: ' + str(self.health) + ' | ATK: ' + str(self.attack) + ' | SPD: ' + str(self.speed))
    
    def printTypeAcronyms(self) -> str:
        return (self.type1.acronym + ('/' + self.type2.acronym if self.type2 != None else '')).upper()

    def weakTo(self, incomingType:Type) -> float:
        damageMultiplierType1 = self.type1.checkTypeModifier(incomingType.acronym)
        damageMultiplierType2 = self.type2.checkTypeModifier(incomingType.acronym) if self.type2 != None else 1
        return damageMultiplierType1 * damageMultiplierType2