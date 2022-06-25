import pygame
import _globals
from dataObjects.position import Position
from dataObjects.enums.gameStates import GameStates
from dataObjects.enums.colors import Colors
from screenObjects.menu import Menu
from screenObjects.textBox import TextBox
from screenObjects.screenObject import ScreenObject
from gameObjects.battle import Battle
from typing import Callable

class Game:
    def __init__(self) -> None:
        self.mainScreen : pygame.surface.Surface = pygame.display.set_mode((_globals.X, _globals.Y))
        self.gameState : GameStates = GameStates.RUNNING
        self.font : pygame.font.Font = pygame.font.Font('freesansbold.ttf', 14)
        self.objects : dict[str, ScreenObject] = {}
        self.mainTextBox:TextBox = self.initMainTextbox()
        self.mainScreen.fill(Colors.BLACK.value)

    def run(self):
        #self.mainScreen.fill(Colors.BLACK.value)
        self.handleEvents()
        options = dict({0 : (f"fight", self.enterfight), 1 : (f"quit", lambda:None)})
        self.objects['menu'] = Menu(options, self.font, self.mainTextBox.getInnerPosition())
        self.update()
        pygame.time.Clock().tick(60)
    
    def update(self):
        for obj in self.objects.values():
            obj.render(self.mainScreen)
        pygame.display.flip()
    
    def initMainTextbox(self) -> TextBox:
        pos = Position(y = int(_globals.Y / 1.35),  w =_globals.X)
        pos.h = _globals.Y - pos.y
        self.objects['mainText'] = TextBox('', self.font, pos, border = 5)
        return self.objects['mainText']

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameState = GameStates.ENDED
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.gameState = GameStates.ENDED
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                for obj in self.objects.values():
                    if obj.getRect().collidepoint(pos):
                        obj.click()
                        
    def enterfight():
        monster1 = SpecificMon(_globals.genericMons['1'], 10)
        monster2 = SpecificMon(_globals.genericMons['2'], 10)
        side1 = Side([monster1], monster1, _globals.playerName)
        side2 = Side([monster2], monster2)
        battle = Battle(side1, side2)
        while(True):
            if battle.hasCompleted():
                return

            battle.executeIntro()
            battle.executeTurn()
        return
      
