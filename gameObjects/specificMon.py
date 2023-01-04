from dataclasses import dataclass, field
from dataObjects.genericMon import GenericMon
from dataObjects.type import Type
@dataclass
class SpecificMon:
    currentHealth: int = field(init=False)
    maxHealth: int = field(init=False)
    attack: int = field(init=False)
    speed: int = field(init=False)
    genericMon: GenericMon = field(repr=False)
    level:int
    nickname: str = ''
    status: str = 'normal'

    def __post_init__(self):
        if self.nickname == '':
            self.nickname = self.genericMon.name
        self.maxHealth = int(self.genericMon.health/5 * self.level)
        self.currentHealth = int(self.genericMon.health/5 * self.level)
        baseAttack = self.genericMon.attack/13
        self.attack = int(baseAttack if baseAttack >= 0 else 1) * self.level
        baseSpeed = self.genericMon.speed/13
        self.speed = int(baseSpeed if baseSpeed >= 0 else 1) * self.level

    def loseHealth(self, hitPointLoss : int):
        self.currentHealth -= hitPointLoss
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
        self.healStatus()
        self.currentHealth = self.maxHealth

    def weakTo(self, incomingType:Type) -> float:
        return self.genericMon.weakTo(incomingType)
    
    def getHealthPercent(self):
        return self.maxHealth / self.currentHealth 