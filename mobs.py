"""HP-здоровье,AP-ловкость,SP-сила,LVL-уровень"""

import random

class mobs:
    def __init__(self,HP,AP,SP,LVL):
        self.lvl=LVL
        self.hp=HP*self.lvl
        self.ap=AP*self.lvl
        self.sp=SP*self.lvl
    def __str__(self):
        Hp=f"Очки здоровья:{self.hp}"
        Ap=f"Очки ловкости:{self.ap}"
        Sp=f"Очки силы:{self.sp}"
        Lvl=f"Уровень:{self.lvl}"
        t=type(self).__name__
        return f"{t}\n{Hp}\n{Ap}\n{Sp}\n{Lvl}"
    def __repr__(self) :
        return self.__str__()
class Zombie(mobs):
    def __init__(self, HP=100, AP=2, SP=2, LVL=random.randrange(1,5)):
        self.lvl=LVL
        self.hp=HP
        self.ap=AP
        self.sp=SP
    
Zombie.__name__="Зомби"   

#снизу пробный вариант Зомби
"""  self.lvl=LVL
        self.hp=HP*self.lvl
        self.ap=AP*self.lvl
        self.sp=SP*self.lvl
    def __str__(self) -> str:
        Hp=f"Heals point:{self.hp}"
        Ap=f"Очки ловкости:{self.ap}"
        Sp=f"Очки силы:{self.sp}"
        Lvl=f"Уровень:{self.lvl}"
        return Hp+Ap+Sp+Lvl
   """  
   