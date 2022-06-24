from dataFactory import dataFactory
from globals import _GLOBALS

def loadData():
    _GLOBALS['types'] = dataFactory.loadClassDict('type') 
    _GLOBALS['cats'] = dataFactory.loadClassDict('cat')

def main():
    MODE_1_KEY = 'fight'
    MODE_2_KEY = 'cats'
    modes = {mode1: MODE_1_KEY, mode2: MODE_2_KEY}

    playerName = _GLOBALS['playerName'] = input("What's your name? > ").capitalize()
    print(f'Your name is {playerName}')

    print('Choose a mode : ')
    
    modePicked = input_dict(modes)
    modePicked()

def mode1():
    monster1 = _GLOBALS['cats'][1]
    monster1 = _GLOBALS['cats'][2]

    While()
    return

def mode2():
    cats = dataFactory.loadClassDict('cat')
    print('Choose a cat :')
    catPicked = input_dict(cats)
    return

def input_list(list):
    for item in list:
        print(item)
    return input('> ')

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
