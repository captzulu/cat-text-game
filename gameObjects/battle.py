from dataclasses import dataclass, field
from gameObjects.battleLog import BattleLog
from gameObjects.specificMon import SpecificMon
from gameObjects.side import Side
from dataObjects.type import Type
import random
@dataclass
class Battle:
    side1: Side
    side2: Side
    turn: int = 0
    log: BattleLog = field(init=False)
    completed: bool = False

    def write(self, text : str):
        self.log.addExplicitLine(self.turn, text)
        self.log.addImplicitLine(self.turn, text)

    def executeIntro(self):
        self.log = BattleLog()
        
        self.write(f"=== Battle ! {self.side1.name} Vs {self.side2.name} ===")
        self.write(f"{self.side1.activeMon.genericMon}")
        self.write(f"{self.side2.activeMon.genericMon}")
        self.executeTurn()

    def executeTurn(self):
        self.turn += 1
        self.write(f"=== New turn ({self.turn}) ===")
        self.__attackPhase()
        self.write("\n")
        if self.turn >= 100:
            winner = self.side1.activeMon if self.side1.activeMon.currentHealth > self.side2.activeMon.currentHealth else self.side2.activeMon
            self.completeBattle(f'{winner.nickname} has stalled out the win !')
            
    def __attackPhase(self):
        side1Speed = self.side1.activeMon.speed
        side2Speed = self.side2.activeMon.speed

        if side1Speed == side2Speed:
            firstSide = self.side1 if random.randint(0,1) == 1 else self.side2
            secondSide = self.side2 if firstSide == self.side1 else self.side1
        else:
            firstSide = self.side1 if side1Speed > side2Speed else self.side2
            secondSide = self.side2 if side1Speed > side2Speed else self.side1
        self.__sideTurn(firstSide, secondSide)
        if self.hasCompleted() == False:
            self.__sideTurn(secondSide, firstSide)

    def __sideTurn(self, side : Side, oppositeSide : Side):
        oppositeMon = oppositeSide.activeMon
        self.__attack(side.activeMon, oppositeMon, side.activeMon.genericMon.type1)
        if oppositeSide.isDefeated():
            self.completeBattle(f'{oppositeMon.nickname} has fainted !')
        else:
            self.write(f'{oppositeMon.nickname} has {oppositeMon.currentHealth}/{oppositeMon.maxHealth} health !')

    def hasCompleted(self):
        return self.completed
            
    def completeBattle(self, message:str):
        self.write(message)
        self.completed = True
        return
    
    def __attack(self, attacker:SpecificMon, defender:SpecificMon, attackType:Type):
        damage = int(attacker.attack * defender.weakTo(attackType))
        defender.loseHealth(damage)
        self.write(f"{attacker.nickname} dealt {damage} to {defender.nickname}")
        return
        
    def writeImplicit(self, text : str):
        self.log.addImplicitLine(self.turn, text)
        
    def getTurnLog(self):
        return self.log.getFormattedLine(self.turn)
    
