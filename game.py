import pygame
import _globals
import random
from dataObjects.position import Position
from dataObjects.enums.gameStates import GameStates
from dataObjects.enums.colors import Colors
from screenObjects.menu import Menu
from screenObjects.textBox import TextBox
from gameObjects.battle import Battle
from gameObjects.specificMon import SpecificMon
from gameObjects.side import Side
from dataObjects.fourSides import FourSides
class Game:
    def __init__(self) -> None:
        self.mainScreen : pygame.surface.Surface = pygame.display.set_mode((_globals.X, _globals.Y))
        self.gameState : GameStates = GameStates.RUNNING
        self.font : pygame.font.Font = pygame.font.Font('freesansbold.ttf', 14)
        self.mainTextBox:TextBox = self.initMainTextbox()
        self.mainScreen.fill(Colors.BLACK.value)
        options = dict({0 : (f"fight", self.enterFight), 1 : (f"quit", self.quit)})
        _globals.objects['menu'] = Menu(options, self.font, self.mainTextBox.getInnerPosition())

    def run(self):
        self.handleEvents()
        self.update()
        pygame.time.Clock().tick(20)
    
    def update(self):
        for obj in _globals.objects.values():
            obj.render(self.mainScreen)
        pygame.display.flip()
    
    def initMainTextbox(self) -> TextBox:
        pos = Position(y = int(_globals.Y / 1.35),  w =_globals.X)
        pos.h = _globals.Y - pos.y
        _globals.objects['mainText'] = TextBox('', self.font, pos, FourSides.fromTuple((5,5,5,5)))
        return _globals.objects['mainText']

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameState = GameStates.ENDED
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.gameState = GameStates.ENDED
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                for obj in _globals.clickables:
                    if obj.getRect().collidepoint(pos):
                        obj.click()
                        
    def enterFight(self):
        monNo1 = random.randint(0, len(_globals.genericMons) - 1)
        monNo2 = random.randint(0, len(_globals.genericMons) - 1)
        monster1 = SpecificMon(_globals.genericMons[monNo1], 10)
        monster2 = SpecificMon(_globals.genericMons[monNo2], 10)
        side1 = Side([monster1], monster1, _globals.playerName)
        side2 = Side([monster2], monster2)
        battle = Battle(side1, side2)
        battle.executeIntro()
        mainMenu = _globals.objects.pop('menu')
        while battle.hasCompleted() == False:
            self.mainTextBox.text = battle.getTurnLog()
            self.update()
            self.waitForClick()
            battle.executeTurn()
        self.mainTextBox.text = battle.getTurnLog()
        self.update()
        self.waitForClick()
        self.mainTextBox.text = ''
        _globals.objects['menu'] = mainMenu
        return
    
    def quit(self):
        self.gameState = GameStates.ENDED
        return
    
    def waitForClick(self):
        pygame.event.clear()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    return
