from dataclasses import dataclass, field
from gameObjects.specificMon import SpecificMon
from gameObjects.side import Side
from dataObjects.type import Type
import random
@dataclass
class Battle:
    turn: int = field(init=False, default=0)
    side1: Side
    side2: Side 
    completed: bool = field(init=False, default=False)

    def hasCompleted(self):
        return self.completed

    def completeBattle(self, message:str):
        print(message)
        self.completed = True
        return
    
    def attack(self, attacker:SpecificMon, defender:SpecificMon, attackType:Type):
        damage = int(attacker.attack * defender.weakTo(attackType))
        defender.loseHealth(damage)
        print(f"{attacker.nickname} dealt {damage} to {defender.nickname}")
        return

    def executeIntro(self):
        print(f"=== Battle ! {self.side1.name} Vs {self.side2.name} ===")
        print(f"{self.side1.activeMon.genericMon}")
        print(f"{self.side2.activeMon.genericMon}")
        self.turn += 1
        self.attackPhase()

    def executeTurn(self):
        print(f"=== New turn ({self.turn}) ===")

        self.attackPhase()
        self.turn += 1
        if self.turn >= 100:
            winner = self.side1.activeMon if self.side1.activeMon.currentHealth > self.side2.activeMon.currentHealth else self.side2.activeMon
            self.completeBattle(f'{winner.nickname} has stalled out the win !')

    def attackPhase(self):
        side1Speed = self.side1.activeMon.speed
        side2Speed = self.side2.activeMon.speed
        firstSide = self.side1 if side1Speed > side2Speed else self.side2
        secondSide = self.side2 if side2Speed > side1Speed else self.side1
        if side1Speed == side2Speed:
            firstSide = self.side1 if random.randint(0,1) == 1 else self.side2
            secondSide = self.side2 if firstSide == self.side1 else self.side1

        self.sideTurn(firstSide, secondSide)
        if self.hasCompleted() == False:
            self.sideTurn(secondSide, firstSide)

    def sideTurn(self, side : Side, oppositeSide : Side):
        oppositeMon = oppositeSide.activeMon
        self.attack(side.activeMon, oppositeMon, side.activeMon.genericMon.type1)
        if oppositeSide.isDefeated():
            self.completeBattle(f'{oppositeMon.nickname} has fainted !')
        else:
            print(f'{oppositeMon.nickname} has {oppositeMon.currentHealth}/{oppositeMon.maxHealth} health !')
    
