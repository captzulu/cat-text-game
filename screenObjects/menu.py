from pygame.surface import Surface
from pygame.font import Font
import _globals
from dataclasses import dataclass, field
from screenObjects.screenObject import ScreenObject
from screenObjects.textBox import TextBox
from dataObjects.position import Position
from dataObjects.fourSides import FourSides
from typing import Callable
@dataclass
class Menu(ScreenObject):
    options : dict[int, tuple[str, Callable[..., None]]]
    font : Font
    position: Position
    renderedOption: list[ScreenObject] = field(default_factory=list)

    def __post_init__(self):
        x = self.position.x
        y = self.position.y
        w = self.position.w // 2
        h = self.position.h // 2
        for i, option in self.options.items():
            mod = (i + 1) % 2
            botBorder = 5 if i < 2 else 0 
            rightBorder = 5 if mod == 1 else 0 
            border = FourSides.fromTuple((0, botBorder, 0 , rightBorder))
            margin = FourSides.fromTuple((5, 5, 5, 5))
            newOption = TextBox(option[0], self.font, Position.fromTuple((x, y, w, h)), border, margin)
            newOption.setClickEvent(option[1])
            self.renderedOption.append(newOption)
            _globals.clickables.append(newOption)
            x = x + (- w if mod == 0 else + w)
            y = y - (h if mod == 0 else 0)

    def render(self, screen : Surface):
        for option in self.renderedOption:
            option.render(screen)
            
    def click(self):
        return