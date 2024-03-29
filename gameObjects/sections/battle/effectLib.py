from gameObjects.specificMon import SpecificMon
import random
class EffectLib:
    triggerList : dict[str, list]= dict({
        "afterMove" : ['poison', 'burn', 'flinch']
    })
    
    @staticmethod
    def checkTriggerList(trigger : str, effect : str) -> bool:
        return effect in EffectLib.triggerList[trigger]
            
    @staticmethod
    def poison(targetMon : SpecificMon, chance : int):
        if targetMon.status == "normal":
            roll = random.randint(1, 100)
            if roll <= chance :
                targetMon.status = 'poison'
                print(f"{targetMon.nickname} was poisoned !")
                
    @staticmethod
    def burn(targetMon : SpecificMon, chance : int):
        if targetMon.status == "normal":
            roll = random.randint(1, 100)
            if roll <= chance :
                targetMon.status = 'burn'
                print(f"{targetMon.nickname} was burned !")
                
    @staticmethod
    def flinch(targetMon : SpecificMon, chance : int):
        roll = random.randint(1, 100)
        if roll <= chance :
            targetMon.flinchCounter += 1
            print(f"{targetMon.nickname} gained 1 flinch, it's at {targetMon.flinchCounter}!")
