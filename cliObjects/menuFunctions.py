from typing import Callable

class menuFunctions():
    @staticmethod
    def menuCallable(dict : dict[int, tuple[str, Callable]]):
        valuesList = list(dict.values())
        choices = menuFunctions.makeOrderedChoices(valuesList)
        for i, item in choices.items():
            text: str = item[0]
            print(str(i) + '. ' + text)

        while(True):
            textInputted = input('> ')
            if textInputted.isnumeric() and int(textInputted) in choices.keys():
                textInputted: str = choices[int(textInputted)][0]

            for key, item in dict.items():
                text = item[0]
                if text == textInputted:
                    item[1]()
                    return
            print(f"'{textInputted}' is not a valid choice. Pick again :")

    @staticmethod
    def makeOrderedChoices(values):
        choices = {
            i : values[i - 1]
            for i in range(1, len(values) + 1)
            }
        return choices

    @staticmethod
    def input_dict(dict : dict[int, str]):
        valuesList = list(dict.values())
        choices = menuFunctions.makeOrderedChoices(valuesList)
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