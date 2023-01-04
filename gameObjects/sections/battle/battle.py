from dataclasses import dataclass, field
from gameObjects.sections.battle.battleLog import BattleLog
from gameObjects.specificMon import SpecificMon
from gameObjects.sections.battle.side import Side
from dataObjects.type import Type
import random
@dataclass
class Battle:
    side1: Side
    side2: Side
    turn: int = 0
    log: BattleLog = field(init=False)
    completed: bool = False
    edgeSymbol: str = '°'
    Filler: str = '='
    DAMAGE_VARIATION_MIN : float = 0.85
    DAMAGE_VARIATION_MAX : float = 1.15
    
    def executeBattle(self):
        self.__executeIntro()
        input("Hit a key to start the fight...")
        self.__battleLoop()

    def __executeIntro(self):
        title = f"Battle ! {self.side1.name} Vs {self.side2.name}"
        titleLine = self.edgeSymbol + self.fillTitleLine(title) + self.edgeSymbol
        self.write(titleLine)
        self.write(str(self.side1.activeMon))
        
        longestMonNameLength = self.calculateLongestMonNameLength()
        paddingLength = longestMonNameLength // 2
        self.write(' ' * paddingLength + 'VS' + (' ' * paddingLength))
        self.write(str(self.side2.activeMon))
        self.write(self.edgeSymbol + (self.Filler * longestMonNameLength) + self.edgeSymbol)
        print(self.__getTurnLog())

    def fillTitleLine(self, title:str) -> str:
        longestMonNameLength = self.calculateLongestMonNameLength()
        titleLineHalf : str = self.Filler * ((longestMonNameLength - len(title)) // 2)
        return titleLineHalf + title + titleLineHalf

    def write(self, text : str):
        if hasattr(self, 'log') == False:
            self.log = BattleLog()
        self.log.addExplicitLine(self.turn, text)
        self.log.addImplicitLine(self.turn, text)
    
    def calculateLongestMonNameLength(self) -> int:
        mon1Length = len(str(self.side1.activeMon))
        mon2Length = len(str(self.side2.activeMon))
        return mon1Length if mon1Length > mon2Length else mon2Length

    def __executeTurn(self):
        self.turn += 1
        self.write(f"=== New turn ({self.turn}) ===")
        self.__attackPhase()
        if self.turn >= 100:
            winner = self.side1.activeMon if self.side1.activeMon.currentHealth > self.side2.activeMon.currentHealth else self.side2.activeMon
            self.__completeBattle(f'{winner.nickname} has stalled out the win !')
            
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
        if self.__hasCompleted() == False:
            self.__sideTurn(secondSide, firstSide)

    def __sideTurn(self, side : Side, oppositeSide : Side):
        oppositeMon = oppositeSide.activeMon
        self.attack(side.activeMon, oppositeMon, side.activeMon.genericMon.type1)
        if oppositeSide.isDefeated():
            self.__completeBattle(f'{oppositeMon.nickname} has fainted !')
        else:
            self.write(f'{oppositeMon.nickname} has {oppositeMon.currentHealth}/{oppositeMon.maxHealth} health !')

    def __battleLoop(self) -> None:
        while self.__hasCompleted() == False:
            self.__executeTurn()
            print(self.__getTurnLog())
            if self.__hasCompleted() == False:
                input("Hit a key to continue...")
        return

    def __hasCompleted(self):
        return self.completed
            
    def __completeBattle(self, message:str):
        self.write(message)
        self.completed = True
        return
    
    def attack(self, attacker:SpecificMon, defender:SpecificMon, attackType:Type):
        damage = int(self.__damageVariation(attacker.attack * defender.weakTo(attackType)))
        defender.loseHealth(damage)
        self.write(f"{attacker.nickname} dealt {damage} to {defender.nickname}")
        return
    
    def __damageVariation(self, damage : float):
        return damage * random.uniform(self.DAMAGE_VARIATION_MIN, self.DAMAGE_VARIATION_MAX)
        
    def writeImplicit(self, text : str):
        self.log.addImplicitLine(self.turn, text)
        
    def __getTurnLog(self):
        return self.log.getFormattedLine(self.turn)
    
