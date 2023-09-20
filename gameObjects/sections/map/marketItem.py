from dataclasses import dataclass
from typing import Callable
@dataclass
class MarketItem:
    name: str
    giveFonction: Callable
    price: int
    
    def giveItem(self):
        self.giveFonction()