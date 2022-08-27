from static import *
"""Ar-защита Pr-цена R-ранг брони St-прочность Ty-тип вещи"""
class Armor:
    def __init__(self,Ar,Pr,R,St,Ty):
        self.ar=Ar
        self.pr=Pr
        self.r=R
        self.st=St
        self.ty=Ty
    def __str__(self):
        Ar=f"Защита:{self.ar}"
        St=f"Прочность:{self.st}"
        R=f"Ранг брони:{self.r}"
        Pr=f"Цена:{self.pr}"
        t=type(self).__name__
        return f"{t}\n{Ar}\n{St}\n{R}\n{Pr}"
    def __repr__(self) :
        return self.__str__()
    
    
class Shirt(Armor):
    def __init__(self, Ar, Pr, R, St, Ty):
        super().__init__(Ar, Pr, R, St, Ty)
Shirt.__name__="Одежда из плотной ткани"    

class Armored_Shirt(Armor):
    def __init__(self, Ar, Pr, R, St, Ty):
        super().__init__(Ar, Pr, R, St, Ty)
Armored_Shirt.__name__="Одежда с металлическими вставками"  

class F_Leather_Armor(Armor):
    def __init__(self, Ar, Pr, R, St, Ty):
        super().__init__(Ar, Pr, R, St, Ty)
F_Leather_Armor.__name__="Дешовая кожанная броня"

class G_Leather_Armor(Armor):
    def __init__(self, Ar, Pr, R, St, Ty):
        super().__init__(Ar, Pr, R, St, Ty)
G_Leather_Armor.__name__="Хорошая кожанная броня"