from dataclasses import dataclass
from typing import Callable
@dataclass
class MarketItem:
    name: str
    giveFonction: Callable
    price: int
    power: int | None = None
    
    def giveItem(self):
        if self.power is not None: 
            self.giveFonction(self.power)
        else:
            self.giveFonction()