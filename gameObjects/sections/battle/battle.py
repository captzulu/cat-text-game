from dataclasses import dataclass, field
from gameObjects.sections.battle.battleLog import BattleLog
from gameObjects.sections.battle.effectLib import EffectLib
from gameObjects.specificMon import SpecificMon
from dataObjects.genericMon import GenericMon
from gameObjects.sections.battle.side import Side
from dataObjects.type import Type
from dataObjects.move import Move
import random
from cliObjects.menuFunctions import menuFunctions
import time
import _globals

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
    quickMode: bool = False
    winner : Side = field(init=False)
    sideWithPriority : Side | None = None  
    
    def executeBattle(self):
        self.__executeIntro()
        input("Hit a key to start the fight...")
        print()
        self.battleLoop()

    def __executeIntro(self):
        title = f"Battle ! {self.side1.name} Vs {self.side2.name}"
        titleLine = self.edgeSymbol + self.writeTitle(title) + self.edgeSymbol
        self.write(titleLine)
        self.write(str(self.side1.activeMon))
        
        longestMonNameLength = self.calculateLongestMonNameLength()
        paddingLength = longestMonNameLength // 2
        self.write(' ' * paddingLength + 'VS' + (' ' * paddingLength))
        self.write(str(self.side2.activeMon))
        self.write(self.edgeSymbol + (self.Filler * longestMonNameLength) + self.edgeSymbol)

    def writeTitle(self, title:str) -> str:
        longestMonNameLength = self.calculateLongestMonNameLength()
        titleLineHalf : str = self.Filler * ((longestMonNameLength - len(title)) // 2)
        return titleLineHalf + title + titleLineHalf
    
    def showStatusPanel(self) -> None:
        mon1 = self.side1.activeMon
        mon2 = self.side2.activeMon
        spacer = "¦"
        mon1str = f"{mon1.nickname} {spacer} lvl:{str(mon1.level)} {spacer} {mon1.genericMon.printTypeAcronyms()}"
        mon2str = f"{mon2.nickname} {spacer} lvl:{str(mon2.level)} {spacer} {mon2.genericMon.printTypeAcronyms()}"
        padding = self.__calculatePadding(len(mon1str + mon2str))
        print(mon1str + padding + mon2str)
        
        mon1HpBar = self.getHpBar(mon1.currentHealth, mon1.maxHealth, length = 25)
        mon2HpBar = self.getHpBar(mon2.currentHealth, mon2.maxHealth, length = 25)
        padding = self.__calculatePadding(len(mon1HpBar + mon2HpBar))
        print(mon1HpBar + padding + mon2HpBar)
    
    def __calculatePadding(self, textLength : int, paddingChar : str = " ") -> str:
        return (_globals.terminalSize.columns - textLength) * paddingChar
        
    def getHpBar(self, iteration :int, total : int, decimals : int = 0, length : int = 100) -> str:
        if total == 0:
            return f'HP : |0| 0%'
        
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = '█' * filledLength + '-' * (length - filledLength)
        return f'HP : |{bar}| {percent}%'

    def write(self, text : str):
        if hasattr(self, 'log') == False:
            self.log = BattleLog()
        self.log.addExplicitLine(self.turn, text)
        self.log.addImplicitLine(self.turn, text)
        print(text)
        if not self.quickMode:
            time.sleep(0.10)
    
    def calculateLongestMonNameLength(self) -> int:
        mon1Length = len(str(self.side1.activeMon))
        mon2Length = len(str(self.side2.activeMon))
        return mon1Length if mon1Length > mon2Length else mon2Length

    def __executeTurn(self):
        self.write(f"\n==== New turn ({self.turn}) ====")
        self.__attackPhase()
        if self.turn >= 100:
            winner = self.side1 if self.side1.activeMon.currentHealth > self.side2.activeMon.currentHealth else self.side2
            self.__completeBattle(f'{winner.activeMon.nickname} has stalled out the win !', winner)
            return
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
        
        prioritySide = self.__checkPriority()
        if prioritySide:
            return prioritySide

        if side1Speed == side2Speed:
            firstSide = self.side1 if random.randint(0,1) == 1 else self.side2
        else:
            firstSide = self.side1 if side1Speed > side2Speed else self.side2
        return firstSide
    
    def __checkPriority(self) -> Side | None:
        if self.side1 == self.sideWithPriority:
            return self.side1
        
        if self.side2 == self.sideWithPriority:
            return self.side2
        
        return None
 
    def __takeTurn(self, side : Side) -> Move:
        pickedMoveFirst : Move = self.__pickMoveAi(side.getActiveMonSpecies()) if side.isAi else self.__pickMove(side)
        return pickedMoveFirst 

    def __pickMove(self, side : Side) -> Move:
        print("Pick a move to use :")
        moves : dict[int, tuple[str, Move]] = dict()
        activeMon : SpecificMon = side.activeMon
        for i, move in activeMon.genericMon.moves.items():
            moves[i] = (move.name, move)

        if _globals.debug:
            debugMove : Move = Move("[Debug] Instant Kill", 100000, 'ste')
            moves[len(moves)] = (debugMove.name, debugMove)

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
            self.__completeBattle(f'{oppositeMon.nickname} has fainted !', side)
        else:
            self.write(f'{oppositeMon.nickname} has {oppositeMon.currentHealth}/{oppositeMon.maxHealth} health !')

    def battleLoop(self) -> None:
        while self.__hasCompleted() == False:
            self.showStatusPanel()
            self.__executeTurn()
            print()
        return

    def __hasCompleted(self):
        return self.completed
            
    def __completeBattle(self, message:str, winner:Side):
        self.write(message)
        self.completed = True
        self.winner = winner
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
            if move.effect != '' and move.effect in EffectLib.triggerList['afterMove']:
               eval("EffectLib." + str.lower(move.effect) + "(defender, move.effectPower)")
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