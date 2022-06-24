from dataclasses import dataclass
import _globals  
@dataclass
class Type:
    name: str
    weaknesses: str
    resistances: str
    immunities: str
    acronym: str

    def checkTypeModifier(self, incomingType:str):
        damageMultiplier = 1
        if incomingType in self.weaknesses.split(','):
            damageMultiplier *= 2
        if incomingType in self.resistances.split(','):
            damageMultiplier /= 2
        if incomingType in self.immunities.split(','):
            damageMultiplier = 0
        
        return damageMultiplier
    
