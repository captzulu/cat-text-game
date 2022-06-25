from dataclasses import dataclass  
@dataclass
class Position:
    x: int = 0
    y: int = 0
    w: int = 0
    h: int = 0

    @classmethod
    def fromTuple(cls, pos : tuple[int, int, int, int]):
        return cls(pos[0], pos[1], pos[2], pos[3])
    
    def getTuple(self) -> tuple[int, int, int, int]:
        return (self.x, self.y, self.w, self.h)
    
    def modifyBy(self, mod : tuple[int, int, int, int]):
        self.x += mod[0]
        self.y += mod[1]
        self.w += mod[2]
        self.h += mod[3]
