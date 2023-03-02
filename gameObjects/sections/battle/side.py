from dataclasses import dataclass, field
from gameObjects.specificMon import SpecificMon
from dataObjects.genericMon import GenericMon
@dataclass
class Side:
    mons: list[SpecificMon] = field(default_factory=list)
    name: str = ''
    isAi: bool = False
    activeMon: SpecificMon = field(init=False)

    def __post_init__(self):
        if len(self.mons) != 0:
            self.activeMon = self.mons[0]
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