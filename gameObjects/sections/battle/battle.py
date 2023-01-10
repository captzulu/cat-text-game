from dataclasses import dataclass, field
from gameObjects.sections.battle.battleLog import BattleLog
from gameObjects.specificMon import SpecificMon
from dataObjects.genericMon import GenericMon
from gameObjects.sections.battle.side import Side
from dataObjects.type import Type
from dataObjects.move import Move
import random
from cliObjects.menuFunctions import menuFunctions
import _globals
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
        print(self.getTurnLog())

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
        
    def __takeTurn(self, side : Side) -> Move:
        pickedMoveFirst : Move = self.__pickMoveAi(side.getActiveMonSpecies()) if side.isAi else self.__pickMove(side.getActiveMonSpecies())
        return pickedMoveFirst 

    def __pickMove(self, pokemonSpecies : GenericMon) -> Move:
        moves : dict[int, tuple[str, Move]] = dict()
        for i, move in pokemonSpecies.moves.items():
            moves[i] = (move.name, move) 
        pickedMove : Move = menuFunctions.menuObject(moves)
        return pickedMove
    
    def __pickMoveAi(self, pokemonSpecies : GenericMon) -> Move:
        pickedMoveId = random.choice(range(0,len(_globals.moves)))
        pickedMove : Move = pokemonSpecies.moves[pickedMoveId]
        return pickedMove

    def __sideTurn(self, side : Side, oppositeSide : Side):
        pickedMove: Move = self.__takeTurn(side)
        oppositeMon = oppositeSide.activeMon
        self.attack(side.activeMon, oppositeMon, pickedMove)
        if oppositeSide.isDefeated():
            self.__completeBattle(f'{oppositeMon.nickname} has fainted !')
        else:
            self.write(f'{oppositeMon.nickname} has {oppositeMon.currentHealth}/{oppositeMon.maxHealth} health !')

    def __battleLoop(self) -> None:
        while self.__hasCompleted() == False:
            self.__executeTurn()
            print(self.getTurnLog())
            if self.__hasCompleted() == False:
                input("Hit a key to continue...")
        return

    def __hasCompleted(self):
        return self.completed
            
    def __completeBattle(self, message:str):
        self.write(message)
        self.completed = True
        return
    
    def attack(self, attacker:SpecificMon, defender:SpecificMon, move:Move):
        attackType:Type = move.type
        damageEffectiveness : float = defender.weakTo(attackType)
        defense : int = 50
        damage = int(self.__damageVariation((attacker.attack / defense) * move.power * damageEffectiveness))
        defender.loseHealth(damage)
        
        if damageEffectiveness == 0:
            self.write(f"{defender.nickname} is immune to {attackType.name} !")
        else :
            effectivenessMessage : str = self.__getEffectivenessMessage(damageEffectiveness)
            self.write(f"{attacker.nickname} dealt {damage} to {defender.nickname}. {effectivenessMessage}")
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
    
