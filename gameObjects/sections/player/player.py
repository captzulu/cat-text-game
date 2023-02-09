from dataclasses import dataclass, field
from gameObjects.sections.battle.side import Side
@dataclass
class Player:
    name: str
    party: Side = field(init=False)
    gold: int = 0
    items: list = field(default_factory=list)