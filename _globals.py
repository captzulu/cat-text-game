from dataObjects.type import Type
from dataObjects.genericMon import GenericMon
from screenObjects.screenObject import ScreenObject
types: dict[str, Type] = {}
genericMons: dict[str | int, GenericMon] = {}
playerName: str = 'trainer'
X: int = 600
Y: int = 400
objects: dict[str, ScreenObject] = {}
clickables: list[ScreenObject] = []
