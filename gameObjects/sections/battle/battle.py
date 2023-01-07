from dataclasses import dataclass, field
from gameObjects.sections.battle.battleLog import BattleLog
from gameObjects.specificMon import SpecificMon
from dataObjects.genericMon import GenericMon
from gameObjects.sections.battle.side import Side
from dataObjects.type import Type
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
            
        pickedTypeFirst : Type = self.__pickTypeAi(firstSide.getActiveMonSpecies()) if firstSide.isAi else self.__takeTurn()
        self.__sideTurn(firstSide, secondSide, pickedTypeFirst)
        if self.__hasCompleted() == False:
            pickedTypeSecond : Type = self.__pickTypeAi(secondSide.getActiveMonSpecies()) if secondSide.isAi else self.__takeTurn()
            self.__sideTurn(secondSide, firstSide, pickedTypeSecond)
    
    def __pickTypeAi(self, pokemonSpecies : GenericMon) -> Type:
        if pokemonSpecies.type2 != None:
            pickedType = random.choice([1,2])
            return pokemonSpecies.type1 if pickedType == 1 else pokemonSpecies.type2

        return pokemonSpecies.type1
        
    def __takeTurn(self) -> Type:
        return self.__pickAttackType() if self.side1.getActiveMonSpecies().type2 != None else self.side1.getActiveMonSpecies().type1

    def __pickAttackType(self) -> Type:
        types : dict[int, str] = dict()
        i : int = 1
        types[1] = self.side1.getActiveMonSpecies().type1.acronym
        if self.side1.getActiveMonSpecies().type2 != None:
            types[2] = self.side1.getActiveMonSpecies().type2.acronym
        pickedTypeAcr : str = types[menuFunctions.input_dict(types)]
        return _globals.types[pickedTypeAcr]

    def __sideTurn(self, side : Side, oppositeSide : Side, attackType : Type):
        oppositeMon = oppositeSide.activeMon
        self.attack(side.activeMon, oppositeMon, attackType)
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
    
    def attack(self, attacker:SpecificMon, defender:SpecificMon, attackType:Type):
        damageEffectiveness : float = defender.weakTo(attackType)
        damage = int(self.__damageVariation(attacker.attack * damageEffectiveness))
        defender.loseHealth(damage)
        
        if damageEffectiveness == 0:
            self.write(f"{defender.nickname} is immune to {attackType.name} !")
        else :
            effectivenessMessage : str = self.__getEffectivenessMessage(damageEffectiveness)
            self.write(f"{attacker.nickname} dealt {damage} to {defender.nickname}. {effectivenessMessage}")
        return
    
    def __getEffectivenessMessage(self, damageEffectiveness : float) -> str:
        if damageEffectiveness == 1:
            return ""
        elif damageEffectiveness >= 2 :
            return "It was super effective !"
        elif damageEffectiveness == 0.5:
            return"It was not very effective"
    
    def __damageVariation(self, damage : float):
        return damage * random.uniform(self.DAMAGE_VARIATION_MIN, self.DAMAGE_VARIATION_MAX)
        
    def writeImplicit(self, text : str):
        self.log.addImplicitLine(self.turn, text)
        
    def getTurnLog(self) -> str:
        return self.log.getFormattedLine(self.turn)
    
