import random

class Node():
    NAME_LIST = ['city', 'market', 'fight', 'chickens', 'rest']
    
    def __init__(self, id : int, name : str, columnIndex : int, backLinks : list[int], forwardLinks : list[int]=list()):
        self.id = id
        self.name = name 
        self.backLinks = backLinks 
        self.forwardLinks = forwardLinks
        self.columnIndex = columnIndex
    
    @staticmethod
    def randomName() -> str:
        results  = random.choices(Node.NAME_LIST, cum_weights=[1, 1, 17, 1, 5])
        return results[0]

    @staticmethod
    def randomBackLinks(previousIds : list[int]) -> list[int]:
        if len(previousIds) == 0:
            return []

        amount = random.choices([1, 2, 3], cum_weights=[2, 5, 3])[0]
        results = random.choices(previousIds, k=amount)
        return results