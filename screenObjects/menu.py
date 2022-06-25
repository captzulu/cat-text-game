from pygame.surface import Surface
from pygame.font import Font
from dataclasses import dataclass
from screenObjects.screenObject import ScreenObject
from screenObjects.textBox import TextBox
from dataObjects.position import Position
from typing import Callable
@dataclass
class Menu(ScreenObject):
    options : dict[int, tuple[str, Callable[..., None]]]
    font : Font
    position: Position

    def render(self, screen : Surface):
        positionNextBox : Position = Position.fromTuple(self.position.getTuple())
        positionNextBox.w = self.position.w // 2
        positionNextBox.h = self.position.h // 2
        for i, option in self.options.items():
            mod = (i + 1) % 2
            newOption = TextBox(option[0], self.font, positionNextBox, border = 2)
            newOption.setClickEvent(option[1])
            newOption.render(screen)
            positionNextBox.x += - positionNextBox.w if mod == 0 else + positionNextBox.w
            positionNextBox.y += - positionNextBox.h if mod == 0 else 0
            
    def click(self):
        return