import pygame.draw
from pygame.surface import Surface
from dataclasses import dataclass, field
from screenObjects.screenObject import ScreenObject
from dataObjects.enums.colors import Colors
from dataObjects.position import Position
from dataObjects.fourSides import FourSides
from screenObjects.textBox import TextBox
import ext_modules.ptext as ptext
import _globals

@dataclass
class Map(ScreenObject):
    title: str
    titleBox: TextBox = field(init=False)
    border: FourSides = field(default_factory=FourSides)
    margin: FourSides = field(default_factory=FourSides)
    position: Position = field(default_factory=Position)
    
    def __post_init__(self) -> None:
        self.position = Position(0, 0, _globals.X, _globals.Y)
        textBoxWidth : int = _globals.X // 3 
        textBoxHeight : int = 10 
        self.titleBox = TextBox(self.title, Position.fromTuple((self.position.getCenterX(), _globals.Y // 4, textBoxWidth, textBoxHeight)))

    def render(self,  screen : Surface) -> None:
        pygame.draw.rect(screen, Colors.GRAY.value, self.position.getTuple())

    def getInnerPosition(self) -> Position:
        return Position(self.position.x + self.border.l,
                        self.position.y + self.border.t,
                        self.position.w - (self.border.l + self.border.r),
                        self.position.h - (self.border.t + self.border.b))
        
    def click(self) -> None:
        return