from dataFactory import dataFactory 
def main():
    MODE_1_KEY = 'mode_1'
    MODE_2_KEY = 'mode_2'
    modes = {MODE_1_KEY: 'mode 1', MODE_2_KEY: 'mode 2'}

    player_name = input("What's your name? > ")
    print(f'Your name is {player_name.upper()}')

    print('Choose a mode : ')
    
    modePicked = input_dict(modes)

    if modePicked == MODE_1_KEY:
        mode1()
    elif modePicked == MODE_2_KEY:
        mode2()

def mode1():
    cats = ['yuki', 'jari', 'néné', 'lolo']
    print('Choose a cat :')
    catPicked = input_list(cats)
    types = dataFactory.loadTypes()
    print(types)
    return

def mode2():
    return

def input_list(list):
    for item in list:
        print(item)
    return input('> ')

def input_dict(dict):
    for key, text in dict.items():
        print(text)
    textSelected = input('> ')
    if textSelected in dict.values():
        for key, text in dict.items():
            if text == textSelected:
                return key
        

if __name__ == '__main__':
    main()