from gameObjects.specificMon import SpecificMon
class Status():

    @staticmethod
    def poison(mon : SpecificMon):
        hpLost = mon.loseMaxHealthPercent(100/12, True)
        print(f"{mon.nickname} suffers from poison ({hpLost} hp)")
        
    @staticmethod
    def burn(mon : SpecificMon):
        hpLost = mon.loseMaxHealthPercent(100/20)
        print(f"{mon.nickname} suffers from burn ({hpLost} hp)")
    
    @staticmethod
    def normal(mon : SpecificMon):
        pass
    
    @staticmethod
    def fainted(mon : SpecificMon):
        pass