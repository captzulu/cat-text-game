from dataclasses import dataclass, field
from gameObjects.sections.battle.battleLog import BattleLog
from gameObjects.specificMon import SpecificMon
from dataObjects.genericMon import GenericMon
from gameObjects.sections.battle.side import Side
from dataObjects.type import Type
from dataObjects.move import Move
import random
from cliObjects.menuFunctions import menuFunctions
import time

@dataclass
class Battle:
    side1: Side
    side2: Side
    turn: int = 1
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

    def fillTitleLine(self, title:str) -> str:
        longestMonNameLength = self.calculateLongestMonNameLength()
        titleLineHalf : str = self.Filler * ((longestMonNameLength - len(title)) // 2)
        return titleLineHalf + title + titleLineHalf

    def write(self, text : str):
        if hasattr(self, 'log') == False:
            self.log = BattleLog()
        self.log.addExplicitLine(self.turn, text)
        self.log.addImplicitLine(self.turn, text)
        print(text)
        time.sleep(0.10)
    
    def calculateLongestMonNameLength(self) -> int:
        mon1Length = len(str(self.side1.activeMon))
        mon2Length = len(str(self.side2.activeMon))
        return mon1Length if mon1Length > mon2Length else mon2Length

    def __executeTurn(self):
        self.write(f"\n==== New turn ({self.turn}) ====")
        self.__attackPhase()
        if self.turn >= 100:
            winner = self.side1.activeMon if self.side1.activeMon.currentHealth > self.side2.activeMon.currentHealth else self.side2.activeMon
            self.__completeBattle(f'{winner.nickname} has stalled out the win !')
        self.turn += 1
    
    def __attackPhase(self):
        firstSide : Side = self.getFastestSide()
        secondSide : Side = self.side2 if firstSide == self.side1 else self.side1
        firstSideMove : Move = self.__takeTurn(firstSide)
        secondSideMove : Move = self.__takeTurn(secondSide)
        self.__sideTurn(firstSide, secondSide, firstSideMove)
        if self.__hasCompleted() == False:
            print("")
            self.__sideTurn(secondSide, firstSide, secondSideMove)
        
    def getFastestSide(self) -> Side:
        side1Speed = self.side1.activeMon.speed
        side2Speed = self.side2.activeMon.speed

        if side1Speed == side2Speed:
            firstSide = self.side1 if random.randint(0,1) == 1 else self.side2
        else:
            firstSide = self.side1 if side1Speed > side2Speed else self.side2
        return firstSide
 
    def __takeTurn(self, side : Side) -> Move:
        pickedMoveFirst : Move = self.__pickMoveAi(side.getActiveMonSpecies()) if side.isAi else self.__pickMove(side.getActiveMonSpecies())
        return pickedMoveFirst 

    def __pickMove(self, pokemonSpecies : GenericMon) -> Move:
        print("Pick a move to use :")
        moves : dict[int, tuple[str, Move]] = dict()
        for i, move in pokemonSpecies.moves.items():
            moves[i] = (move.name, move) 
        pickedMove : Move = menuFunctions.menuObject(moves)
        return pickedMove
    
    def __pickMoveAi(self, pokemonSpecies : GenericMon) -> Move:
        maxMoveIndex : int = len(pokemonSpecies.moves) - 1
        pickedMoveIndex = 0 if maxMoveIndex == 0 else random.choice(range(0, maxMoveIndex))
        pickedMove : Move = pokemonSpecies.moves[pickedMoveIndex]
        return pickedMove

    def __sideTurn(self, side : Side, oppositeSide : Side, pickedMove: Move):
        oppositeMon = oppositeSide.activeMon
        self.attack(side.activeMon, oppositeMon, pickedMove)
        if oppositeSide.isDefeated():
            self.__completeBattle(f'{oppositeMon.nickname} has fainted !')
        else:
            self.write(f'{oppositeMon.nickname} has {oppositeMon.currentHealth}/{oppositeMon.maxHealth} health !')

    def __battleLoop(self) -> None:
        while self.__hasCompleted() == False:
            self.__executeTurn()
        return

    def __hasCompleted(self):
        return self.completed
            
    def __completeBattle(self, message:str):
        self.write(message)
        self.completed = True
        return
    
    def attack(self, attacker:SpecificMon, defender:SpecificMon, move:Move):
        attackType : Type = move.type
        damageEffectiveness : float = defender.weakTo(attackType)
        defense : int = 80
        damage = int(self.__damageVariation((attacker.attack / defense) * move.power * damageEffectiveness))
        defender.loseHealth(damage)
        
        if damageEffectiveness == 0:
            self.write(f"{defender.nickname} is immune to {attackType} !")
        else :
            effectivenessMessage : str = self.__getEffectivenessMessage(damageEffectiveness)
            self.write(f"{attacker.nickname} used {move} to deal {damage} to {defender.nickname}. {effectivenessMessage}")
        return
    
    def __getEffectivenessMessage(self, damageEffectiveness : float) -> str:
        effectivenessMessage = ""
        if damageEffectiveness >= 2 :
            effectivenessMessage =  "It was super effective !"
        elif damageEffectiveness == 0.5:
            effectivenessMessage = "It was not very effective"
        return effectivenessMessage
    
    def __damageVariation(self, damage : float):
        return damage * random.uniform(self.DAMAGE_VARIATION_MIN, self.DAMAGE_VARIATION_MAX)
        
    def writeImplicit(self, text : str):
        self.log.addImplicitLine(self.turn, text)
        
    def getTurnLog(self) -> str:
        return self.log.getFormattedLine(self.turn)