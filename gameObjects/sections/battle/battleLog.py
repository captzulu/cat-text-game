from dataclasses import dataclass, field
@dataclass
class BattleLog:
    explicitLog: dict[int, tuple[str, ...]] = field(init=False)
    implicitLog: dict[int, tuple[str, ...]] = field(init=False)

    def __post_init__(self):
        self.explicitLog = {}
        self.implicitLog = {}
        
    def getFormattedLine(self, turn : int) -> str:
        return ' ' + ' '.join(self.explicitLog[turn]) if len(self.explicitLog) - 1 >= turn else ''

    def addExplicitLine(self, turn : int, line : str):
        if turn not in self.explicitLog.keys():
            self.explicitLog[turn] = ()
        self.explicitLog[turn] += (line , '\n')
            
    def addImplicitLine(self, turn : int, line : str):
        if turn not in self.implicitLog.keys():
            self.implicitLog[turn] = ()
        self.implicitLog[turn] += (line , '\n')