import pygame.draw
from pygame.surface import Surface
from dataclasses import dataclass, field
from screenObjects.screenObject import ScreenObject
from dataObjects.enums.colors import Colors
from dataObjects.position import Position
from dataObjects.fourSides import FourSides
from typing import Callable
import ext_modules.ptext as ptext
import _globals

@dataclass
class Map(ScreenObject):
    title: str
    titleBox: 
    border: FourSides
    margin: FourSides
    position: Position = field(default_factory=Position)
    
    def __post_init__(self):
        distanceFromLeftEdge : int = self.border.l + self.margin.l
        distanceFromRightEdge : int = self.border.r + self.margin.r
        distanceFromBottomEdge : int = self.border.b + self.margin.b
        distanceFromTopEdge : int = self.border.t + self.margin.t
        width : int = _globals.X - distanceFromLeftEdge - distanceFromRightEdge
        height : int = _globals.Y - distanceFromTopEdge - distanceFromBottomEdge
        self.position = Position(distanceFromLeftEdge, distanceFromBottomEdge, width, height)

    def render(self,  screen : Surface):
        pygame.draw.rect(screen, Colors.GRAY.value, self.position.getTuple())

    def getInnerPosition(self) -> Position:
        return Position(self.position.x + self.border.l,
                        self.position.y + self.border.t,
                        self.position.w - (self.border.l + self.border.r),
                        self.position.h - (self.border.t + self.border.b))