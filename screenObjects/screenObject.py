from abc import ABC, abstractmethod
from dataObjects.position import Position
from pygame.surface import Surface
from pygame import Rect
class ScreenObject(ABC):
    def getPosition(self) -> Position:
        return self.position

    def setPosition(self, position : Position) -> None:
        self.position : Position = position  
        
    def getRect(self) -> Rect:
        return Rect(self.position.getTuple())
    
    @abstractmethod
    def click(self):
        ...

    @abstractmethod
    def render(self, screen : Surface):
        ...