from typing import Callable, TypeVar
Obj = TypeVar('Obj')
class menuFunctions():
    @staticmethod
    def menuCallable(choices : list[tuple[str, Callable]]) -> bool:
        orderedChoices = menuFunctions.makeOrderedChoices(choices)
        menuFunctions.printTupleChoices(orderedChoices)

        while(True):
            textInputted = input('> ')
            if textInputted.isnumeric() and int(textInputted) in orderedChoices.keys():
                print()
                return orderedChoices[int(textInputted)][1]()

            print(f"'{textInputted}' is not a valid choice. Pick again :")

    @staticmethod
    def makeOrderedChoices(values):
        choices = {
            i : values[i - 1]
            for i in range(1, len(values) + 1)
            }
        return choices

    @staticmethod
    def printTupleChoices(choices : dict) -> None:
        for i, item in choices.items():
            text: str = item[0]
            print(str(i) + '. ' + text)

    @staticmethod
    def menuInt(dictIn : dict[int, str]) -> int:
        valuesList: list[str] = list(dictIn.values())
        choices: dict[int, str] = menuFunctions.makeOrderedChoices(valuesList)
        for i, text in choices.items():
            print(str(i) + '. ' + str(text))

        while(True):
            textInputted: str = input('> ')
            if textInputted.isnumeric() and int(textInputted) in choices.keys():
                textInputted = choices[int(textInputted)]

            #this is necessary to be able to enter a dict with IDs as keys and get that id back 
            # and not the ordered choice index
            if textInputted in choices.values():
                for key, text in dictIn.items():
                    if text == textInputted:
                        print()
                        return key
            print(f"'{textInputted}' is not a valid choice. Pick again :")
    
    @staticmethod
    def menuObject(choices : list[tuple[str, Obj]]) -> Obj:
        choicesDict = menuFunctions.makeOrderedChoices(choices)
        menuFunctions.printTupleChoices(choicesDict)

        while(True):
            textInputted = input('> ')
            if textInputted.isnumeric() and int(textInputted) in choicesDict.keys():
                print()
                return choicesDict[int(textInputted)][1]

            print(f"'{textInputted}' is not a valid choice. Pick again :")