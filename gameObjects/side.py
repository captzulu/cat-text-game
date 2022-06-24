from dataclasses import dataclass, field
from gameObjects.specificMon import SpecificMon
@dataclass
class Side:
    mons: list[SpecificMon]
    activeMon: SpecificMon
    name: str = None

    def __post_init__(self):
        if self.name == None:
            self.name = self.activeMon.nickname = 'Wild ' + self.activeMon.nickname

    def isDefeated(self):
        for mon in self.mons:
            if mon.hasFainted() == False:
                return False

        return True
