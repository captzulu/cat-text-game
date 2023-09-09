from dataclasses import dataclass, field
from cliObjects.menuFunctions import menuFunctions
import _globals
@dataclass
class Market:
    selection: dict[int, tuple[str, int]] = field(init=False)

    def generateSelection(self):
        self.selection : dict[int, tuple[str, int]] = dict()
        self.selection[0] = ('Level up', 10)
        self.selection[1] = ('Back', 0)
        
    def marketMenu(self):
        if not hasattr(self,'selection'):
            self.generateSelection()
        pickedOption : tuple[str, int] = self.pickFromSelection()
        if pickedOption[0] == 'Back':
            return
        if self.processPayment(pickedOption):
            self.giveItem(pickedOption)
        
        
    def pickFromSelection(self) -> tuple[str, int]:
        choices = {index:item[0] for (index, item) in self.selection.items()}
        return self.selection[menuFunctions.menuInt(choices)]
    
    def processPayment(self, pickedOption : tuple[str, int]) -> bool:
        if _globals.player.gold >= pickedOption[1]: 
            _globals.player.gold -= pickedOption[1]
            print(f"You bought {pickedOption[0]} for {pickedOption[1]}g. You now have {_globals.player.gold}g")
            return True
        else:
            print(f"You have {_globals.player.gold}g, you need {pickedOption[1]}g to buy {pickedOption[0]}")
            return False
            
    def giveItem(self, pickedOption : tuple[str, int]):
        if pickedOption[0] == 'Level up':
            _globals.player.party.activeMon.levelUp()
        
