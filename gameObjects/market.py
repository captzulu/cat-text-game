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
        choices = {index:item[0] for (index, item) in self.selection.items()}
        pickedOption : tuple[str, int] = self.selection[menuFunctions.menuInt(choices)]
        _globals.player.gold -= pickedOption[1]
        if pickedOption[0] == 'Level up':
            _globals.player.party.activeMon.levelUp()
        elif pickedOption[0] == 'Back':
            return
        
