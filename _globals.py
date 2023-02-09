from dataObjects.move import Move
from dataObjects.type import Type
from dataObjects.genericMon import GenericMon
from gameObjects.sections.player.player import Player
from screenObjects.screenObject import ScreenObject
types: dict[str, Type] = {}
moves: dict[str, Move] = {}
genericMons: dict[str | int, GenericMon] = {}
player: Player
X: int = 600
Y: int = 400
objects: dict[str, ScreenObject] = {}
clickables: list[ScreenObject] = []
