from dataclasses import dataclass  
@dataclass
class FourSides:
    t: int = 0
    b: int = 0
    l: int = 0
    r: int = 0

    @classmethod
    def fromTuple(cls, sides : tuple[int, int, int, int]):
        return cls(sides[0], sides[1], sides[2], sides[3])
    
    def getTuple(self) -> tuple[int, int, int, int]:
        return (self.t, self.b, self.l, self.r)
    
