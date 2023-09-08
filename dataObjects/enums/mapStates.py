from enum import Enum, auto
class MapStates(Enum):
    STARTED = auto()
    FAILED = auto()
    COMPLETED = auto()
    READY = auto()