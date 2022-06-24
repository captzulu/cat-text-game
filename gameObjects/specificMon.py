from dataclasses import dataclass, field
from dataObjects.generic_mon import Generic_mon
from dataObjects.type import Type
import _globals  
@dataclass
class SpecificMon:
    currentHealth: int = field(init=False)
    maxHealth: int = field(init=False)
    attack: int = field(init=False)
    speed: int = field(init=False)
    genericMon: Generic_mon = field(repr=False)
    level:int
    nickname: str = None
    status: str = 'normal'

    def __post_init__(self):
        if self.nickname == None:
            self.nickname = self.genericMon.name
        self.maxHealth = int(self.genericMon.health/25 * self.level)
        self.currentHealth = int(self.genericMon.health/25 * self.level)
        self.attack = int(self.genericMon.attack/62.5 * self.level)
        self.speed = int(self.genericMon.speed/62.5 * self.level)

    def loseHealth(self, hitpointLoss:int):
        self.currentHealth -= hitpointLoss
        if self.currentHealth <= 0 :
            self.faint()

    def faint(self):
        self.changeStatus('fainted')
        self.currentHealth = 0

    def hasFainted(self):
        return self.status == 'fainted'

    def changeStatus(self, status:str):
        self.status = status
    
    def healStatus(self):
        self.changeStatus('normal')
    
    def fullHeal(self):
        self.healStatus('normal')
        self.currentHealth = self.maxHealth

    def weakTo(self, incomingType:Type):
        return int(self.genericMon.weakTo(incomingType))

    
