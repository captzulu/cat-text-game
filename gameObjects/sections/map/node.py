import random

class Node():
    NAME_LIST = ['city', 'market', 'fight', 'chickens', 'rest']
    
    def __init__(self, id : int, name : str, columnIndex : int, backLinks : list[int], forwardLinks : list[int]=list()):
        self.id : int = id
        self.name : str = name 
        self.backLinks : list[int] = backLinks 
        self.forwardLinks : list[int] = forwardLinks
        self.columnIndex : int = columnIndex
    
    def __str__(self) -> str:
        return f"{{{self.id}:{self.name} {self.backLinks}}}"

    @staticmethod
    def randomName() -> str:
        results : list[str] = random.choices(Node.NAME_LIST, weights=[1, 1, 8, 1, 5])
        return results[0]

    @staticmethod
    def randomBackLinks(previousIds : list[int]) -> list[int]:
        if len(previousIds) == 0:
            return []

        amount : int = random.choices([1, 2, 3], weights=[2, 5, 3])[0]
        results : list[int] = list()
        while amount > 0 and len(previousIds) > 0:
            pickedId: int = random.choice(previousIds)
            results.append(pickedId)
            previousIds.remove(pickedId)
            amount -= 1
        return results
    