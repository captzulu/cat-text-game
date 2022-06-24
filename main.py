from dataFactory import dataFactory
import _globals  
from gameObjects.battle import Battle
from gameObjects.specificMon import SpecificMon
from gameObjects.side import Side

def loadData():
    _globals.types = dataFactory.loadClassDict('type') 
    _globals.genericMons = dataFactory.loadClassDict('generic_mon')

def main():
    playerName = _globals.playerName = input("What's your name? > ").capitalize()
    print(f'Your name is {playerName}')
    fight()

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

def fight():
    monster1 = SpecificMon(_globals.genericMons['1'], 10)
    monster2 = SpecificMon(_globals.genericMons['2'], 10)
    side1 = Side([monster1], monster1, _globals.playerName)
    side2 = Side([monster2], monster2)
    battle = Battle(side1, side2)
    while(True):
        if battle.hasCompleted():
            return

        battle.executeIntro()
        battle.executeTurn()
    return
        
def input_list(list):
    for item in list:
        print(item)
    return input('> ')

if __name__ == '__main__':
    loadData()
    main()
