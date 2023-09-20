from gameObjects.specificMon import SpecificMon
class Status():

    @staticmethod
    def poison(mon : SpecificMon):
        hpLost = mon.loseMaxHealthPercent(100/12)
        print(f"{mon.nickname} suffers from poison ({hpLost if hpLost > 0 else 1} hp)")