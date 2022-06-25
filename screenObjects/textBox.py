import pygame.draw
from pygame.surface import Surface
from pygame.font import Font
from dataclasses import dataclass
from screenObjects.screenObject import ScreenObject
from dataObjects.enums.colors import Colors
from dataObjects.position import Position
from typing import Callable

@dataclass
class TextBox(ScreenObject):
    text: str
    font: Font
    position: Position
    border: int = 0

    def render(self,  screen : Surface):
        printedText : Surface = self.font.render(self.text, True, Colors.WHITE.value, Colors.BLACK.value)
        pygame.draw.rect(screen, Colors.WHITE.value, self.position.getTuple())
        innerRect = self.getInnerPosition()
        rect = pygame.draw.rect(screen, Colors.GRAY.value, innerRect.getTuple())
        screen.blit(printedText, rect)

    def getInnerPosition(self) -> Position:
        return Position(self.position.x + self.border,
                        self.position.y + self.border,
                        self.position.w - self.border * 2,
                        self.position.h - self.border * 2)
        
    def click(self):
        self.onClick(self)
    
    def setClickEvent(self, callback : Callable[..., None]):
        self.onClick : Callable[..., None] = callback