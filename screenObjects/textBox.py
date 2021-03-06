import pygame.draw
from pygame.surface import Surface
from dataclasses import dataclass
from screenObjects.screenObject import ScreenObject
from dataObjects.enums.colors import Colors
from dataObjects.position import Position
from dataObjects.fourSides import FourSides
from typing import Callable
import ext_modules.ptext as ptext

@dataclass
class TextBox(ScreenObject):
    text: str
    position: Position
    border: FourSides = FourSides.fromTuple((0,0,0,0))
    margin: FourSides = FourSides.fromTuple((0,0,0,0))
    onClick: Callable[..., None] = lambda a: None

    def render(self,  screen : Surface):
        pygame.draw.rect(screen, Colors.DARK_GRAY.value, self.position.getTuple())
        innerRect = self.getInnerPosition()
        pygame.draw.rect(screen, Colors.GRAY.value, innerRect.getTuple())
        textSurf, pos = ptext.draw(self.text, (innerRect.x + self.margin.l, innerRect.y + self.margin.t), fontsize = 14)
        screen.blit(textSurf, pos)

    def getInnerPosition(self) -> Position:
        return Position(self.position.x + self.border.l,
                        self.position.y + self.border.t,
                        self.position.w - (self.border.l + self.border.r),
                        self.position.h - (self.border.t + self.border.b))
        
    def click(self):
        self.onClick()
    
    def setClickEvent(self, callback : Callable[..., None]):
        self.onClick : Callable[..., None] = callback