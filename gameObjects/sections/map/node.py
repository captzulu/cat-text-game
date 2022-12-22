from dataclasses import dataclass
@dataclass
class Node():
    id: int
    name: str
    backLink: list[int]
    forwardLink: list[int]