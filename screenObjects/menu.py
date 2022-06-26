from pygame.surface import Surface
from pygame.font import Font
import _globals
from dataclasses import dataclass, field
from screenObjects.screenObject import ScreenObject
from screenObjects.textBox import TextBox
from dataObjects.position import Position
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
            newOption = TextBox(option[0], self.font, Position.fromTuple((x, y, w, h)), border = 2)
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