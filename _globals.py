from dataObjects.move import Move
from dataObjects.type import Type
from dataObjects.genericMon import GenericMon
from gameObjects.sections.player.player import Player
import os
terminalSize : os.terminal_size = os.get_terminal_size()
types: dict[str, Type] = {}
moves: dict[str, Move] = {}
genericMons: dict[str | int, GenericMon] = {}
player: Player
debug : bool = False
