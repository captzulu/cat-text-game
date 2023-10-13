from dataObjects.move import Move
from dataObjects.type import Type
from dataObjects.genericMon import GenericMon
from gameObjects.sections.player.player import Player
import shutil
import os
terminalSize : os.terminal_size = shutil.get_terminal_size()
types: dict[str, Type] = {}
moves: dict[str, Move] = {}
genericMons: dict[str | int, GenericMon] = {}
player: Player
debug : bool = True
testMode : bool = False
