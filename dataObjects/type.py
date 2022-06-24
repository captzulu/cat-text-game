from dataclasses import dataclass
from globals import _GLOBALS
@dataclass
class Type:
    name: str
    weaknesses: str
    resistances: str
    immunities: str
    acronym: str

    @staticmethod
    def accessTypeDict(key):
        try:
            return _GLOBALS['types'][key]
        except IndexError:
            print("Oops!  That was no valid number.  Try again...")