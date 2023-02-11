import pygame
import _globals
import random
from dataObjects.position import Position
from dataObjects.enums.gameStates import GameStates
from dataObjects.enums.colors import Colors
from screenObjects.menu import Menu
from screenObjects.textBox import TextBox
from gameObjects.sections.battle.battle import Battle
from gameObjects.specificMon import SpecificMon
from gameObjects.sections.battle.side import Side
from dataObjects.fourSides import FourSides
class Game:
    def __init__(self) -> None:
        self.mainScreen : pygame.surface.Surface = pygame.display.set_mode((_globals.X, _globals.Y))
        self.gameState : GameStates = GameStates.RUNNING
        self.mainTextBox:TextBox = self.__initMainTextbox()
        self.mainScreen.fill(Colors.BLACK.value)
        options = dict({0 : (f"Fight", self.enterFight), 1 : (f"Quit", self.quit)})
        _globals.objects['menu'] = Menu(options, self.mainTextBox.getInnerPosition())
        
    def __initMainTextbox(self) -> TextBox:
        pos = Position(y = int(_globals.Y / 1.35),  w =_globals.X)
        pos.h = _globals.Y - pos.y
        _globals.objects['mainText'] = TextBox('', pos, FourSides.fromTuple((5,5,5,5)), FourSides.fromTuple((5,5,10,10)))
        return _globals.objects['mainText']

    def quit(self):
        self.gameState = GameStates.ENDED
        exit()

    def run(self):
        self.__handleEvents()
        self.__update()
        pygame.time.Clock().tick(30)

    def __handleEvents(self):
        for event in pygame.event.get():
            self.__checkEvents(event)
    
    def __checkEvents(self, event : pygame.event.Event):
        if event.type == pygame.QUIT:
            self.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.quit()
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for obj in _globals.clickables:
                if obj.getRect().collidepoint(pos):
                    obj.click()
    
    def __update(self):
        for obj in _globals.objects.values():
            obj.render(self.mainScreen)
        pygame.display.flip()
                        
    def enterFight(self):
        monNo1 = str(random.randint(0, len(_globals.genericMons) - 1))
        monNo2 = str(random.randint(0, len(_globals.genericMons) - 1))
        monster1 = SpecificMon(_globals.genericMons[monNo1], 10)
        monster2 = SpecificMon(_globals.genericMons[monNo2], 10)
        side1 = Side([monster1], monster1, _globals.player.name)
        side2 = Side([monster2], monster2)
        battle = Battle(side1, side2)
        mainMenu : Menu = _globals.objects.pop('menu')
        mainMenu.removeClickables()
        battle.executeIntro()
        self.displayTurnLog(battle)
        while battle.hasCompleted() == False:
            battle.executeTurn()
            self.displayTurnLog(battle)
        self.mainTextBox.text = ''
        _globals.objects['menu'] = mainMenu
        return
    
    def displayTurnLog(self, battle : Battle):
        self.mainTextBox.text = battle.getTurnLog()
        self.__update()
        self.__waitForClick()
    
    def __waitForClick(self):
        #pygame.event.clear()
        while True:
            for event in pygame.event.get():
                self.__checkEvents(event)
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        return