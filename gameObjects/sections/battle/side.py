from dataclasses import dataclass
from gameObjects.specificMon import SpecificMon
from dataObjects.genericMon import GenericMon
@dataclass
class Side:
    mons: list[SpecificMon]
    activeMon: SpecificMon
    isAi: bool
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
    
    def addMon(self, specificMon : SpecificMon) -> None:
        self.mons.append(specificMon)
        if len(self.mons) == 1:
            self.activeMon = specificMon
            
    def healParty(self, percentageToHeal : int):
        for mon in self.mons:
            mon.heal(int(mon.maxHealth * (percentageToHeal / 100)))