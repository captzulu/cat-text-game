from dataclasses import dataclass, field
from dataObjects.genericMon import GenericMon
from dataObjects.type import Type
import math
@dataclass
class SpecificMon:
    currentHealth: int = field(init=False)
    maxHealth: int = field(init=False)
    attack: int = field(init=False)
    speed: int = field(init=False)
    genericMon: GenericMon = field(repr=False)
    level: int
    nickname: str = ''
    status: str = 'normal'

    def __post_init__(self):
        if self.nickname == '':
            self.nickname = self.genericMon.name
        self.calculateStats()
        self.currentHealth = self.maxHealth
        
    def calculateStats(self):
        initialStatModifier = 2
        statsPerLevelModifier = 10
        healthPerLevel = self.genericMon.health / statsPerLevelModifier
        self.maxHealth = math.ceil(healthPerLevel * (self.level + initialStatModifier))
        baseAttack = self.genericMon.attack / statsPerLevelModifier
        self.attack = int(baseAttack * (self.level + initialStatModifier))
        baseSpeed = self.genericMon.speed / statsPerLevelModifier
        self.speed = int(baseSpeed * (self.level + initialStatModifier))

    def loseHealth(self, hitPointLoss : int):
        self.currentHealth -= hitPointLoss
        if self.currentHealth <= 0 :
            self.faint()

    def faint(self):
        self.changeStatus('fainted')
        self.currentHealth = 0

    def hasFainted(self):
        return self.status == 'fainted'

    def changeStatus(self, status : str):
        self.status = status
    
    def healStatus(self):
        self.changeStatus('normal')
    
    def fullHeal(self):
        self.healStatus()
        self.currentHealth = self.maxHealth

    def weakTo(self, incomingType : Type) -> float:
        return self.genericMon.weakTo(incomingType)
    
    def getHealthPercent(self):
        return self.maxHealth / self.currentHealth
    
    def levelUp(self):
        self.level += 1
        beforeLevelUpMaxHp = self.maxHealth
        self.calculateStats()
        maxHpGain = self.maxHealth - beforeLevelUpMaxHp
        self.currentHealth += maxHpGain
    
    def heal(self, amount):
        self.currentHealth = self.maxHealth if amount + self.currentHealth > self.maxHealth else self.currentHealth + amount
    
    def __str__(self):
        return (
            self.nickname + " | lvl:" + str(self.level) + " | " + self.genericMon.printTypeAcronyms() + " | HP:" + str(self.maxHealth) +
            ' ¦ ATK: ' + str(self.attack) + ' ¦ SPD:' + str(self.speed)
            )