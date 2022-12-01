from dataclasses import dataclass
from gameObjects.specificMon import SpecificMon
from dataObjects.genericMon import GenericMon
@dataclass
class Side:
    mons: list[SpecificMon]
    activeMon: SpecificMon
    name: str = ''

    def __post_init__(self):
        if self.name == '':
            self.name = self.activeMon.nickname = 'Wild ' + self.activeMon.nickname

    def isDefeated(self) -> bool:
        for mon in self.mons:
            if mon.hasFainted() == False:
                return False

        return True
    
    def getActiveMonSpecies(self) -> GenericMon:
        return self.activeMon.genericMon