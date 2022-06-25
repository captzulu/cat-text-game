import pygame
from dataFactory import dataFactory
import _globals  
from game import Game
from gameObjects.battle import Battle
from gameObjects.specificMon import SpecificMon
from gameObjects.side import Side
from dataObjects.enums.gameStates import GameStates

def loadData():
    _globals.types = dataFactory.loadClassDict('type') 
    _globals.genericMons = dataFactory.loadClassDict('genericMon')

def main():
    #playerName = _globals.playerName = input("What's your name? > ").capitalize()
    #print(f'Your name is {playerName}')
    pygame.init()
    pygame.display.set_caption("Pokemon Clone")
    game = Game()
    while game.gameState == GameStates.RUNNING:
        game.run()

def input_dict(dict):
    valuesList = list(dict.values())
    choices = makeOrderedChoices(valuesList)
    for i, text in choices.items():
        print(str(i) + '. ' + str(text))

    while(True):
        textInputted = input('> ')
        if textInputted.isnumeric() and int(textInputted) in choices.keys():
            textInputted = choices[int(textInputted)]

        if textInputted in choices.values():
            for key, text in dict.items():
                if text == textInputted:
                    return key
        print(f"'{textInputted}' is not a valid choice. Pick again :")

def makeOrderedChoices(dict_values):
    choices = {
        i : dict_values[i - 1]
        for i in range(1, len(dict_values) + 1)
        }
    return choices

if __name__ == '__main__':
    loadData()
    main()
