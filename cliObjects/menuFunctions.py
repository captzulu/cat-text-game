from typing import Callable, TypeVar
Obj = TypeVar('Obj')
class menuFunctions():
    @staticmethod
    def menuCallable(dict : dict[int, tuple[str, Callable]]) -> bool:
        valuesList = list(dict.values())
        choices = menuFunctions.makeOrderedChoices(valuesList)
        menuFunctions.printTupleChoices(choices)

        while(True):
            textInputted = input('> ')
            if textInputted.isnumeric() and int(textInputted) in choices.keys():
                textInputted: str = choices[int(textInputted)][0]

            for item in dict.values():
                text: str = item[0]
                if text == textInputted:
                    print()
                    return item[1]()
            print(f"'{textInputted}' is not a valid choice. Pick again :")

    @staticmethod
    def makeOrderedChoices(values):
        choices = {
            i : values[i - 1]
            for i in range(1, len(values) + 1)
            }
        return choices

    @staticmethod
    def printTupleChoices(choices) -> None:
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

            if textInputted in choices.values():
                for key, text in dictIn.items():
                    if text == textInputted:
                        print()
                        return key
            print(f"'{textInputted}' is not a valid choice. Pick again :")
    
    @staticmethod
    def menuObject(dict : dict[int, tuple[str, Obj]]) -> Obj:
        valuesList = list(dict.values())
        choices = menuFunctions.makeOrderedChoices(valuesList)
        menuFunctions.printTupleChoices(choices)

        while(True):
            textInputted = input('> ')
            if textInputted.isnumeric() and int(textInputted) in choices.keys():
                textInputted: str = choices[int(textInputted)][0]

            for item in dict.values():
                text: str = item[0]
                if text == textInputted:
                    print()
                    return item[1]
            print(f"'{textInputted}' is not a valid choice. Pick again :")