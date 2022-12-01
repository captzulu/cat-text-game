from dataclasses import dataclass
@dataclass
class Node():
    name: str
    backLink: list[int]
    forwardLink: list[int]