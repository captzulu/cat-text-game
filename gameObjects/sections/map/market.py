from dataclasses import dataclass, field
from cliObjects.menuFunctions import menuFunctions
from gameObjects.sections.map.marketItem import MarketItem
import _globals
from typing import TypeVar
Obj = TypeVar('Obj')
@dataclass
class Market:
    selection: dict[int, MarketItem] = field(init=False)

    def generateSelection(self):
        self.selection : dict[int, MarketItem] = dict()
        self.selection[0] = MarketItem('Level up', _globals.player.party.activeMon.levelUp, 10)
        self.selection[1] = MarketItem('Back', lambda : True, 0)
        
    def marketMenu(self):
        exitMenu = False
        while exitMenu != True:
            if not hasattr(self,'selection'):
                self.generateSelection()
            selection : dict[int, tuple[str, MarketItem]] = self.pickFromSelection()
            item = menuFunctions.menuObject(selection)
            if item.name == 'Back':
                exitMenu = True
                continue
            if self.processPayment(item):
               item.giveItem()
                
    def pickFromSelection(self) -> dict[int, tuple[str, MarketItem]]:
        items : dict[int, tuple[str, MarketItem]] = dict()
        for i, item in self.selection.items():
            items[i] = (item.name, item)
        return items
    
    def processPayment(self, item : MarketItem) -> bool:
        if _globals.player.gold >= item.price:
            _globals.player.takeGold(item.price)
            print(f"You bought {item.name} for {item.price}g. You now have {_globals.player.gold}g")
            return True
        else:
            print(f"You have {_globals.player.gold}g, you need {item.price}g to buy {item.name}")
            return False
        
