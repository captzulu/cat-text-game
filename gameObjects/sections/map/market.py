from dataclasses import dataclass, field
from cliObjects.menuFunctions import menuFunctions
from gameObjects.sections.map.marketItem import MarketItem
import _globals
@dataclass
class Market:
    selection: list[MarketItem] = field(init=False)

    def generateSelection(self):
        self.selection : list[MarketItem] = list()
        self.selection.append(MarketItem('Level up', _globals.player.party.activeMon.levelUp, 10))
        self.selection.append(MarketItem('Full Heal', _globals.player.party.activeMon.fullHeal, 20))
        self.selection.append(MarketItem('Heal 30%', _globals.player.party.activeMon.healMaxHealthPercent, 5, 30))
        self.selection.append(MarketItem('Back', lambda : True, 0))
        
    def marketMenu(self):
        exitMenu = False
        while exitMenu != True:
            if not hasattr(self,'selection'):
                self.generateSelection()
            choices : list[tuple[str, MarketItem]] = self.makeChoicesFromSelection()
            item = menuFunctions.menuObject(choices)
            if item.name == 'Back':
                exitMenu = True
                continue
            if self.processPayment(item):
               item.giveItem()
                
    def makeChoicesFromSelection(self) -> list[tuple[str, MarketItem]]:
        return [(item.name, item) for item in self.selection]
    
    def processPayment(self, item : MarketItem) -> bool:
        if _globals.player.gold >= item.price:
            _globals.player.takeGold(item.price)
            print(f"You bought {item.name} for {item.price}g. You now have {_globals.player.gold}g")
            return True
        else:
            print(f"You have {_globals.player.gold}g, you need {item.price}g to buy {item.name}")
            return False
        
