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
        self.party = Side([], self.name)
    
    def addItem(self, item : str):
        print(f"You have acquired {item}")
        self.items.append(item)
        
    def addGold(self, amount : int):
        print(f"You have acquired {amount}g")
        self.gold += amount
    
    def takeGold(self, amount : int):
        if self.gold >= amount:
            self.gold -= amount
        else:
            self.gold = 0
        
    def addMon(self, specificMon : SpecificMon):
        self.party.addMon(specificMon)
            
    def chooseMon(self, level : int):
        print("Pick a mon to start with :")
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
        partyHp = [(mon.nickname, f"lvl {mon.level}",f"{mon.currentHealth}/{mon.maxHealth}") for mon in self.party.mons]
        return self.name + " " + str(partyHp)