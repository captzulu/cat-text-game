from dataclasses import dataclass  
@dataclass
class Type:
    name: str
    weaknesses: str
    resistances: str
    immunities: str
    acronym: str

    def checkTypeModifier(self, incomingType:str) -> float:
        damageMultiplier = 1.0
        if incomingType in self.weaknesses.split(','):
            damageMultiplier *= 2
        if incomingType in self.resistances.split(','):
            damageMultiplier /= 2
        if incomingType in self.immunities.split(','):
            damageMultiplier = 0.0
        
        return damageMultiplier
    
    def __str__(self):
        return (self.name.capitalize())
    
