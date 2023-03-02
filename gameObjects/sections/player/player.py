from dataclasses import dataclass, field
from gameObjects.sections.battle.side import Side
from gameObjects.specificMon import SpecificMon
from dataObjects.genericMon import GenericMon
import _globals
from cliObjects.menuFunctions import menuFunctions
@dataclass
class Player:
    name: str
    party: Side = field(init=False)
    gold: int = 0
    items: list = field(default_factory=list)
    
    def __post_init__(self):
        self.chooseFirstMon(5)
    
    def addItem(self, item : str):
        print(f"You have aquired {item}")
        self.items.append(item)
        
    def addMon(self, specificMon : SpecificMon):
            self.party.addMon(specificMon)
            
    def chooseFirstMon(self, level : int):
        specificMon : SpecificMon = self.pickSpecificMon(level)
        self.party = Side([specificMon])
    
    def pickGenericMon(self) -> GenericMon:
        mons : dict[int, str] = dict()
        for no, mon in _globals.genericMons.items():
            mons[int(no)] = str(mon)
    
        return _globals.genericMons[str(menuFunctions.menuInt(mons))]
    
    def pickSpecificMon(self, level : int) -> SpecificMon:
        return SpecificMon(self.pickGenericMon(), level)
    
    def status(self):
        print(self)
        
    def __str__(self) -> str:
        partyHp = [(mon.nickname, f"{mon.currentHealth}/{mon.maxHealth}") for mon in self.party.mons]
        return self.name + " " + str(partyHp)