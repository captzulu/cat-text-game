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
    
    def executeBattle(self):
        self.__executeIntro()
        input("Hit a key to start the fight...")
        self.__battleLoop()

    def __executeIntro(self):
        title = f"Battle ! {self.side1.name} Vs {self.side2.name}"
        titleLine = self.edgeSymbol + self.fillTitleLine(title) + self.edgeSymbol
        self.__write(titleLine)
        self.__write(str(self.side1.getActiveMonSpecies()))
        
        longestMonNameLength = self.__calculateLongestMonNameLength()
        paddingLength = longestMonNameLength // 2
        self.__write(' ' * paddingLength + 'VS' + (' ' * paddingLength))
        self.__write(str(self.side2.getActiveMonSpecies()))
        self.__write(self.edgeSymbol + (self.Filler * longestMonNameLength) + self.edgeSymbol)
        print(self.__getTurnLog())

    def fillTitleLine(self, title:str) -> str:
        longestMonNameLength = self.__calculateLongestMonNameLength()
        titleLineHalf : str = self.Filler * ((longestMonNameLength - len(title)) // 2)
        return titleLineHalf + title + titleLineHalf

    def __write(self, text : str):
        if hasattr(self, 'log') == False:
            self.log = BattleLog()
        self.log.addExplicitLine(self.turn, text)
        self.log.addImplicitLine(self.turn, text)
    
    def __calculateLongestMonNameLength(self) -> int:
        mon1Length = len(str(self.side1.getActiveMonSpecies()))
        mon2Length = len(str(self.side2.getActiveMonSpecies()))
        return mon1Length if mon1Length > mon2Length else mon2Length

    def __executeTurn(self):
        self.turn += 1
        self.__write(f"=== New turn ({self.turn}) ===")
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
        self.__attack(side.activeMon, oppositeMon, side.activeMon.genericMon.type1)
        if oppositeSide.isDefeated():
            self.__completeBattle(f'{oppositeMon.nickname} has fainted !')
        else:
            self.__write(f'{oppositeMon.nickname} has {oppositeMon.currentHealth}/{oppositeMon.maxHealth} health !')

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
        self.__write(message)
        self.completed = True
        return
    
    def __attack(self, attacker:SpecificMon, defender:SpecificMon, attackType:Type):
        damage = int(attacker.attack * defender.weakTo(attackType))
        defender.loseHealth(damage)
        self.__write(f"{attacker.nickname} dealt {damage} to {defender.nickname}")
        return
        
    def __writeImplicit(self, text : str):
        self.log.addImplicitLine(self.turn, text)
        
    def __getTurnLog(self):
        return self.log.getFormattedLine(self.turn)
    
