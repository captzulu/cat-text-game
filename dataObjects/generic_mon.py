from dataclasses import dataclass, field
from dataObjects.type import Type
import _globals  

@dataclass
class Generic_mon:
    name: str
    speed: int
    attack: int
    health: int
    type1: Type = field(init=False, repr=False)
    type2: Type = field(init=False, repr=False)
    typeText: str = ''

    def __post_init__(self):
        types = self.typeText.split(',')
        self.type1 = _globals.types[types[0]]
        self.type2 = _globals.types[types[1]] if len(types) == 2 else None

    def __str__(self):
        edgeSymbol = '°'
        horizontalWidth = 50
        print("\n" + edgeSymbol + ('-' * horizontalWidth) + edgeSymbol + "\n")
        print(self.name + ' || ' + self.type1.acronym + ' / ' + self.type2.acronym)
        print('HP: ' + self.health)
        print('ATK: ' + self.attack)
        print('SPD: ' + self.speed)
        print("\n" + edgeSymbol + ('-' * horizontalWidth) + edgeSymbol + "\n")

    def weakTo(self, incomingType:Type):
        damageMultiplierType1 = self.type1.checkTypeModifier(incomingType.acronym)
        damageMultiplierType2 = self.type2.checkTypeModifier(incomingType.acronym) if self.type2 != None else 1
        return damageMultiplierType1 * damageMultiplierType2

