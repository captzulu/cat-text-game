from dataclasses import dataclass, field
from dataObjects.genericMon import GenericMon
from dataObjects.move import Move
from dataObjects.type import Type
import math
@dataclass
class SpecificMon:
    currentHealth: int = field(init=False)
    maxHealth: int = field(init=False)
    attack: int = field(init=False)
    speed: int = field(init=False)
    moves: list[Move] = field(init=False)
    genericMon: GenericMon = field(repr=False)
    level: int
    nickname: str = ''
    status: str = 'normal'
    flinchCounter : int = 0

    def __post_init__(self):
        if self.nickname == '':
            self.nickname = self.genericMon.name
        self.calculateStats()
        self.currentHealth = self.maxHealth
        self.assignDefaultMoves()
        
    def calculateStats(self):
        initialStatModifier = 2
        healthPerLevel = self.genericMon.health / 5
        self.maxHealth = math.ceil(healthPerLevel * (self.level + initialStatModifier))
        baseAttack = self.genericMon.attack / 10
        self.attack = int(baseAttack * (self.level + initialStatModifier))
        baseSpeed = self.genericMon.speed / 10
        self.speed = int(baseSpeed * (self.level + initialStatModifier))

    def loseHealth(self, hitPointLoss : int):
        self.currentHealth -= hitPointLoss
        if self.currentHealth <= 0 :
            self.faint()
    
    def assignDefaultMoves(self):
        self.moves : list[Move] = list()
        for (level, move) in reversed(self.genericMon.moveList):
            if level <= self.level and len(self.moves) < 4:
                self.moves.append(move)
            
    def loseMaxHealthPercent(self, hitPointLossPercent : float, minDmg : bool = True) -> int:
        hpLost = math.floor(self.maxHealth * (hitPointLossPercent / 100))
        hpLost = 1 if hpLost == 0 and minDmg == True else hpLost
        self.loseHealth(hpLost)
        return hpLost

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
    
    def healMaxHealthPercent(self, hitPointHealPercent : float) -> int:
        hpGained = math.floor(self.maxHealth * (hitPointHealPercent / 100))
        self.heal(hpGained)
        return hpGained
    
    def getStatusAcronym(self) -> str: 
        if self.status == 'poison':
            return 'psn'
        
        if self.status == 'burn':
            return 'brn'
        
        return ''
    
    def flinch(self) -> str:
        self.flinchCounter -= 1
        return f"{self} has flinched !" + (f"It will continue flinching for {self.flinchCounter} turns"
                if self.flinchCounter > 0 else '')

    def __str__(self):
        return (
            self.nickname + " | lvl:" + str(self.level) + " | " + self.genericMon.printTypeAcronyms() + " | HP:" + str(self.maxHealth) +
            ' ¦ ATK: ' + str(self.attack) + ' ¦ SPD:' + str(self.speed)
            )